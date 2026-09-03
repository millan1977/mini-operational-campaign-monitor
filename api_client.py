import requests

def obtener_datos_api(url, params, headers, timeout):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()

        # print(response.headers)
        print(response.url)
        print(response)
        print(type(response))
        print(response.status_code)
        print(response.headers["Content-Type"])
        print(type(response.headers))
        print(response.request.headers)

        data = response.json()
        return data
    except requests.exceptions.Timeout:
            print("La petición superó el tiempo máximo de espera")
    except requests.exceptions.ConnectionError:
        print("Error de conexion")
    except requests.exceptions.HTTPError:
        print(f"Error HTTP: {response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("La respuesta no contiene JSON válido")

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
    
