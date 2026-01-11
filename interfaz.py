import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import key_manager
import crypto_utils
import backup_manager

def generar():
<<<<<<< HEAD
    # Intenta generar una clave nueva usando el gestor de claves
=======
<<<<<<< HEAD
    # Intenta generar una clave nueva usando el gestor de claves
    clave = key_manager.generar_clave()
    if clave:
        # Si se genera con éxito, muestra un mensaje de éxito
        messagebox.showinfo("Exito", "Clave generada correctamente (clave.key)")
    else:
        # Si ya existe una clave, evita sobrescribirla y avisa al usuario
        messagebox.showwarning("Atencion", "La clave ya existe")

def cifrar():
    # Intenta cargar la clave existente desde el archivo
    clave = key_manager.cargar_clave() # primero se carga la clave
    if not clave:
        # Si no hay clave, no se puede cifrar; muestra error y sale de la función
        messagebox.showerror("Error", "No se encuentra la clave (clave.key)")
        return
    # Abre un explorador de archivos para que el usuario seleccione qué quiere proteger    archivo = filedialog.askopenfilename(title="Elige el archivo a cifrar") # abrimos una ventana para elegir el archivo
    archivo = filedialog.askopenfilename(title="Elige el archivo a cifrar")
    if archivo:
        # Llama a la utilidad de criptografía para procesar el archivo
=======
>>>>>>> lucasdelas610/Develop
    clave = key_manager.generar_clave()
    if clave:
        messagebox.showinfo("Exito", "Clave generada correctamente (clave.key)")
    else:
        messagebox.showwarning("Atencion", "La clave ya existe")

def cifrar():
    # Intenta cargar la clave existente desde el archivo
    clave = key_manager.cargar_clave() # primero se carga la clave
    if not clave:
        messagebox.showerror("Error", "No se encuentra la clave (clave.key)")
        return
     # Abre un explorador de archivos para que el usuario seleccione qué quiere proteger
    archivo = filedialog.askopenfilename(title="Elige el archivo a cifrar") # abrimos una ventana para elegir el archivo
    if archivo:
>>>>>>> origin/Develop
        crypto_utils.cifrar_archivo(archivo, clave)
        messagebox.showinfo("Info", "Revisa la carpeta, deberia estar el .enc")

<<<<<<< HEAD
def descifrar(): # Carga la clave necesaria para la operación inversa
=======
def descifrar():
<<<<<<< HEAD
    # Carga la clave necesaria para la operación inversa
=======
>>>>>>> origin/Develop
>>>>>>> lucasdelas610/Develop
    clave = key_manager.cargar_clave()
    if not clave:
        messagebox.showerror("Error", "Necesitas la clave para descifrar.")
        return
<<<<<<< HEAD
    # Abre el explorador filtrando solo archivos con extensión .enc (cifrados)
    archivo = filedialog.askopenfilename(title="Elige archivo cifrado", filetypes=[("Archivos ENC", "*.enc")])  # se filtra para ver solo archivos .enc
    if archivo:
        # Recupera el contenido original y devuelve el nombre del archivo restaurado
=======
    archivo = filedialog.askopenfilename(title="Elige archivo cifrado", filetypes=[("Archivos ENC", "*.enc")])  # se filtra para ver solo archivos .enc
    if archivo:
>>>>>>> origin/Develop
        nombre_salida = crypto_utils.descifrar_archivo(archivo, clave)
        messagebox.showinfo("Hecho", f"Archivo restaurado: {nombre_salida}")

def backup():
<<<<<<< HEAD
    # Pide al usuario que seleccione qué carpeta completa quiere respaldar
    carpeta = filedialog.askdirectory(title="Selecciona carpeta para hacer backup")  # aqui se elige la carpeta para guardar
    if carpeta:
       # Pide un nombre para el archivo comprimido resultante
        nombre = simpledialog.askstring("Nombre", "Nombre del archivo backup (ej: copia.zip):")
        if nombre:
            # Validación: si el usuario no escribió ".zip", se lo agregamos automáticamente
            if not nombre.endswith(".zip"):
                nombre += ".zip"
            # Llama al gestor de backup para comprimir la carpeta
=======
    carpeta = filedialog.askdirectory(title="Selecciona carpeta para hacer backup")  # aqui se elige la carpeta para guardar
    if carpeta:
       
        nombre = simpledialog.askstring("Nombre", "Nombre del archivo backup (ej: copia.zip):")
        if nombre:
            
            if not nombre.endswith(".zip"):
                nombre += ".zip" #  si el usuario no escribió ".zip", se lo agregamos automáticamente
            
>>>>>>> origin/Develop
            resultado = backup_manager.comprimir_carpeta(carpeta, nombre)
            if resultado:
                messagebox.showinfo("Bien", "Backup creado correctamente.")
            else:
<<<<<<< HEAD
                # Si algo sale mal, sugerimos revisar el log de errores
                messagebox.showerror("Error", "Algo fallo (mira historial.txt)")

def restaurar():
    # Selecciona el archivo ZIP que contiene el respaldo
    archivo_zip = filedialog.askopenfilename(title="Elige el ZIP", filetypes=[("Archivos ZIP", "*.zip")])
    if archivo_zip:
        # Pregunta en qué ubicación desea extraer los archivos
=======
                messagebox.showerror("Error", "Algo fallo (mira historial.txt)")

def restaurar(): # Selecciona el archivo ZIP que contiene el respaldo
    archivo_zip = filedialog.askopenfilename(title="Elige el ZIP", filetypes=[("Archivos ZIP", "*.zip")])
    if archivo_zip:
>>>>>>> origin/Develop
        destino = filedialog.askdirectory(title="Donde lo descomprimo?")
        if destino:
            backup_manager.restaurar_copia(archivo_zip, destino)
            messagebox.showinfo("Listo", "Restauracion completada.")


ventana = tk.Tk()
ventana.title("Programa Cifrado")

<<<<<<< HEAD
# Define el tamaño de la ventana (Ancho x Alto)
=======

>>>>>>> origin/Develop
ventana.geometry("320x380") # estas son las medidas de la ventana

# Etiqueta titulo
lbl_titulo = tk.Label(ventana, text="DATA BUNKER", font=("Arial", 16))
lbl_titulo.pack(pady=10)
<<<<<<< HEAD
# Creación de botones. Cada botón llama a su función correspondiente mediante 'command'
=======

>>>>>>> origin/Develop
tk.Button(ventana, text="1. Generar Clave", command=generar, width=30).pack(pady=10) # Aqui estan todos los botones 
tk.Button(ventana, text="2. Cifrar Archivo", command=cifrar, width=30).pack(pady=10)
tk.Button(ventana, text="3. Descifrar Archivo", command=descifrar, width=30).pack(pady=10)
tk.Button(ventana, text="4. Crear Backup", command=backup, width=30).pack(pady=10)
tk.Button(ventana, text="5. Restaurar Backup", command=restaurar, width=30).pack(pady=10)


tk.Button(ventana, text="Salir", command=ventana.quit, bg="#ffcccc").pack(pady=20) # Con este boton puedes salir del programa

ventana.mainloop() # Bucle principal