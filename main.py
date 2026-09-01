import json
from pathlib import Path
from datetime import datetime

base_path = Path(__file__).parent
json_path = base_path / "line_items.json"

with open(json_path, "r") as file:
    dataset = json.load(file)
print("Mini Operational Campaign Monitor")
today = datetime.now()
for li in dataset:
    start_date = datetime.strptime(li["LineItem_StartDate"],"%d-%m-%Y %H:%M")
    end_date = datetime.strptime(li["LineItem_EndDate"],"%d-%m-%Y %H:%M")
    dias_totales = (end_date - start_date).days + 1
    elapsed_days = (today - start_date).days    
    if elapsed_days == 0:
        osi = None
    else:
        osi = (li["Lifetime_Impressions"] / li["Contracted_Impressions"]) / (elapsed_days / dias_totales)
    print(f"El line item {li['LineItem_Name']} tiene {dias_totales} dias en total, de los cuales han transcurrido ya {elapsed_days} dias.")
    if osi is None:
        print(f"No podemos calcular el OSI")
    else:
        print(f"El OSI de este line item es {osi:.2%}")
    