# Creacion i restauracion de copias

import zipfile
import os
import crypto_utils


def comprimir_carpeta(carpeta, zip_final):
    if os.path.exists(carpeta) == False:
        print("Error: La carpeta no existe.")
        return False 
    zip_1 = zipfile.ZipFile(zip_final, 'w')
    for archivo in os.listdir(carpeta):
        ruta_completa = carpeta + "/" + archivo
        if os.path.isfile(ruta_completa):# comprueba que es un archivo y no falle
            zip_1.write(ruta_completa, arcname=archivo)
    zip_1.close()
    
    print("Carpeta comprimida correctamente en: " + zip_final)
    return True 


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


def restaurar_copia(zip_arxiu, carpeta_desti):# Validar formato ZIP
    if zipfile.is_zipfile(zip_arxiu) == False:
        print("Error: El archivo no es un ZIP válido o está roto.")
        with open("historial.txt", "a") as f:
            f.write("ERROR: Intento de restaurar un zip corrupto.")
        return

    arxiu = zipfile.ZipFile(zip_arxiu, 'r')
    arxiu.extractall(carpeta_desti) 
    arxiu.close()
    
    # Llamamos a la función para comprobar que todo esta bien
    verificar_restauracio(carpeta_desti)
    
    print(f"Restauració completada a {carpeta_desti}")
    with open("historial.txt", "a") as f:
        f.write("EXITO: Restauracion completada.")