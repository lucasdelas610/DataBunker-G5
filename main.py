# Punto de entrada del programa
import os
import zipfile





# FJ-22
import key_manager
import crypto_utils


# 1. Pruebo si la clave se genera bien
print("1. Probando gestor de claves...")
key_manager.generar_clave() 

# 2. Creo un archivo para ver si cifra bien
with open("test_secreto.txt", "w") as f:
    f.write("Esto es una prueba de cifrado")
# 3. Intento cifrarlo usando mi funcion de crypto_utils
print("2. Probando a cifrar archivo de prueba")

mi_clave = key_manager.cargar_clave() # Cargo la clave primero

if mi_clave:
    crypto_utils.cifrar_archivo("test_secreto.txt", mi_clave) # Si tengo clave, intento cifrar

    # 4. Compruebo si ha salido el archivo .enc
    if os.path.exists("test_secreto.txt.enc"):
        print("Perfecto: El cifrado funciona, se ha creado el archivo .enc")
    else:
        print("Fallo: No se ha creado el archivo cifrado")
else:
    print("No se ha podido probar el cifrado porque fallo la clave")

print("Fin de las pruebas")


def pedir_nombre_archivo(): # FJ-27
    nombre = input("Escribe el nombre del archivo: ")
    return nombre
