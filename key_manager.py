# Gestion de claves de cifrado
import os

from cryptography.fernet import Fernet
# Función para generar una clave de cifrado
def generar_clave(nom_fitxer = "clave.key"):
    # Comprobamos si el archivo de la clave ya existe
    if os.path.exists(nom_fitxer) == True:
        # Evitamos sobrescribir una clave existente
        print("Cuidado: La clave ya existe. No la toco para no borrarla.")
        return None
    # Generamos una nueva clave segura usando Fernet
    clave = Fernet.generate_key()
   # Guardamos la clave en un archivo en modo binario
    with open (nom_fitxer, "wb") as f:
        f.write(clave)
    # Devolvemos la clave generada (por si se quiere usar en el momento)
    return clave

# Función para cargar una clave de cifrado existente
def cargar_clave(nom_fitxer = "clave.key"):
    # Comprobamos si el archivo de la clave existe
    if os.path.exists(nom_fitxer) == False:
        print("Error: No encuentro el archivo de la clave.")
        return None
     # Abrimos el archivo de la clave en modo lectura binaria
    with open (nom_fitxer, "rb") as f:
        clave_cargada = f.read()
    # Devolvemos la clave cargada desde el archivo
    return clave_cargada
