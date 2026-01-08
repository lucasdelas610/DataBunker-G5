import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import key_manager
import crypto_utils
import backup_manager

def generar():
    clave = key_manager.generar_clave()
    if clave:
        messagebox.showinfo("Exito", "Clave generada correctamente (clave.key)")
    else:
        messagebox.showwarning("Atencion", "La clave ya existe")

def cifrar():
    clave = key_manager.cargar_clave() # primero se carga la clave
    if not clave:
        messagebox.showerror("Error", "No se encuentra la clave (clave.key)")
        return

    archivo = filedialog.askopenfilename(title="Elige el archivo a cifrar") # abrimos una ventana para elegir el archivo
    if archivo:
        crypto_utils.cifrar_archivo(archivo, clave)
        messagebox.showinfo("Info", "Revisa la carpeta, deberia estar el .enc")

def descifrar():
    clave = key_manager.cargar_clave()
    if not clave:
        messagebox.showerror("Error", "Necesitas la clave para descifrar.")
        return
    archivo = filedialog.askopenfilename(title="Elige archivo cifrado", filetypes=[("Archivos ENC", "*.enc")])  # se filtra para ver solo archivos .enc
    if archivo:
        nombre_salida = crypto_utils.descifrar_archivo(archivo, clave)
        messagebox.showinfo("Hecho", f"Archivo restaurado: {nombre_salida}")
