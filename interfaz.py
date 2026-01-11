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

def backup():
    carpeta = filedialog.askdirectory(title="Selecciona carpeta para hacer backup")  # aqui se elige la carpeta para guardar
    if carpeta:
       
        nombre = simpledialog.askstring("Nombre", "Nombre del archivo backup (ej: copia.zip):")
        if nombre:
            # Solo se puede si es .zip
            if not nombre.endswith(".zip"):
                nombre += ".zip"
            
            resultado = backup_manager.comprimir_carpeta(carpeta, nombre)
            if resultado:
                messagebox.showinfo("Bien", "Backup creado correctamente.")
            else:
                messagebox.showerror("Error", "Algo fallo (mira historial.txt)")

def restaurar():
    archivo_zip = filedialog.askopenfilename(title="Elige el ZIP", filetypes=[("Archivos ZIP", "*.zip")])
    if archivo_zip:
        destino = filedialog.askdirectory(title="Donde lo descomprimo?")
        if destino:
            backup_manager.restaurar_copia(archivo_zip, destino)
            messagebox.showinfo("Listo", "Restauracion completada.")


ventana = tk.Tk()
ventana.title("Programa Cifrado")


ventana.geometry("320x380") # estas son las medidas de la ventana

# Etiqueta titulo
lbl_titulo = tk.Label(ventana, text="DATA BUNKER", font=("Arial", 16))
lbl_titulo.pack(pady=10)

tk.Button(ventana, text="1. Generar Clave", command=generar, width=30).pack(pady=10) # Aqui estan todos los botones 
tk.Button(ventana, text="2. Cifrar Archivo", command=cifrar, width=30).pack(pady=10)
tk.Button(ventana, text="3. Descifrar Archivo", command=descifrar, width=30).pack(pady=10)
tk.Button(ventana, text="4. Crear Backup", command=backup, width=30).pack(pady=10)
tk.Button(ventana, text="5. Restaurar Backup", command=restaurar, width=30).pack(pady=10)


tk.Button(ventana, text="Salir", command=ventana.quit, bg="#ffcccc").pack(pady=20) # Con este boton puedes salir del programa

ventana.mainloop() # Bucle principal