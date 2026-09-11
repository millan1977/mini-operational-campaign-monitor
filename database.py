import os
import psycopg
from dotenv import load_dotenv
import logging

load_dotenv()

# funcion de conexion
def conexion_db():
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="campaign_monitor",
        user="postgres",
        password=postgres_password
    )
# funcion de insercion
def insertar_snapshots(dataset_enriquecido):
    from datetime import datetime
    with conexion_db() as conexion:
        with conexion.cursor() as cursor:
            insertados = 0
            omitidos = 0
            for registro in dataset_enriquecido:
                start_date = datetime.strptime(
                    registro["LineItem_StartDate"],
                    "%d-%m-%Y %H:%M"
                )
                end_date = datetime.strptime(
                    registro["LineItem_EndDate"],
                    "%d-%m-%Y %H:%M"
                )
                cursor.execute(
                    """
                    INSERT INTO line_item_snapshots (
                        line_item_id,
                        snapshot_date,
                        advertiser_id,
                        advertiser_name,
                        line_item_start_date,
                        contracted_impressions,
                        order_name,
                        order_id,
                        line_item_name,
                        line_item_end_date,
                        lifetime_impressions,
                        trafficker_name,
                        trafficker_id,
                        status,
                        total_days,
                        elapsed_days,
                        delivery_ratio,
                        time_ratio,
                        osi
                    )
                    VALUES (
                        %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s, %s, %s
                    )
                    ON CONFLICT (line_item_id, snapshot_date)
                    DO NOTHING;
                    """,
                    (
                        registro["LineItem_ID"],
                        registro["snapshot_date"],
                        registro["Advertiser_ID"],
                        registro["Advertiser_Name"],
                        start_date,
                        registro["Contracted_Impressions"],
                        registro["Order_Name"],
                        registro["Order_ID"],
                        registro["LineItem_Name"],
                        end_date,
                        registro["Lifetime_Impressions"],
                        registro["Trafficker_Name"],
                        registro["Trafficker_ID"],
                        registro["Status"],
                        registro["total_days"],
                        registro["elapsed_days"],
                        registro["delivery_ratio"],
                        registro["time_ratio"],
                        registro["osi"]
                    )
                )

                if cursor.rowcount == 1:
                    insertados += 1
                else:
                    omitidos += 1
        logging.info(
        "PostgreSQL: %s snapshots insertados, %s omitidos",
        insertados,
        omitidos
        )