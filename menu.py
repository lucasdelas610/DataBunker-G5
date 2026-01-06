import os
import key_manager
import crypto_utils
import backup_manager

def mostrar_menu():
    while True:
        print("MENU")
        print("1. Generar Clave")
        print("2. Cifrar Archivo")
        print("3. Descifrar Archivo")
        print("4. Crear Backup (Zip)")
        print("5. Restaurar Backup")
        print("0. Salir")
        
        # Uso strip() para que no fallen los espacios
        opcion = input("Selecciona una opcion: ").strip()

        # Si le das al Enter sin escribir nada, vuelve a empezar
        if opcion == "":
            continue

        if opcion == "1":
            key_manager.generar_clave()
        
        elif opcion == "2":
            # FJ-39
            clave = key_manager.cargar_clave()
            
            if clave is None:
                print("ATENCION: No se encontro la clave. Usa la opcion 1 primero.")
            else:
                archivo = input("Archivo a cifrar: ")
                # Validamos si el archivo existe 
                if os.path.exists(archivo):
                    crypto_utils.cifrar_archivo(archivo, clave)
                else:
                    print("Error: El archivo no existe.")

        elif opcion == "3":
            # FJ-39
            clave = key_manager.cargar_clave()
            
            if clave is None:
                print("ATENCION: Necesitas la clave para descifrar.")
            else:
                archivo = input("Archivo .enc a descifrar: ")
                if os.path.exists(archivo):
                    crypto_utils.descifrar_archivo(archivo, clave)
                else:
                    print("Error: El archivo no existe.")

        elif opcion == "4":
            carpeta = input("Carpeta para backup: ").strip()
            if os.path.exists(carpeta):
                destino = input("Nombre del archivo: ").strip()
                
                # obligamos a que el nombre tenga algo escrito
                if len(destino) > 0:
                    backup_manager.comprimir_carpeta(carpeta, destino)
                else:
                    print("Error, el nombre del archivo no puede estar vacio.")
            else:
                print("La carpeta no existe.")

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

        elif opcion == "0":
            print("Saliendo")
            break
        else:
            print("Opcion no valida.")