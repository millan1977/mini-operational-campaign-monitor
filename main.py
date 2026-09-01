from datetime import datetime
print("Mini Operational Campaign Monitor")
dataset = [
{
"Advertiser_Name" : "Pepsico",
"Advertiser_ID" : 100002,
"Order_Name" : "15 de septiembre 2026",
"Order_ID" : 10000002,
"LineItem_Name" : "Display_TUDN_pepsico",
"LineItem_ID" : 1000000002,
"LineItem_StartDate" : "29-08-2026 00:00",
"LineItem_EndDate" : "19-09-2026 23:59",
"Contracted_Impressions" : 1000000,
"Lifetime_Impressions": 100000,
"Trafficker_Name" : "Fulanito Perez",
"Trafficker_ID" : 10001,
"Status" : "Delivering"
},
{
"Advertiser_Name" : "CocaCola",
"Advertiser_ID" : 100001,
"Order_Name" : "Fiestas Patrias 2026",
"Order_ID" : 10000001,
"LineItem_Name" : "Display_TUDN_cocacola",
"LineItem_ID" : 1000000001,
"LineItem_StartDate" : "22-08-2026 00:00",
"LineItem_EndDate" : "19-09-2026 23:59",
"Contracted_Impressions" : 1000000,
"Lifetime_Impressions": 50000,
"Trafficker_Name" : "Fulanito Perez",
"Trafficker_ID" : 10001,
"Status" : "Delivering"
}]
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
    




    
