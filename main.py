from metrics import enriquecer_dataset_metricas
from output import escribir_csv
from api_client import adaptar_dataset_api_sample, obtener_todas_las_paginas, extraer_datos_resultado_api
from datetime import datetime
import os
from dotenv import load_dotenv
import logging
import csv
from database import insertar_snapshots

logging.basicConfig(level=logging.INFO)
load_dotenv()

token = os.getenv("REQRES_API_KEY")

url = "https://reqres.in/api/collections/line_items/records?"
params={
    "project_id" : 49465
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": token,
    "X-Reqres-Env": "prod"
}
timeout = 5

dataset = obtener_todas_las_paginas(
    url, 
    params, 
    headers, 
    timeout
)
data = extraer_datos_resultado_api(dataset)
dataset_normalizado = adaptar_dataset_api_sample(data)

logging.info("Mini Operational Campaign Monitor")

today = datetime.now()
snapshot_date = today.date()

dataset_enriquecido = enriquecer_dataset_metricas(dataset_normalizado, today)

# creamos la fecha de ejecucion snapshot

for registro in dataset_enriquecido:
    registro["snapshot_date"] = snapshot_date

# Lo vamos a meter en un CSV
ruta_archivo = "campaign_monitor.csv"

escribir_csv(dataset_enriquecido, ruta_archivo)

# comprobar si hay ids duplicados
# conteo_ids = {}

# for registro in dataset_enriquecido:
#     line_item_id = registro["LineItem_ID"]

#     if line_item_id in conteo_ids:
#         conteo_ids[line_item_id] += 1
#     else:
#         conteo_ids[line_item_id] = 1

# for line_item_id, conteo in conteo_ids.items():
#     if conteo > 1:
#         print(line_item_id, conteo)
        
insertar_snapshots(dataset_enriquecido)

