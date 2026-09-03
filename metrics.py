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