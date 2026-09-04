from metrics import calcular_dias_totales, calcular_dias_transcurridos, calcular_delivery_ratio, calcular_time_ratio, calcular_osi
from api_client import adaptar_dataset_api_sample, obtener_datos_api
from datetime import datetime

url = "http://localhost:8000/api_line_items_sample.json"
params={}
headers = {
    "Accept":"application/json"
}
timeout = 5

dataset = obtener_datos_api(url, params, headers, timeout)

dataset_normalizado = adaptar_dataset_api_sample(dataset)

print("Mini Operational Campaign Monitor")

today = datetime.now()

for li in dataset_normalizado:
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
