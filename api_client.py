import requests
from datetime import datetime
import logging

def obtener_datos_api(url, params, headers, timeout):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()

        logging.debug("URL solicitada: %s", response.url)

        data = response.json()
        return data
    except requests.exceptions.Timeout:
        logging.error("La petición superó el tiempo máximo de espera")
    except requests.exceptions.ConnectionError:
        logging.error("Error de conexion")
    except requests.exceptions.HTTPError:
        logging.error(f"Error HTTP: {response.status_code}")
    except requests.exceptions.JSONDecodeError:
        logging.error("La respuesta no contiene JSON válido")

def obtener_todas_las_paginas(url, params, headers, timeout):
    params_paginacion = params.copy()
    resultado = obtener_datos_api(url, params_paginacion, headers, timeout)
    total_paginas = resultado["meta"]["pages"]
    logging.info("El total de paginas es de %s", total_paginas)
    todos_los_registros = []
    todos_los_registros.extend(resultado["data"])
    for pagina in range(2, total_paginas + 1):
        params_paginacion["page"] = pagina
        resultado = obtener_datos_api(url, params_paginacion, headers, timeout)
        todos_los_registros.extend(resultado["data"])
    return todos_los_registros

def extraer_datos_resultado_api(dataset):
    data = []
    for registro in dataset:
        data.append(registro["data"])
    return data

def crear_datos_api(url, headers, body, timeout):
    try:
        response = requests.post(
            url,
            headers = headers,
            json = body, 
            timeout = timeout
            )
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        logging.error("La petición superó el tiempo máximo de espera")
    except requests.exceptions.ConnectionError:
        logging.error("Error de conexion")
    except requests.exceptions.HTTPError:
        logging.error(f"Error HTTP: {response.status_code}")
    except requests.exceptions.JSONDecodeError:
        logging.error("La respuesta no contiene JSON válido")

def adaptar_line_item_api_sample(api_line_item):
     line_item = {
        "Advertiser_ID" : api_line_item["advertiserId"],
        "Advertiser_Name" : api_line_item["advertiserName"],
        "Order_Name" : api_line_item["orderName"],
        "Order_ID" : api_line_item["orderId"],
        "LineItem_Name" : api_line_item["name"],
        "LineItem_ID" : api_line_item["id"],
        "LineItem_StartDate" : api_line_item["startDate"],
        "LineItem_EndDate" : api_line_item["endDate"], 
        "Contracted_Impressions" : api_line_item["contractedImpressions"], 
        "Lifetime_Impressions" : api_line_item["lifetimeImpressions"],
        "Trafficker_Name" : api_line_item["traffickerName"],
        "Trafficker_ID" : api_line_item["traffickerId"],
        "Status" : api_line_item["status"],
    }
     return line_item

def adaptar_dataset_api_sample(dataset):
    dataset_normalizado = []
    for li in dataset:
        li_norm = adaptar_line_item_api_sample(li)
        dataset_normalizado.append(li_norm)
    return dataset_normalizado


