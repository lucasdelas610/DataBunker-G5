# Creacion i restauracion de copias

import zipfile
import os

def restaurar_copia(zip_arxiu, carpeta_desti): #FJ-20
    if os.path.exists(zip_arxiu): #se comprueba si existe el archivo
        arxiu= zipfile.ZipFile(zip_arxiu, 'r')
        arxiu.extractall(carpeta_desti) #se extrae el contenido del archivo
        arxiu.close()
        print(f"Restauració completada a {carpeta_desti}")
    else:
        print(f"Error, no s'ha trobat l'arxiu '{zip_arxiu}'") #si no existe el archivo, printea error

