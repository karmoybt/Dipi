import tkinter as tk
from tkinter import ttk

class Visual:
    def __init__(self, root):
        self.style = ttk.Style()
        self.style.configure("TButton", padding=(10, 5), font=("Arial", 12))
        self.root = root
        self.root.title("Interfaz")

    def configurar_ventana(self, width, height):
        # Calcular la posición centrada
        x_position = (self.root.winfo_screenwidth() - width) // 2
        y_position = (self.root.winfo_screenheight() - height) // 2
        # Establecer tamaño y posición de la ventana
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")

    def crear_boton(self, text, command, row, column):
        button = ttk.Button(self.root, text=text, command=command)
        button.grid(row=row, column=column)

    def crear_entrada(self, row, column):
        entry = ttk.Entry(self.root)
        entry.grid(row=row, column=column)
        return entry

    def obtener_contenido_entrada(self, entry):
        contenido = entry.get()
        print("Contenido de la entrada:", contenido)

