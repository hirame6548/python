# AtCoder Python template

## 問題文と公式サンプルの取得

コンテストのルートフォルダで実行すると、フォルダ名からコンテストIDを判定し、
A〜Gの各フォルダに日本語の公式問題文を `problem.md` として保存し、
`test/` に公式サンプルを取得します。

```sh
python dl.py
```

自動判定できないフォルダ名では、コンテストIDを指定できます。

```sh
python dl.py abc467
```

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

`input.txt` はGitの管理対象外なので、その後は自由に書き換えられます。
再度 `dl.py` を実行すると、入力例1の内容に戻ります。
