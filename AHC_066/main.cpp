#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;

// --- 調整用パラメータ ---
const int TURN_PENALTY = 3; // 旋回ペナルティ（直進を優遇し、圧縮率を上げる）

int N, M, T_limit;
vector<string> v_walls, h_walls;
int b_r[40], b_c[40], d_r[40], d_c[40];

int dist_cost[20][20][4][20][20];
int best_end_dir[20][20][4][20][20];
string best_path_str[20][20][4][20][20];

int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};

bool has_wall(int r, int c, int dir) {
    if (dir == 0) return c + 1 >= N || v_walls[r][c] == '1';
    if (dir == 1) return r + 1 >= N || h_walls[r][c] == '1';
    if (dir == 2) return c - 1 < 0  || v_walls[r][c - 1] == '1';
    if (dir == 3) return r - 1 < 0  || h_walls[r - 1][c] == '1';
    return true;
}

struct Node {
    int r, c, d, cost;
    bool operator>(const Node& other) const { return cost > other.cost; }
};

// --- 直進優先の経路計算 ---
void precompute_paths() {
    for (int sr = 0; sr < N; ++sr) {
        for (int sc = 0; sc < N; ++sc) {
            for (int sd = 0; sd < 4; ++sd) {
                for (int i = 0; i < N; ++i)
                    for (int j = 0; j < N; ++j)
                        dist_cost[sr][sc][sd][i][j] = 1e9;
                
                int min_cost[20][20][4];
                int parent_r[20][20][4], parent_c[20][20][4], parent_d[20][20][4];
                char parent_act[20][20][4];
                for(int i=0; i<N; ++i) for(int j=0; j<N; ++j) for(int k=0; k<4; ++k) min_cost[i][j][k] = 1e9;

                priority_queue<Node, vector<Node>, greater<Node>> pq;
                pq.push({sr, sc, sd, 0});
                min_cost[sr][sc][sd] = 0;

                while (!pq.empty()) {
                    auto curr = pq.top(); pq.pop();
                    if (curr.cost > min_cost[curr.r][curr.c][curr.d]) continue;

                    if (!has_wall(curr.r, curr.c, curr.d)) {
                        int nr = curr.r + dr[curr.d];
                        int nc = curr.c + dc[curr.d];
                        if (curr.cost + 1 < min_cost[nr][nc][curr.d]) {
                            min_cost[nr][nc][curr.d] = curr.cost + 1;
                            parent_r[nr][nc][curr.d] = curr.r; parent_c[nr][nc][curr.d] = curr.c; parent_d[nr][nc][curr.d] = curr.d;
                            parent_act[nr][nc][curr.d] = 'F';
                            pq.push({nr, nc, curr.d, curr.cost + 1});
                        }
                    }
                    int rd = (curr.d + 1) % 4;
                    if (curr.cost + TURN_PENALTY < min_cost[curr.r][curr.c][rd]) {
                        min_cost[curr.r][curr.c][rd] = curr.cost + TURN_PENALTY;
                        parent_r[curr.r][curr.c][rd] = curr.r; parent_c[curr.r][curr.c][rd] = curr.c; parent_d[curr.r][curr.c][rd] = curr.d;
                        parent_act[curr.r][curr.c][rd] = 'R';
                        pq.push({curr.r, curr.c, rd, curr.cost + TURN_PENALTY});
                    }
                    int ld = (curr.d + 3) % 4;
                    if (curr.cost + TURN_PENALTY < min_cost[curr.r][curr.c][ld]) {
                        min_cost[curr.r][curr.c][ld] = curr.cost + TURN_PENALTY;
                        parent_r[curr.r][curr.c][ld] = curr.r; parent_c[curr.r][curr.c][ld] = curr.c; parent_d[curr.r][curr.c][ld] = curr.d;
                        parent_act[curr.r][curr.c][ld] = 'L';
                        pq.push({curr.r, curr.c, ld, curr.cost + TURN_PENALTY});
                    }
                }

                for (int gr = 0; gr < N; ++gr) {
                    for (int gc = 0; gc < N; ++gc) {
                        int best_d = 0;
                        for (int d = 1; d < 4; ++d) {
                            if (min_cost[gr][gc][d] < min_cost[gr][gc][best_d]) best_d = d;
                        }
                        dist_cost[sr][sc][sd][gr][gc] = min_cost[gr][gc][best_d];
                        best_end_dir[sr][sc][sd][gr][gc] = best_d;

                        string path = "";
                        int cr = gr, cc = gc, cd = best_d;
                        while (cr != sr || cc != sc || cd != sd) {
                            path += parent_act[cr][cc][cd];
                            int pr = parent_r[cr][cc][cd]; int pc = parent_c[cr][cc][cd]; int pd = parent_d[cr][cc][cd];
                            cr = pr; cc = pc; cd = pd;
                        }
                        reverse(path.begin(), path.end());
                        best_path_str[sr][sc][sd][gr][gc] = path;
                    }
                }
            }
        }
    }
}

// --- 巡回コスト計算（ジャグリング対応） ---
long long evaluate_order(const vector<int>& order, const vector<bool>& juggle) {
    long long total_cost = 0;
    int curr_r = 0, curr_c = 0, curr_d = 0;

    for (int i = 0; i < M; ) {
        if (i < M - 1 && juggle[i]) {
            int t1 = order[i];
            int t2 = order[i+1];
            // t1を拾う
            total_cost += dist_cost[curr_r][curr_c][curr_d][b_r[t1]][b_c[t1]];
            curr_d = best_end_dir[curr_r][curr_c][curr_d][b_r[t1]][b_c[t1]];
            curr_r = b_r[t1]; curr_c = b_c[t1];
            // t2の位置でスワップ
            total_cost += dist_cost[curr_r][curr_c][curr_d][b_r[t2]][b_c[t2]];
            curr_d = best_end_dir[curr_r][curr_c][curr_d][b_r[t2]][b_c[t2]];
            curr_r = b_r[t2]; curr_c = b_c[t2];
            // t2を届ける
            total_cost += dist_cost[curr_r][curr_c][curr_d][d_r[t2]][d_c[t2]];
            curr_d = best_end_dir[curr_r][curr_c][curr_d][d_r[t2]][d_c[t2]];
            curr_r = d_r[t2]; curr_c = d_c[t2];
            // t2の初期位置に戻り、t1を拾い直す
            total_cost += dist_cost[curr_r][curr_c][curr_d][b_r[t2]][b_c[t2]];
            curr_d = best_end_dir[curr_r][curr_c][curr_d][b_r[t2]][b_c[t2]];
            curr_r = b_r[t2]; curr_c = b_c[t2];
            // t1を届ける
            total_cost += dist_cost[curr_r][curr_c][curr_d][d_r[t1]][d_c[t1]];
            curr_d = best_end_dir[curr_r][curr_c][curr_d][d_r[t1]][d_c[t1]];
            curr_r = d_r[t1]; curr_c = d_c[t1];
            i += 2; // 2タスク分処理した
        } else {
            int t = order[i];
            // 通常の 拾う → 届ける
            total_cost += dist_cost[curr_r][curr_c][curr_d][b_r[t]][b_c[t]];
            curr_d = best_end_dir[curr_r][curr_c][curr_d][b_r[t]][b_c[t]];
            curr_r = b_r[t]; curr_c = b_c[t];

            total_cost += dist_cost[curr_r][curr_c][curr_d][d_r[t]][d_c[t]];
            curr_d = best_end_dir[curr_r][curr_c][curr_d][d_r[t]][d_c[t]];
            curr_r = d_r[t]; curr_c = d_c[t];
            i += 1;
        }
    }
    return total_cost;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    auto start_time = chrono::high_resolution_clock::now();

    if (!(cin >> N >> M >> T_limit)) return 0;
    v_walls.resize(N); for (int i = 0; i < N; ++i) cin >> v_walls[i];
    h_walls.resize(N - 1); for (int i = 0; i < N - 1; ++i) cin >> h_walls[i];
    for (int i = 0; i < M; ++i) cin >> b_r[i] >> b_c[i] >> d_r[i] >> d_c[i];

    precompute_paths();

    mt19937 rng(42);
    vector<int> best_order(M);
    vector<bool> best_juggle(M, false);
    for (int i = 0; i < M; ++i) best_order[i] = i;
    
    long long best_cost = evaluate_order(best_order, best_juggle);
    
    vector<int> curr_order = best_order;
    vector<bool> curr_juggle = best_juggle;
    long long curr_cost = best_cost;

    double time_limit = 1.85;
    double start_temp = 50.0;
    double end_temp = 0.1;
    int iter = 0;

    // --- 焼きなまし法 ---
    while (true) {
        if ((iter & 255) == 0) { 
            auto now = chrono::high_resolution_clock::now();
            double elapsed = chrono::duration_cast<chrono::milliseconds>(now - start_time).count() / 1000.0;
            if (elapsed > time_limit) break;
            
            double temp = start_temp + (end_temp - start_temp) * (elapsed / time_limit);
            
            vector<int> next_order = curr_order;
            vector<bool> next_juggle = curr_juggle;
            
            int r = rng() % 100;
            if (r < 40) { // 2-opt
                int l = rng() % M; int right = rng() % M;
                if (l > right) swap(l, right);
                reverse(next_order.begin() + l, next_order.begin() + right + 1);
            } else if (r < 80) { // Insert
                int u = rng() % M; int v = rng() % M;
                if (u != v) {
                    int val = next_order[u];
                    next_order.erase(next_order.begin() + u);
                    next_order.insert(next_order.begin() + v, val);
                }
            } else { // Juggle Toggle
                int idx = rng() % (M - 1);
                next_juggle[idx] = !next_juggle[idx];
                // 重複コンボを防ぐため前後のフラグを折る
                if (next_juggle[idx]) {
                    if (idx > 0) next_juggle[idx-1] = false;
                    if (idx < M-2) next_juggle[idx+1] = false;
                }
            }

            long long new_cost = evaluate_order(next_order, next_juggle);

            if (new_cost <= curr_cost || exp((curr_cost - new_cost) / temp) > (double)rng() / rng.max()) {
                curr_cost = new_cost;
                curr_order = next_order;
                curr_juggle = next_juggle;
                if (curr_cost < best_cost) {
                    best_cost = curr_cost;
                    best_order = curr_order;
                    best_juggle = curr_juggle;
                }
            }
        }
        iter++;
    }

    // --- 生の操作文字列(改行なし)の生成 ---
    string raw_actions = "";
    int curr_r = 0, curr_c = 0, curr_d = 0;

    for (int i = 0; i < M; ) {
        if (i < M - 1 && best_juggle[i]) {
            int t1 = best_order[i]; int t2 = best_order[i+1];
            raw_actions += best_path_str[curr_r][curr_c][curr_d][b_r[t1]][b_c[t1]]; raw_actions += "S";
            curr_d = best_end_dir[curr_r][curr_c][curr_d][b_r[t1]][b_c[t1]]; curr_r = b_r[t1]; curr_c = b_c[t1];
            
            raw_actions += best_path_str[curr_r][curr_c][curr_d][b_r[t2]][b_c[t2]]; raw_actions += "S";
            curr_d = best_end_dir[curr_r][curr_c][curr_d][b_r[t2]][b_c[t2]]; curr_r = b_r[t2]; curr_c = b_c[t2];
            
            raw_actions += best_path_str[curr_r][curr_c][curr_d][d_r[t2]][d_c[t2]]; raw_actions += "S";
            curr_d = best_end_dir[curr_r][curr_c][curr_d][d_r[t2]][d_c[t2]]; curr_r = d_r[t2]; curr_c = d_c[t2];
            
            raw_actions += best_path_str[curr_r][curr_c][curr_d][b_r[t2]][b_c[t2]]; raw_actions += "S";
            curr_d = best_end_dir[curr_r][curr_c][curr_d][b_r[t2]][b_c[t2]]; curr_r = b_r[t2]; curr_c = b_c[t2];
            
            raw_actions += best_path_str[curr_r][curr_c][curr_d][d_r[t1]][d_c[t1]]; raw_actions += "S";
            curr_d = best_end_dir[curr_r][curr_c][curr_d][d_r[t1]][d_c[t1]]; curr_r = d_r[t1]; curr_c = d_c[t1];
            i += 2;
        } else {
            int t = best_order[i];
            raw_actions += best_path_str[curr_r][curr_c][curr_d][b_r[t]][b_c[t]]; raw_actions += "S";
            curr_d = best_end_dir[curr_r][curr_c][curr_d][b_r[t]][b_c[t]]; curr_r = b_r[t]; curr_c = b_c[t];
            
            raw_actions += best_path_str[curr_r][curr_c][curr_d][d_r[t]][d_c[t]]; raw_actions += "S";
            curr_d = best_end_dir[curr_r][curr_c][curr_d][d_r[t]][d_c[t]]; curr_r = d_r[t]; curr_c = d_c[t];
            i += 1;
        }
    }

    // --- 安全なガチ文法圧縮（改行付与） ---
    string final_ans = "";
    int ptr = 0;
    int window_size = 250;

    while (ptr < (int)raw_actions.size()) {
        int current_window = min(window_size, (int)raw_actions.size() - ptr);
        string window_str = raw_actions.substr(ptr, current_window);
        
        string best_macro = "";
        int max_saved = 0;
        
        for (int len = 2; len <= 30; ++len) {
            for (int start = 0; start + len <= (int)window_str.size(); ++start) {
                string sub = window_str.substr(start, len);
                int count = 0;
                for (int j = start; j + len <= (int)window_str.size(); ) {
                    if (window_str.substr(j, len) == sub) {
                        count++; j += len;
                    } else {
                        j++;
                    }
                }
                int saved = (count * len) - (len + 2 + count);
                if (saved > max_saved) {
                    max_saved = saved; best_macro = sub;
                }
            }
        }
        
        if (max_saved > 0) {
            bool first_occurrence = true;
            int end_idx = ptr + current_window;
            
            while (ptr < end_idx) {
                if (ptr + best_macro.size() <= raw_actions.size() && 
                    raw_actions.substr(ptr, best_macro.size()) == best_macro) {
                    
                    if (first_occurrence) {
                        // 1回目は「記録しながら実行」
                        final_ans += "M\n";
                        for(char c : best_macro) { final_ans += c; final_ans += "\n"; }
                        final_ans += "M\n";
                        first_occurrence = false;
                    } else {
                        // 2回目以降は「再生(P)のみ」
                        final_ans += "P\n";
                    }
                    ptr += best_macro.size();
                } else {
                    final_ans += raw_actions[ptr]; final_ans += "\n";
                    ptr++;
                }
            }
        } else {
            final_ans += raw_actions[ptr]; final_ans += "\n";
            ptr++;
        }
    }

    cout << final_ans;
    return 0;
}