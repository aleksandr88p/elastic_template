import os
import json

# Пути к файлам
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(BASE_DIR, 'data', 'all_lawsOLD.ndjson')
OUTPUT_PATH = os.path.join(BASE_DIR, 'data', 'all_laws.ndjson')

def normalize_ndjson(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if not line.strip():
                continue
            doc = json.loads(line)
            # Если есть "text", переименовываем в "texto"
            if "text" in doc:
                doc["texto"] = doc.pop("text")
            outfile.write(json.dumps(doc, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    print(f"Нормализация {INPUT_PATH} -> {OUTPUT_PATH}")
    normalize_ndjson(INPUT_PATH, OUTPUT_PATH)
    print("Готово! Все поля 'text' переименованы в 'texto'.")