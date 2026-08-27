# AtCoder Python tools

## コンテスト開始前の準備

リポジトリのルートでコンテストIDを指定します。この処理では通信しません。

```sh
python new.py abc468
```

`ABC/468`にA〜Gの問題フォルダ、テスト設定、ダウンロード用の`dl.py`が
作成されます。`ABC 468`のように2引数で指定することもできます。

主な初期構成は次のとおりです。

| 種類 | 作成する問題フォルダ | 指定例 |
| --- | --- | --- |
| ABC | A〜G | `abc468` |
| ARC / AGC | A〜F | `arc219` |
| AHC | A | `ahc070` |
| AWC | A〜E | `awc0141` |
| ADT EASY | A〜E | `adt_easy_20260827_1` |
| ADT ALL | A〜I | `adt_all_20260827_1` |

標準と異なる場合は問題ラベルを明示できます。

```sh
python new.py awc0141 --labels A B C D E
```

## 問題文と公式サンプルの取得

作成されたコンテストフォルダをVS Codeで開いて待機し、開始後に実行します。

```sh
python dl.py
```

公式のタスク一覧を読み取り、各問題フォルダに日本語の公式問題文を
`problem.md`として保存し、`test/`に公式サンプルを取得します。
問題文中の数式と入力形式はLaTeXとして保存し、実際の入出力例はコピーしやすい
コードブロックとして保存します。

特定の問題だけ取得することもできます。

```sh
python dl.py --labels A B C
```

取得済みの `problem.md` と公式サンプルは上書きしません。片方だけ存在する場合は、
不足している方だけを取得します。

問題文だけ再取得して上書きする場合は、次のように実行します。

```sh
python dl.py --refresh-statements
```

## 自作テストの追加

同じ名前の `.in` と `.out` を各問題の `test/` に追加します。

```text
A/test/custom-boundary.in
A/test/custom-boundary.out
```

`pytest` を実行すると、公式サンプルと自作テストの両方が自動的に検出されます。

## 手動デバッグ

各問題の `input.txt` は、途中の `print()` などを確認するためのスクラッチ入力です。
`dl.py` を実行すると、各問題の入力例1が自動的に入ります。

```sh
python A/main.py < A/input.txt
```

`input.txt`はGitの管理対象外なので、その後は自由に書き換えられます。
再度 `dl.py` を実行すると、入力例1の内容に戻ります。
