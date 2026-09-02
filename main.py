import json
from pathlib import Path
from datetime import datetime

base_path = Path(__file__).parent
json_path = base_path / "line_items.json"
with open(json_path, "r") as file:
    dataset = json.load(file)

print("Mini Operational Campaign Monitor")
today = datetime.now()

def calcular_dias_totales(start_date, end_date):
    dias_totales = (end_date - start_date).days + 1
    return dias_totales
def calcular_dias_transcurridos(today, start_date):
    elapsed_days = (today - start_date).days
    return elapsed_days
def calcular_delivery_ratio(lifetime_impressions, contracted_impressions):
    delivery_ratio = lifetime_impressions / contracted_impressions
    return delivery_ratio 
def calcular_time_ratio(elapsed_days, dias_totales):
    time_ratio = elapsed_days / dias_totales
    return time_ratio
def calcular_osi(delivery_ratio, time_ratio):
    if time_ratio == 0:
        osi = None
    else:
        osi = delivery_ratio / time_ratio
    return osi

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
