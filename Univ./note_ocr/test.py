import json

# ダウンロードしたJSONファイルのパスを指定
json_file_path = "document (2).json"

with open(json_file_path, "r", encoding="utf-8") as f:
    doc_data = json.load(f)

# 抽出された全文テキストを取得
extracted_text = doc_data.get("text", "")

if extracted_text:
    print("✅ 解析成功！抽出されたテキスト:\n")
    print("-" * 40)
    print(extracted_text)
    print("-" * 40)
else:
    print("⚠️ 処理は完了していますが、テキストが抽出されていません（白紙の可能性など）。")