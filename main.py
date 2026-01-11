# Punto de entrada del programa
import os
import zipfile





# FJ-22
# Importamos nuestros módulos personalizados
import key_manager
import crypto_utils


# 1. Pruebo si la clave se genera bien
print("1. Probando gestor de claves...")
# Llamamos a la función que genera la clave y la guarda
key_manager.generar_clave() 

# 2. Creo un archivo para ver si cifra bien
# Abrimos (o creamos) un archivo de texto en modo escritura
with open("test_secreto.txt", "w") as f:
    # Escribimos un texto de prueba dentro del archivo
    f.write("Esto es una prueba de cifrado")
# 3. Intento cifrarlo usando mi funcion de crypto_utils
print("2. Probando a cifrar archivo de prueba")
# Cargo la clave desde el gestor de claves
mi_clave = key_manager.cargar_clave() # Cargo la clave primero
# Verifico que la clave se haya cargado correctamente
if mi_clave:
    # Si hay clave, intento cifrar el archivo de prueba
    crypto_utils.cifrar_archivo("test_secreto.txt", mi_clave) # Si tengo clave, intento cifrar

    # 4. Compruebo si ha salido el archivo .enc
    # Verificamos si el archivo cifrado existe

    if os.path.exists("test_secreto.txt.enc"):
        print("Perfecto: El cifrado funciona, se ha creado el archivo .enc")
    else:
        print("Fallo: No se ha creado el archivo cifrado")
else:
    # Si no se pudo cargar la clave, avisamos
    print("No se ha podido probar el cifrado porque fallo la clave")
# Mensaje final indicando que las pruebas han terminado
print("Fin de las pruebas")

# Función que pide al usuario el nombre de un archivo
def pedir_nombre_archivo(): # FJ-27
    nombre = input("Escribe el nombre del archivo: ")
    return nombre
# Función que elimina un archivo dado su ruta
def eliminar_archivo(ruta_archivo): #FJ-28
    os.remove(ruta_archivo)
