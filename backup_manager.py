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

def verificar_restauracio(carpeta_desti): #FJ-21
    if os.path.exists(carpeta_desti):
        fitxers = os.listdir(carpeta_desti)
        if len(fitxers) > 0: #aqui se comprueban posibles fallos, como si la carpeta puede estar vacia o no existe
            print(f"Verificació completada, s'han trobat {len(fitxers)} fitxers.")
            return True
        else:
            print("Verificació fallida, la carpeta està buida.")
            return False
    else:
        print("Verificació fallida, la carpeta no existeix.")
        return False