# Gestion de claves de cifrado

from cryptography.fernet import Fernet

def generar_clave(nom_fitxer = "clave.key"):
    clave = Fernet.generate_key()
    with open (nom_fitxer, "wb") as f:
        f.write(clave)
    return clave
clave = generar_clave()
print(f"Clave guardada correctamente")

def cargar_clave(nom_fitxer = "clave.key"):
    with open (nom_fitxer, "rb") as f:
        clave_cargada = f.read()
    return clave_cargada
