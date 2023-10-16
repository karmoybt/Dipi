import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from Redimensionar import redimensionar_imagen


class Botones:
    def __init__(self, entry, borrar_fondo):
        self.entry = entry
        self.borrar_fondo = borrar_fondo
        self.ancho = 1000 
        self.alto = 1000 


    def crear_texto(self, root, row, column):
        entry_widget = ttk.Entry(root)
        entry_widget.grid(row=row, column=column)
        return entry_widget

    def crear_texto_obtener_ruta(self, root, row, column):
        entry_widget = ttk.Entry(root)
        entry_widget.grid(row=row, column=column)

        ruta_seleccionada = tk.StringVar()

        def obtener_ruta_func():
            contenido = entry_widget.get()
            if not contenido:
                ruta = filedialog.askdirectory()
                if ruta:
                    ruta_seleccionada.set(ruta)
                    entry_widget.delete(0, tk.END)
                    entry_widget.insert(tk.END, ruta)
            else:
                ruta_seleccionada.set(contenido)

        return entry_widget, obtener_ruta_func, ruta_seleccionada

    def obtener_ruta(self):
        contenido = self.entry.get()
        if not contenido:
            ruta_seleccionada = filedialog.askdirectory()
            if ruta_seleccionada:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, ruta_seleccionada)
        else:
            print(contenido)

    def btn_borrar_fondo(self):
        self.obtener_ruta()  # Llama a obtener_ruta al principio
        ruta = self.entry.get()
        if ruta:
            self.borrar_fondo(ruta)
        else:  
            print("Primero selecciona una ruta")

    def redimensionar(self):
        self.obtener_ruta()  # Llama a obtener_ruta al principio
        ruta = self.entry.get()
        alto = self.alto
        ancho = self.ancho

        if ruta and alto and ancho:
            redimensionar_imagen(ruta, alto, ancho)
        else:
            print("Completa todos los campos antes de redimensionar.")


