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

# FJ-24
def descifrar_archivo(archivo_encriptado, clave):
    if os.path.exists(archivo_encriptado) == False: # se mira si existe
        print("Error: No encuentro el archivo cifrado(.enc)")
        return None
        
    f = Fernet(clave)
    with open(archivo_encriptado, "rb") as file:
        datos_encriptados = file.read()
            
    datos_originales = f.decrypt(datos_encriptados)#La librería Fernet descifra los datos
    nombre_salida = archivo_encriptado.replace(".enc", "") # se le quita .enc al nombre para guardarlo
        
    with open(nombre_salida, "wb") as file:
        file.write(datos_originales)
    print("Archivo descifrado temporalmente: " + nombre_salida)
    return nombre_salida