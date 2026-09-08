from metrics import enriquecer_dataset_metricas
from api_client import adaptar_dataset_api_sample, obtener_todas_las_paginas, extraer_datos_resultado_api
from datetime import datetime
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()

token = os.getenv("REQRES_API_KEY")

url = "https://reqres.in/api/collections/line_items/records?"
params={
    "project_id" : 49465
}
headers = headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": token,
    "X-Reqres-Env": "prod"
}
timeout = 5

dataset = dataset = obtener_todas_las_paginas(
    url, 
    params, 
    headers, 
    timeout
)
data = extraer_datos_resultado_api(dataset)
dataset_normalizado = adaptar_dataset_api_sample(data)

logging.info("Mini Operational Campaign Monitor")

today = datetime.now()

dataset_enriquecido = enriquecer_dataset_metricas(dataset_normalizado, today)
