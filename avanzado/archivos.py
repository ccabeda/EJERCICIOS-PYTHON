import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()
ventana.withdraw() # Oculta la ventana principal

# Crea una ventana de diálogo para seleccionar un archivo
archivo_seleccionado = filedialog.askopenfilename()

# Imprime la ruta del archivo seleccionado
print(archivo_seleccionado)