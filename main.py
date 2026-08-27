from datetime import datetime
print("Mini Operational Campaign Monitor")
Line_Item = {
    "Advertiser_Name" : "CocaCola",
    "Advertiser_ID" : 100001,
    "Order_Name" : "Fiestas Patrias 2026",
    "Order_ID" : 10000001,
    "LineItem_Name" : "Display_TUDN",
    "LineItem_ID" : 1000000001,
    "LineItem_StartDate" : "22-08-2026 00:00",
    "LineItem_EndDate" : "19-09-2026 23:59",
    "Contracted_Impressions" : 1000000,
    "Lifetime_Impressions": 50000,
    "Trafficker_Name" : "Fulanito Perez",
    "Trafficker_ID" : 10001,
    "Status" : "Delivering"
}
start_date = datetime.strptime(Line_Item["LineItem_StartDate"],"%d-%m-%Y %H:%M")
end_date = datetime.strptime(Line_Item["LineItem_EndDate"],"%d-%m-%Y %H:%M")
dias_totales = (end_date - start_date).days +1
print(f"{dias_totales} dias totales")
print(type(dias_totales))
