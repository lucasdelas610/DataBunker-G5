import os
from cryptography.fernet import Fernet
<<<<<<< HEAD
# Gestion de claves de cifrado
def generar_clave(nom_fitxer = "clave.key"):
    if os.path.exists(nom_fitxer) == True: # Verifica si el archivo ya existe para no sobrescribir una clave
=======
# Función para generar una clave de cifrado
def generar_clave(nom_fitxer = "clave.key"):
    # Comprobamos si el archivo de la clave ya existe
    if os.path.exists(nom_fitxer) == True:
        # Evitamos sobrescribir una clave existente
>>>>>>> origin/Develop
        print("Cuidado: La clave ya existe. No la toco para no borrarla.")
        return None
    # Generamos una nueva clave segura usando Fernet
    clave = Fernet.generate_key()
<<<<<<< HEAD
    with open (nom_fitxer, "wb") as f: # Abre el archivo y guarda la nueva clave
=======
   # Guardamos la clave en un archivo en modo binario
    with open (nom_fitxer, "wb") as f:
>>>>>>> origin/Develop
        f.write(clave)
    # Devolvemos la clave generada (por si se quiere usar en el momento)
    return clave

# Función para cargar una clave de cifrado existente
def cargar_clave(nom_fitxer = "clave.key"):
    # Comprobamos si el archivo de la clave existe
    if os.path.exists(nom_fitxer) == False:
        print("Error: No encuentro el archivo de la clave.")
        return None
<<<<<<< HEAD
    with open (nom_fitxer, "rb") as f: # Lee el contenido del archivo para cargarlo
=======
     # Abrimos el archivo de la clave en modo lectura binaria
    with open (nom_fitxer, "rb") as f:
>>>>>>> origin/Develop
        clave_cargada = f.read()
    # Devolvemos la clave cargada desde el archivo
    return clave_cargada
