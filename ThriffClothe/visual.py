import tkinter as tk
from tkinter import ttk, PhotoImage
import io , os


class Visual:
    def __init__(self, root):
        self.style = ttk.Style()
        self.style.configure("TButton", padding=(10, 5), font=("Arial", 12))
        self.root = root
        self.root.title("Interfaz")

    def configurar_ventana(self, width, height):
        x_position = (self.root.winfo_screenwidth() - width) // 2
        y_position = (self.root.winfo_screenheight() - height) // 2
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")

    def crear_boton(self, text, command, row, column):
        button = ttk.Button(self.root, text=text, command=command)
        button.grid(row=row, column=column)

    def crear_entrada(self, row, column):
        entry = ttk.Entry(self.root)
        entry.grid(row=row, column=column)
        return entry

    def ventana_carga(self,row, column):
                # Ruta del archivo GIF
        gif_path = os.path.join(os.path.dirname(__file__), 'loading.gif')

        gif_image = PhotoImage(file=gif_path)

        # Crear la ventana de carga y mostrar el GIF
        self.carga_window = tk.Toplevel(self.root)
        self.carga_window.title("Cargando...")

        label = ttk.Label(self.carga_window, image=gif_image)
        label.image = gif_image  # Mantener referencia a la imagen
        label.pack(padx=20, pady=20)
        label.grid(row=row, column=column)