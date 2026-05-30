#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <chrono>
#include <unordered_set>

using namespace std;

// === グローバル変数の定義 ===
int N, M, T_limit;
vector<string> v_walls; // 縦方向の壁
vector<string> h_walls; // 横方向の壁
int basket_r[40], basket_c[40]; // カゴの座標
int dist_map[20][20][20][20];   // 2点間の最短距離を保存する4次元配列

// === 盤面の状態を管理する構造体 ===
// C++の構造体(struct)は、関連する変数をひとまとめにするための箱です。
struct State {
    int r, c, dir;       // ロボットの行(r), 列(c), 向き(dir)
    int holding;         // 持っているボールのID（-1なら何も持っていない）
    int turn;            // 現在の消費ターン数
    int placed_count;    // カゴに正しく入ったボールの数
    
    int b_r[40], b_c[40]; // 各ボールの現在の行(r)と列(c)
    int b_status[40];     // ボールの状態 (0: 盤面にある, 1: ロボットが持っている, 2: カゴに入っている)

    long long score;     // この状態の評価スコア
    int parent_idx;      // 直前のターンにおける「親」状態のインデックス（経路復元用）
    char last_action;    // 親からこの状態になるために実行したアクション(F, R, L, S)
};

// === ハッシュ値の計算関数 ===
// 盤面の状態を64ビットの整数1つに変換します。同じ盤面なら必ず同じ数値になります。
uint64_t compute_hash(const State& s) {
    uint64_t h = 14695981039346656037ULL; 
    // ラムダ式（関数の中に関数を作るC++の便利な書き方）
    auto combine = [&](uint64_t val) {
        h ^= val;
        h *= 1099511628211ULL;
    };
    
    combine(s.r); combine(s.c); combine(s.dir); combine(s.holding);
    for (int i = 0; i < M; ++i) {
        combine(s.b_r[i]); combine(s.b_c[i]); combine(s.b_status[i]);
    }
    return h;
}

// === 壁の判定関数 ===
// 現在のマス(r, c)から、指定した方向(dir)へ進めるかどうかを返します。
bool has_wall(int r, int c, int dir) {
    if (dir == 0) return c + 1 >= N || v_walls[r][c] == '1'; // 右
    if (dir == 1) return r + 1 >= N || h_walls[r][c] == '1'; // 下
    if (dir == 2) return c - 1 < 0  || v_walls[r][c - 1] == '1'; // 左
    if (dir == 3) return r - 1 < 0  || h_walls[r - 1][c] == '1'; // 上
    return true;
}

// === 状態を1手進める関数 ===
State advance_state(State s, char action) {
    s.turn++;
    s.last_action = action;
    
    if (action == 'F') { // 前進
        int nr = s.r, nc = s.c;
        if (s.dir == 0) nc++; else if (s.dir == 1) nr++;
        else if (s.dir == 2) nc--; else if (s.dir == 3) nr--;
        
        if (!has_wall(s.r, s.c, s.dir)) {
            s.r = nr; s.c = nc;
        }
    } 
    else if (action == 'R') { s.dir = (s.dir + 1) % 4; } // 右折
    else if (action == 'L') { s.dir = (s.dir + 3) % 4; } // 左折
    else if (action == 'S') { // 交換・拾う・置く
        int board_ball = -1;
        // 足元にボールがあるか探す
        for (int i = 0; i < M; ++i) {
            if (s.b_status[i] == 0 && s.b_r[i] == s.r && s.b_c[i] == s.c) {
                board_ball = i; break;
            }
        }

        if (s.holding == -1 && board_ball != -1) {
            // 何も持っていなくて、足元にボールがある -> 拾う
            s.holding = board_ball;
            s.b_status[board_ball] = 1;
        } 
        else if (s.holding != -1 && board_ball == -1) {
            // ボールを持っていて、足元は空っぽ -> 置く
            int h = s.holding;
            s.holding = -1;
            s.b_r[h] = s.r; s.b_c[h] = s.c;
            if (s.r == basket_r[h] && s.c == basket_c[h]) {
                s.b_status[h] = 2; // カゴに入った！
                s.placed_count++;
            } else {
                s.b_status[h] = 0; // ただの床に置いた
            }
        } 
        else if (s.holding != -1 && board_ball != -1) {
            // ボールを持っていて、足元にもボールがある -> 交換する
            int h = s.holding;
            s.holding = board_ball;
            s.b_status[board_ball] = 1;

            s.b_r[h] = s.r; s.b_c[h] = s.c;
            if (s.r == basket_r[h] && s.c == basket_c[h]) {
                s.b_status[h] = 2; s.placed_count++;
            } else {
                s.b_status[h] = 0;
            }
        }
    }

    // 持っているボールの座標をロボットの座標と同期する
    if (s.holding != -1) {
        s.b_r[s.holding] = s.r; s.b_c[s.holding] = s.c;
    }
    return s;
}

// === 評価関数（盤面の良さを数値化する） ===
long long evaluate(const State& s) {
    long long score = 0;
    
    score += s.placed_count * 100000LL; // カゴに入れたら特大ボーナス
    score -= s.turn * 10LL;             // ターン経過はマイナス

    // 未回収のボールがカゴからどれくらい遠いか（遠いほどマイナス）
    long long remaining_dist = 0;
    for (int i = 0; i < M; ++i) {
        if (s.b_status[i] == 2) continue;
        remaining_dist += dist_map[s.b_r[i]][s.b_c[i]][basket_r[i]][basket_c[i]];
    }
    score -= remaining_dist * 100LL;

    // 空手なら、一番近いボールへ向かいたくなるようにインセンティブをつける
    if (s.holding == -1 && s.placed_count < M) {
        int min_d = 1e9;
        for (int i = 0; i < M; ++i) {
            if (s.b_status[i] == 0) {
                min_d = min(min_d, dist_map[s.r][s.c][s.b_r[i]][s.b_c[i]]);
            }
        }
        if (min_d != 1e9) score -= min_d * 100LL;
    }

    return score;
}

// === 枝刈りロジック（無駄な行動を除外する） ===
vector<char> get_valid_actions(const State& s) {
    vector<char> valid;
    
    if (!has_wall(s.r, s.c, s.dir)) valid.push_back('F');
    if (s.last_action != 'L') valid.push_back('R'); // 左向いてすぐ右向くのは無駄
    if (s.last_action != 'R') valid.push_back('L');
    
    // 交換(S)は、意味がある時だけ許可
    if (s.last_action != 'S') {
        bool has_ball_on_floor = false;
        for (int i = 0; i < M; ++i) {
            if (s.b_status[i] == 0 && s.b_r[i] == s.r && s.b_c[i] == s.c) {
                has_ball_on_floor = true; break;
            }
        }
        if (s.holding != -1 || has_ball_on_floor) valid.push_back('S');
    }
    return valid;
}


int main() {
    // 入出力を高速化するC++のおまじない
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    auto start_time = chrono::high_resolution_clock::now();

    if (!(cin >> N >> M >> T_limit)) return 0;

    v_walls.resize(N);
    for (int i = 0; i < N; ++i) cin >> v_walls[i];
    h_walls.resize(N - 1);
    for (int i = 0; i < N - 1; ++i) cin >> h_walls[i];

    // 初期状態のセットアップ
    State init_state;
    init_state.r = 0; init_state.c = 0; init_state.dir = 0;
    init_state.holding = -1; init_state.turn = 0;
    init_state.placed_count = 0;
    init_state.parent_idx = -1;
    init_state.last_action = ' ';

    for (int i = 0; i < M; ++i) {
        cin >> init_state.b_r[i] >> init_state.b_c[i] >> basket_r[i] >> basket_c[i];
        init_state.b_status[i] = 0;
    }
    init_state.score = evaluate(init_state);

    // 距離の事前計算（全マスから全マスへの最短距離をBFSで求める）
    for (int r1 = 0; r1 < N; ++r1) {
        for (int c1 = 0; c1 < N; ++c1) {
            for (int r2 = 0; r2 < N; ++r2) {
                for (int c2 = 0; c2 < N; ++c2) dist_map[r1][c1][r2][c2] = 1e9;
            }
            queue<pair<int, int>> q;
            q.push({r1, c1});
            dist_map[r1][c1][r1][c1] = 0;
            int dr[] = {0, 1, 0, -1};
            int dc[] = {1, 0, -1, 0};

            while (!q.empty()) {
                auto [curr_r, curr_c] = q.front();
                q.pop();
                for (int d = 0; d < 4; ++d) {
                    if (!has_wall(curr_r, curr_c, d)) {
                        int nr = curr_r + dr[d];
                        int nc = curr_c + dc[d];
                        if (dist_map[r1][c1][nr][nc] > dist_map[r1][c1][curr_r][curr_c] + 1) {
                            dist_map[r1][c1][nr][nc] = dist_map[r1][c1][curr_r][curr_c] + 1;
                            q.push({nr, nc});
                        }
                    }
                }
            }
        }
    }

    // === ビームサーチ開始 ===
    int beam_width = 600; // 1ターンに残す状態の数
    vector<vector<State>> beam(T_limit + 1);
    beam[0].push_back(init_state);

    unordered_set<uint64_t> seen_states;
    seen_states.insert(compute_hash(init_state));

    int best_turn = 0;
    int best_idx = 0;
    bool finished = false;

    for (int t = 0; t < T_limit; ++t) {
        if (beam[t].empty()) break;

        vector<State> next_states;
        next_states.reserve(beam[t].size() * 4);

        // 現在のターンのすべての状態を展開する
        for (int i = 0; i < (int)beam[t].size(); ++i) {
            const State& current = beam[t][i];

            if (current.placed_count == M) { // 全て完了した状態を発見！
                best_turn = t;
                best_idx = i;
                finished = true;
                break;
            }

            vector<char> actions = get_valid_actions(current);
            for (char a : actions) {
                State next_s = advance_state(current, a);
                
                // 重複排除（ハッシュチェック）
                uint64_t h = compute_hash(next_s);
                if (seen_states.count(h)) continue;
                seen_states.insert(h);

                next_s.parent_idx = i;
                next_s.score = evaluate(next_s);
                next_states.push_back(next_s);
            }
        }

        if (finished) break;

        // スコア順に並べ替え
        sort(next_states.begin(), next_states.end(), [](const State& a, const State& b) {
            return a.score > b.score;
        });

        // 優秀なものだけを残す（枝刈り）
        if ((int)next_states.size() > beam_width) {
            next_states.resize(beam_width);
        }
        beam[t + 1] = move(next_states);

        // 実行時間制限のチェック (1.9秒で強制終了)
        if (t % 10 == 0) {
            auto now = chrono::high_resolution_clock::now();
            double elapsed = chrono::duration_cast<chrono::milliseconds>(now - start_time).count() / 1000.0;
            if (elapsed > 1.9) break;
        }
    }

    // 途中で時間切れになった場合は、一番進んでいるものを採用
    if (!finished) {
        best_turn = 0;
        for (int t = T_limit; t >= 0; --t) {
            if (!beam[t].empty()) {
                best_turn = t; best_idx = 0; break;
            }
        }
    }

    // === 履歴の復元 ===
    // 親のインデックスをたどって、最初から最後までの操作文字列(FRLS)を作る
    string raw_actions = "";
    int curr_t = best_turn;
    int curr_idx = best_idx;

    while (curr_t > 0) {
        raw_actions += beam[curr_t][curr_idx].last_action;
        curr_idx = beam[curr_t][curr_idx].parent_idx;
        curr_t--;
    }
    // 後ろから辿ったので文字列を反転させる
    reverse(raw_actions.begin(), raw_actions.end());

    // === 簡易マクロ圧縮（事後処理） ===
    // 見つかった操作列から、一番頻出する2〜20文字のパターンを探してマクロ化する
    string best_macro = "";
    int max_saved = 0;

    for (int len = 2; len <= 20; ++len) {
        for (int i = 0; i + len <= (int)raw_actions.size(); ++i) {
            string sub = raw_actions.substr(i, len);
            int count = 0;
            int j = 0;
            while (j + len <= (int)raw_actions.size()) {
                if (raw_actions.substr(j, len) == sub) {
                    count++;
                    j += len;
                } else {
                    j++;
                }
            }
            // 圧縮効果 = 元の文字数 - (マクロ定義の長さ + 登録用の'M'2回 + 呼び出し回数)
            int saved = (count * len) - (len + 2 + count);
            if (saved > max_saved) {
                max_saved = saved;
                best_macro = sub;
            }
        }
    }

    // 実際にマクロを適用して最終的な出力文字列を作る
    string final_ans = "";
    if (max_saved > 0) {
        int i = 0;
        bool macro_registered = false;
        while (i < (int)raw_actions.size()) {
            if (i + (int)best_macro.size() <= (int)raw_actions.size() && raw_actions.substr(i, best_macro.size()) == best_macro) {
                if (!macro_registered) {
                    final_ans += "M\n"; // マクロ記録開始
                    for (char c : best_macro) { final_ans += c; final_ans += "\n"; }
                    final_ans += "M\n"; // マクロ記録終了
                    macro_registered = true;
                } else {
                    final_ans += "P\n"; // マクロ再生
                }
                i += best_macro.size();
            } else {
                final_ans += raw_actions[i];
                final_ans += "\n";
                i++;
            }
        }
    } else {
        // 圧縮効果がなければそのまま出力
        for(char c : raw_actions) {
            final_ans += c;
            final_ans += "\n";
        }
    }

    // 出力
    cout << final_ans;

    return 0;
}