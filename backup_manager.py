# Creacion y restauracion de copias

import zipfile
import os



def comprimir_carpeta(carpeta, zip_final): # Validar que existen los archivos
    if os.path.exists(carpeta) == False:
        print(" La carpeta no existe.")
        with open("historial.txt", "a") as f:
            f.write(" La carpeta a comprimir no existe\n")
        return False
    
    # Validar carpeta vacía
    contenido = os.listdir(carpeta)
    if len(contenido) == 0:
        print("La carpeta está vacía")
        with open("historial.txt", "a") as f:
            f.write("Intento de comprimir carpeta vacia\n")
        return False

    if os.path.exists(zip_final) == True: # Evitar sobrescribir backups
        print(f"Ya existe un archivo llamado '{zip_final}'.")
        with open("historial.txt", "a") as f:
            f.write(f"Intento de sobrescribir {zip_final}\n")
        return False
    
    zip_1 = zipfile.ZipFile(zip_final, 'w')
    for archivo in contenido:
        ruta_completa = carpeta + "/" + archivo
        if os.path.isfile(ruta_completa):
            zip_1.write(ruta_completa, arcname=archivo)
    zip_1.close()
    
    print("Carpeta comprimida correctamente")
    with open("historial.txt", "a") as f:
        f.write("Backup comprimido creado\n")
    return True

def verificar_restauracio(carpeta_desti): 
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
        print(" El archivo no es un ZIP válido o está roto.")
        with open("historial.txt", "a") as f:
            f.write(" Intento de restaurar un zip corrupto.\n")
        return

    arxiu = zipfile.ZipFile(zip_arxiu, 'r')
    arxiu.extractall(carpeta_desti)  #descomprimimos todo en la carpeta
    arxiu.close()
    
    # Llamamos a la función para comprobar que todo esta bien
    verificar_restauracio(carpeta_desti)
    
    print(f"Restauració completada a {carpeta_desti}")
    with open("historial.txt", "a") as f:
        f.write(" Restauracion completada.\n")