from datetime import datetime

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

def enriquecer_dataset_metricas(dataset, today):
    dataset_enriquecido = []
    for registro in dataset:
        registro_enriquecido = registro.copy()
        start_date = datetime.strptime(registro_enriquecido["LineItem_StartDate"],"%d-%m-%Y %H:%M")
        end_date = datetime.strptime(registro_enriquecido["LineItem_EndDate"], "%d-%m-%Y %H:%M")
        lifetime_impressions = registro_enriquecido["Lifetime_Impressions"]
        contracted_impressions = registro_enriquecido["Contracted_Impressions"]
        
        dias_totales = calcular_dias_totales(start_date, end_date)
        dias_transcurridos = calcular_dias_transcurridos(today,start_date)
        delivery_ratio = calcular_delivery_ratio(lifetime_impressions, contracted_impressions)
        time_ratio = calcular_time_ratio(dias_transcurridos, dias_totales)
        osi = calcular_osi(delivery_ratio, time_ratio)

        registro_enriquecido["total_days"] = dias_totales
        registro_enriquecido["elapsed_days"] = dias_transcurridos
        registro_enriquecido["delivery_ratio"] = delivery_ratio
        registro_enriquecido["time_ratio"] = time_ratio
        registro_enriquecido["osi"] = osi

        dataset_enriquecido.append(registro_enriquecido)

    return dataset_enriquecido