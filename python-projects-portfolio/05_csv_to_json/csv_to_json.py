import csv, json, sys

def convert(csv_path, json_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
