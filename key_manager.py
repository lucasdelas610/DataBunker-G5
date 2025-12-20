# Gestion de claves de cifrado

from cryptography.fernet import Fernet
def generar_clave(nom_fitxer = "clave.key"):
    clave = Fernet.generate_key()
    return clave
clave = generar_clave()
print(f"Clave guardada")