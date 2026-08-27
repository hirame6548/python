# AtCoder Python template

## 公式サンプルの取得

コンテストIDを指定すると、A〜Gの `test/` に公式サンプルを取得します。

```sh
python download_samples.py abc(n)
```

特定の問題だけ取得することもできます。

```sh
python download_samples.py abc(n) --labels A B C
```

## 自作テストの追加

同じ名前の `.in` と `.out` を各問題の `test/` に追加します。

```text
A/test/custom-boundary.in
A/test/custom-boundary.out
```

`pytest` を実行すると、公式サンプルと自作テストの両方が自動的に検出されます。
