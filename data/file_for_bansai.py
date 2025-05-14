import json

# Имя файла с вашими данными
input_file = "all_laws.ndjson"
# Имя файла для выходных данных
output_file = "bulk_data.ndjson"
# Имя индекса в Elasticsearch
index_name = "legal_documents"

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    line_number = 1
    for line in f_in:
        try:
            # Строка метаданных для Bulk API Elasticsearch
            action = {"index": {"_index": index_name, "_id": line_number}}
            f_out.write(json.dumps(action) + "\n")
            
            # Сама строка с вашими данными (со всеми вашими метаданными)
            f_out.write(line)
            
            line_number += 1
        except Exception as e:
            print(f"Ошибка при обработке строки {line_number}: {str(e)}")

print(f"Преобразование завершено. Обработано {line_number-1} документов.")

