# Funciones de cifrado i descifrado

from cryptography.fernet import Fernet
import os


# FJ-22: Función para proteger archivos convirtiéndolos a formato .enc
def cifrar_archivo(nombre_archivo, clave):
    # Validaciones para que no falle
    # Comprobamos que la clave no esté vacía 
    if clave == None:
        print("Error: Sin clave no puedo cifrar nada.")
        return
    # Comprobamos que el archivo original realmente exista en el disco
    if os.path.exists(nombre_archivo) == False:
        print("Error: El archivo no esta, asi que no puedo cifrarlo.")
        return

    # Cifrado
    # Inicializamos el motor de cifrado Fernet con la clave proporcionada
    f = Fernet(clave)
    # Abrimos el archivo original en modo "rb" (lectura binaria) para leer cualquier tipo de archivo
    with open(nombre_archivo, "rb") as file:
        datos = file.read()
    # Aplicamos el algoritmo de cifrado a los datos leídos
    datos_encriptados = f.encrypt(datos)  # Convierto los datos normales a datos cifrados
    # Definimos el nuevo nombre del archivo agregando la extensión .enc
    nombre_final = nombre_archivo + ".enc"
    
    # Guardo los datos cifrados en ese archivo nuevo
    with open(nombre_final, "wb") as file:
        file.write(datos_encriptados)
        
    print("He creado el archivo cifrado: " + nombre_final)

# FJ-24: Función para recuperar el contenido original de un archivo .enc
def descifrar_archivo(archivo_encriptado, clave):
    # Verificamos que el archivo cifrado exista antes de intentar abrirlo
    if os.path.exists(archivo_encriptado) == False: # se mira si existe
        print("Error: No encuentro el archivo cifrado(.enc)")
        return None
    # Inicializamos Fernet con la misma clave que se usó para cifrar    
    f = Fernet(clave)
    # Leemos el contenido cifrado (en binario)
    with open(archivo_encriptado, "rb") as file:
        datos_encriptados = file.read()
    # La librería Fernet descifra los datos. Si la clave es incorrecta, aquí daría un error.        
    datos_originales = f.decrypt(datos_encriptados)#La librería Fernet descifra los datos
    nombre_salida = archivo_encriptado.replace(".enc", "") # se le quita .enc al nombre para guardarlo
    # Guardamos los datos recuperados en un archivo limpio    
    with open(nombre_salida, "wb") as file:
        file.write(datos_originales)
    print("Archivo descifrado temporalmente: " + nombre_salida)
    # Retornamos el nombre para que la interfaz gráfica pueda mostrarlo en el mensaje
    return nombre_salida

    