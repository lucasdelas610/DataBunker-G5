# Punto de entrada del programa
import os
import zipfile

def comprimir_carpeta(carpeta, zip_final):
    if os.path.exists(carpeta) == False:
        print("Error: La carpeta que quieres comprimir no existe.")
        return
    zip_1 = zipfile.ZipFile(zip_final, 'w')
    for archivo in os.listdir(carpeta):
        zip_1.write(carpeta + "/" + archivo)
    zip_1.close()
#Si le das a iniciar se guarda ya la copia .zip FJ 19