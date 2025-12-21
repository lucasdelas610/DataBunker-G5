# Gestion de claves de cifrado
import os

from cryptography.fernet import Fernet

def generar_clave(nom_fitxer = "clave.key"):
    if os.path.exists(nom_fitxer) == True:
        print("Cuidado: La clave ya existe. No la toco para no borrarla.")
        return None
    clave = Fernet.generate_key()
    with open (nom_fitxer, "wb") as f:
        f.write(clave)
    return clave
clave = generar_clave()
print(f"Clave guardada correctamente")

def cargar_clave(nom_fitxer = "clave.key"):
    if os.path.exists(nom_fitxer) == False:
        print("Error: No encuentro el archivo de la clave.")
        return None
    with open (nom_fitxer, "rb") as f:
        clave_cargada = f.read()
    return clave_cargada
