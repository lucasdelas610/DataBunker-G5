import os
import key_manager
import crypto_utils
import backup_manager
# Funcion principal que muestra el menu y gestiona las opciones
def mostrar_menu():
    # Bucle infinito hasta que el usuario decida salir
    while True:
        print("MENU")
        print("1. Generar Clave")
        print("2. Cifrar Archivo")
        print("3. Descifrar Archivo")
        print("4. Crear Backup (Zip)")
        print("5. Restaurar Backup")
        print("6. Eliminar Archivo Temporal")
        print("0. Salir")
        
        # Uso strip() para que no fallen los espacios
        opcion = input("Selecciona una opcion: ").strip()

        # Si le das al Enter sin escribir nada, vuelve a empezar
        if opcion == "":
            continue
        # Opción 1: Generar una clave de cifrado
        if opcion == "1":
            key_manager.generar_clave()
        # Opción 2: Cifrar un archivo
        elif opcion == "2":
            # FJ-39 Cargamos la clave desde el archivo
            clave = key_manager.cargar_clave()
            # Si no existe la clave, avisamos al usuario
            if clave is None:
                print("ATENCION: No se encontro la clave. Usa la opcion 1 primero.")
            else:
                archivo = input("Archivo a cifrar: ")
                # Validamos si el archivo existe 
                if os.path.exists(archivo):
                    crypto_utils.cifrar_archivo(archivo, clave)
                else:
                    print("Error: El archivo no existe.")
        # Opción 3: Descifrar un archivo
        elif opcion == "3":
            # Cargamos la clave necesaria para descifrar
            clave = key_manager.cargar_clave()
            
            if clave is None:
                print("ATENCION: Necesitas la clave para descifrar.")
            else:
                archivo = input("Archivo .enc a descifrar: ")
                # Verificamos que el archivo exista
                if os.path.exists(archivo):
                    crypto_utils.descifrar_archivo(archivo, clave)
                else:
                    print("Error: El archivo no existe.")
        # Opción 4: Crear un backup comprimido (ZIP)
        elif opcion == "4":
            carpeta = input("Carpeta para backup: ").strip()
            # Comprobamos que la carpeta exista
            if os.path.exists(carpeta):
                destino = input("Nombre del archivo: ").strip()
                
                # obligamos a que el nombre tenga algo escrito
                if len(destino) > 0:
                    backup_manager.comprimir_carpeta(carpeta, destino)
                else:
                    print("Error, el nombre del archivo no puede estar vacio.")
            else:
                print("La carpeta no existe.")
        # Opción 5: Restaurar un backup ZIP
        elif opcion == "5":
            archivo_zip = input("Archivo ZIP a restaurar: ").strip()
            if os.path.exists(archivo_zip):
                destino = input("Carpeta de destino: ").strip()
                
                # obligamos a poner destino
                if len(destino) > 0:
                    backup_manager.restaurar_copia(archivo_zip, destino)
                else:
                    print("Error, debes decirme donde guardarlo.")
            else:
                print("Error, el archivo ZIP no existe.")
        # Opción 6: Eliminar un archivo temporal
        elif opcion == "6":
            # Lista de archivos que NO deben eliminarse
            archivos_esenciales = ["main.py",
                                   "menu.py",
                                   "key_manager.py",
                                   "crypto_utils",
                                   "backup_manager.py",
                                   "clave.key",
                                   "historial.txt",
                                   "README.md",
                ]

            borrar_archivo = input("Introduce el nombre del archivo que quieres eliminar: ")

            if archivo in archivos_esenciales:
                print("Error: Estos archivos no se pueden eliminar")

            elif os.path.exists(borrar_archivo):
                # Pedimos confirmación antes de borrar
                confirmacion = input(f"Estas seguro que quieres borrar este archivo: {borrar_archivo}")
                if confirmacion.lower() == "si":
                    os.remove(borrar_archivo)
                    print(f"El archivo ha sido eliminado correctamente")
                else:
                    print("El archivo no ha sido eliminado")
            else:
                print("El archivo que quieres eliminar no existe")
        # Opción 0: Salir del programa
        elif opcion == "0":
            print("Saliendo")
            break
        # Cualquier otra opción no válida
        else:
            print("Opcion no valida.")