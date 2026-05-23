import json
import fitz  # PyMuPDF

# ファイルパスの指定
pdf_path = "sample.pdf"
json_path = "document (2).json"
output_pdf_path = "sample_with_boxes.pdf"

# JSONの読み込み
with open(json_path, "r", encoding="utf-8") as f:
    doc_data = json.load(f)

# PDFを開く
pdf_doc = fitz.open(pdf_path)

# ページごとに処理ループ
for page_data in doc_data.get("pages", []):
    page_index = int(page_data.get("pageNumber", 1)) - 1
    
    if page_index >= len(pdf_doc):
        continue

    pdf_page = pdf_doc[page_index]
    
    width = pdf_page.rect.width
    height = pdf_page.rect.height

    for paragraph in page_data.get("paragraphs", []):
        vertices = paragraph.get("layout", {}).get("boundingPoly", {}).get("normalizedVertices", [])
        if not vertices:
            continue

        points = []
        for v in vertices:
            x = v.get("x", 0.0) * width
            y = v.get("y", 0.0) * height
            points.append(fitz.Point(x, y))

        if len(points) == 4:
            # 【修正箇所】Document AI(0:左上, 1:右上, 2:右下, 3:左下) 
            # から PyMuPDF(ul, ur, ll, lr) の順に適合するよう 2 と 3 のインデックスを入れ替え
            quad = fitz.Quad(points[0], points[1], points[3], points[2])
            pdf_page.draw_quad(quad, color=(1, 0, 0), width=1.5)
        elif len(points) > 0:
            pdf_page.draw_polygon(points, color=(1, 0, 0), width=1.5)

# 保存
pdf_doc.save(output_pdf_path)
print(f"完了: {output_pdf_path} を生成しました。")