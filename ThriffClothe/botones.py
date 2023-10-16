import tkinter as tk
from tkinter import filedialog
from Redimensionar import redimensionar_imagen

class Botones:
    def __init__(self, entry, borrar_fondo):
        self.entry = entry
        self.borrar_fondo = borrar_fondo
        self.ancho = 1000
        self.alto = 1000

    def obtener_ruta(self):
        contenido = self.entry.get()
        if not contenido:
            ruta_seleccionada = filedialog.askdirectory()
            if ruta_seleccionada:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, ruta_seleccionada)
                return ruta_seleccionada
        else:
           return contenido

    def btn_borrar_fondo(self):
        ruta = self.obtener_ruta()
        self.borrar_fondo(ruta)


    def redimensionar(self):
        ruta = self.obtener_ruta()
        alto = self.alto
        ancho = self.ancho

        if ruta and alto and ancho:
            redimensionar_imagen(ruta, alto, ancho)
        else:
            print("Completa todos los campos antes de redimensionar.")
