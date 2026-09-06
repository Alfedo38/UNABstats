import csv
import json

# Abrir el archivo CSV
with open("NBA.csv", "r", encoding="utf-8") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    datos = list(lector)

# Guardar como JSON
with open("data/nba.json", "w", encoding="utf-8") as archivo_json:
    json.dump(datos, archivo_json, indent=4, ensure_ascii=False)

print("✅ Conversión completa: data/nba.json creado")