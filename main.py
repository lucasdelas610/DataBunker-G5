# Punto de entrada del programa
import os
import zipfile

def comprimir_carpeta(carpeta, zip_final):
    if os.path.exists(carpeta) == False:
        print("Error: La carpeta que quieres comprimir no existe.")
        return
    zip_1 = zipfile.ZipFile(zip_final, 'w')
    for archivo in os.listdir(carpeta):
        zip_1.write(carpeta + "/" + archivo)
    zip_1.close()
#Si le das a iniciar se guarda ya la copia .zip FJ 19



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