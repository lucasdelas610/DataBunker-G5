import os
import menu


# FJ - 41: Validacion de los archivos

def validar_archivos():
    archivos = [
        "menu.py",
        "key_manager.py",
        "crypto_utils.py",
        "backup_manager.py"
        ]

    error = 0

    for archivo in archivos:
        if os.path.exists(archivo) == True:
            print("Archivos en orden: " + archivo)
        else:
            print("Error, faltan archivos:" + archivo)
            error = error + 1

    if error == 0:
        return True
    else:
        return False


if validar_archivos() == True:
    print("Todo en orden\n")
    menu.mostrar_menu()
else:
    print("Error al iniciar: Faltan archivos importantes")
