import json

json_path = "document (2).json"

with open(json_path, "r", encoding="utf-8") as f:
    doc_data = json.load(f)

# 全文テキストを取得
full_text = doc_data.get("text", "")

paragraphs_list = []

# ページごとに処理
for page in doc_data.get("pages", []):
    for paragraph in page.get("paragraphs", []):
        # 段落のテキスト範囲（textAnchor）を取得
        text_anchor = paragraph.get("layout", {}).get("textAnchor", {})
        text_segments = text_anchor.get("textSegments", [])
        
        if not text_segments:
            continue
            
        paragraph_text = ""
        for segment in text_segments:
            # 開始位置と終了位置を取得（入っていない場合はデフォルト値）
            start_index = int(segment.get("startIndex", 0))
            end_index = int(segment.get("endIndex", 0))
            
            # 全文から該当部分をスライスして結合
            paragraph_text += full_text[start_index:end_index]
        
        # 末尾の余分な改行などをトリミングしてリストに追加
        cleaned_text = paragraph_text.strip()
        if cleaned_text:
            paragraphs_list.append(cleaned_text)

# --- 確認用：分割された段落を表示 ---
for i, p_text in enumerate(paragraphs_list, 1):
    #print(f"【段落 {i}】")
    print(p_text)
    print("\n")