# Funciones de cifrado i descifrado

from cryptography.fernet import Fernet
import os


# FJ-22
def cifrar_archivo(nombre_archivo, clave):
    # Validaciones para que no falle 
    if clave == None:
        print("Error: Sin clave no puedo cifrar nada.")
        return

    if os.path.exists(nombre_archivo) == False:
        print("Error: El archivo no esta, asi que no puedo cifrarlo.")
        return

    # Cifrado
    f = Fernet(clave)
    with open(nombre_archivo, "rb") as file:
        datos = file.read()
    
    datos_encriptados = f.encrypt(datos)  # Convierto los datos normales a datos cifrados
    nombre_final = nombre_archivo + ".enc"
    
    # Guardo los datos cifrados en ese archivo nuevo
    with open(nombre_final, "wb") as file:
        file.write(datos_encriptados)
        
    print("He creado el archivo cifrado: " + nombre_final)