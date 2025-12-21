# Punto de entrada del programa
import os
import zipfile

def comprimir_carpeta(carpeta, zip_final):
    zip_1 = zipfile.ZipFile(zip_final, 'w')
    for archivo in os.listdir(carpeta):
        zip_1.write(carpeta + "/" + archivo)
    zip_1.close()
