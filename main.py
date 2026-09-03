import json
from pathlib import Path
from datetime import datetime
from metrics import calcular_dias_totales, calcular_dias_transcurridos, calcular_delivery_ratio, calcular_time_ratio, calcular_osi

base_path = Path(__file__).parent
json_file = "line_items.json"
json_path = base_path / json_file
with open(json_path, "r") as file:
    dataset = json.load(file)

print("Mini Operational Campaign Monitor")

today = datetime.now()

for li in dataset:
    start_date = datetime.strptime(li["LineItem_StartDate"], "%d-%m-%Y %H:%M")
    end_date = datetime.strptime(li["LineItem_EndDate"], "%d-%m-%Y %H:%M")
    delivery_ratio = calcular_delivery_ratio(li["Lifetime_Impressions"], li["Contracted_Impressions"])
    dias_totales = calcular_dias_totales(start_date, end_date)
    elapsed_days = calcular_dias_transcurridos(today, start_date)
    time_ratio = calcular_time_ratio(elapsed_days, dias_totales)
    osi = calcular_osi(delivery_ratio, time_ratio)
    if osi is None:
        print(f"El OSI para la linea {li['LineItem_Name']} es N/A")
    else:
        print(f"El OSI para la linea {li['LineItem_Name']} es {osi:.2%}")
