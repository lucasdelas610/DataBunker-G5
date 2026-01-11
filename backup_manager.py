# Creación y restauración de copias de seguridad (backups)

import zipfile   
import os       


<<<<<<< HEAD

def comprimir_carpeta(carpeta, zip_final): # # Función que comprime una carpeta en un archivo ZIP
=======
# Función que comprime una carpeta en un archivo ZIP
def comprimir_carpeta(carpeta, zip_final):  # Validar que existen los archivos
    # Comprobamos que la carpeta existe
>>>>>>> lucasdelas610/Develop
    if os.path.exists(carpeta) == False:
        print("La carpeta no existe.")
        # Guardamos el error en el historial
        with open("historial.txt", "a") as f:
            f.write("La carpeta a comprimir no existe\n")
        return False
    
    # Validamos que la carpeta no esté vacía
    contenido = os.listdir(carpeta)
    if len(contenido) == 0:
        print("La carpeta está vacía")
        # Registramos el intento fallido en el historial
        with open("historial.txt", "a") as f:
            f.write("Intento de comprimir carpeta vacía\n")
        return False

    # Evitamos sobrescribir un backup existente
    if os.path.exists(zip_final) == True:
        print(f"Ya existe un archivo llamado '{zip_final}'.")
        with open("historial.txt", "a") as f:
            f.write(f"Intento de sobrescribir {zip_final}\n")
        return False
    
    # Creamos el archivo ZIP en modo escritura
    zip_1 = zipfile.ZipFile(zip_final, 'w')

    # Recorremos los archivos dentro de la carpeta
    for archivo in contenido:
        ruta_completa = carpeta + "/" + archivo
        # Solo añadimos archivos, no subcarpetas
        if os.path.isfile(ruta_completa):
            # arcname evita guardar la ruta completa dentro del ZIP
            zip_1.write(ruta_completa, arcname=archivo)

    # Cerramos el archivo ZIP
    zip_1.close()
    
    print("Carpeta comprimida correctamente")
    # Registramos la acción correcta en el historial
    with open("historial.txt", "a") as f:
        f.write("Backup comprimido creado\n")

    return True


# Función que verifica si una restauración se ha realizado correctamente
def verificar_restauracio(carpeta_desti):
    # Comprobamos que la carpeta destino exista
    if os.path.exists(carpeta_desti):
        fitxers = os.listdir(carpeta_desti)

        # Si contiene archivos, la restauración es correcta
        if len(fitxers) > 0:
            print(f"Verificación completada, se han encontrado {len(fitxers)} archivos.")
            return True
        else:
            print("Verificación fallida, la carpeta está vacía.")
            return False
    else:
        print("Verificación fallida, la carpeta no existe.")
        return False


# Función que restaura una copia de seguridad desde un archivo ZIP
def restaurar_copia(zip_arxiu, carpeta_desti):  # Validar formato ZIP
    # Comprobamos que el archivo sea un ZIP válido
    if zipfile.is_zipfile(zip_arxiu) == False:
        print("El archivo no es un ZIP válido o está dañado.")
        # Guardamos el intento fallido en el historial
        with open("historial.txt", "a") as f:
            f.write("Intento de restaurar un zip corrupto.\n")
        return

    # Abrimos el archivo ZIP en modo lectura
    arxiu = zipfile.ZipFile(zip_arxiu, 'r')

    # Extraemos todo el contenido en la carpeta destino
    arxiu.extractall(carpeta_desti)
    arxiu.close()
    
    # Llamamos a la función de verificación
    verificar_restauracio(carpeta_desti)
    
    print(f"Restauración completada en {carpeta_desti}")
    # Registramos la restauración en el historial
    with open("historial.txt", "a") as f:
<<<<<<< HEAD
        f.write("Restauración completada.\n")
=======
        f.write("EXITO: Restauracion completada.\n")

>>>>>>> origin/Develop
