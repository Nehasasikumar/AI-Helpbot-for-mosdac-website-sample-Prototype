import json
import pandas as pd
import os

def convert_json_to_excel(json_path, excel_path):
    if not os.path.exists(json_path):
        print(f"❌ JSON file not found: {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    for entry in data:
        rows.append({
            "URL": entry.get("url", ""),
            "Text": entry.get("text", "")[:500],  # limit text size for Excel preview
            "Images": ", ".join(entry.get("images", [])),
            "PDFs": ", ".join(entry.get("pdfs", [])),
        })

    df = pd.DataFrame(rows)
    df.to_excel(excel_path, index=False)
    print(f"Excel file saved to {excel_path}")

if __name__ == "__main__":
    convert_json_to_excel("data/mosdac_missions.json", "data/mosdac_missions.xlsx")
