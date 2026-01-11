import os
from cryptography.fernet import Fernet
# Gestion de claves de cifrado
def generar_clave(nom_fitxer = "clave.key"):
    if os.path.exists(nom_fitxer) == True: # Verifica si el archivo ya existe para no sobrescribir una clave
        print("Cuidado: La clave ya existe. No la toco para no borrarla.")
        return None
    clave = Fernet.generate_key()
    with open (nom_fitxer, "wb") as f: # Abre el archivo y guarda la nueva clave
        f.write(clave)
    return clave

# Función para cargar una clave de cifrado existente
def cargar_clave(nom_fitxer = "clave.key"):
    # Comprobamos si el archivo de la clave existe
    if os.path.exists(nom_fitxer) == False:
        print("Error: No encuentro el archivo de la clave.")
        return None
    with open (nom_fitxer, "rb") as f: # Lee el contenido del archivo para cargarlo
        clave_cargada = f.read()
    # Devolvemos la clave cargada desde el archivo
    return clave_cargada
