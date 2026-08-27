# AtCoder Python template

## 公式サンプルの取得

コンテストIDを指定すると、A〜Gの `test/` に公式サンプルを取得します。

```sh
python download_samples.py abc467
```

特定の問題だけ取得することもできます。

```sh
python download_samples.py abc467 --labels A B C
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
`download_samples.py` を実行すると、各問題の入力例1が自動的に入ります。

```sh
python A/main.py < A/input.txt
```

`input.txt` はGitの管理対象外なので、その後は自由に書き換えられます。
再度 `download_samples.py` を実行すると、入力例1の内容に戻ります。
