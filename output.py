import csv

def escribir_csv(dataset_enriquecido, ruta_archivo):
    
    columnas = dataset_enriquecido[0].keys()

    with open(
        ruta_archivo,
        "w",
        newline = "",
        encoding = "utf-8"
    ) as archivo:

        writer = csv.DictWriter(
            archivo,
            fieldnames = columnas
        )
        writer.writeheader()
        writer.writerows(dataset_enriquecido)