import os
import time
import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image
from utils import utils
from tqdm import tqdm

def borrar_fondo(input_folder):
    # Carpeta de salida
    output_folder = os.path.abspath(os.path.join(input_folder, "Sin Fondo"))

    # Asegurar que la carpeta de salida exista
    os.makedirs(output_folder, exist_ok=True)

    tiempo_inicio = time.time()

    # Obtener la lista de archivos en la carpeta de entrada
    files = [filename for filename in os.listdir(input_folder) if filename.endswith((".jpg", ".png"))]

    # Configuración de la barra de progreso
    progress_window = tk.Tk()
    progress_window.title("Progreso")
    progress_bar = tk.ttk.Progressbar(progress_window, length=300, mode='determinate')
    progress_bar.pack(pady=10)
    progress_label = tk.Label(progress_window, text="")
    progress_label.pack()

    # Función para actualizar la barra de progreso
    def update_progress(file_idx):
        progress_label.config(text=f"Procesando: {files[file_idx]}")
        progress_window.update_idletasks()
        progress_bar["value"] = (file_idx + 1) * 100 / len(files)

    # Procesar archivos en la carpeta de entrada
    for i, filename in enumerate(files):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # Leer los datos de la imagen en formato de bytes
            with open(input_path, 'rb') as i:
                input_data = i.read()

            # Eliminar el fondo usando rembg con los parámetros definidos
            output_data = remove(input_data, alpha_matting=True, alpha_matting_foreground_threshold=240,
                                alpha_matting_background_threshold=10, alpha_matting_erode_structure_size=10,
                                alpha_matting_base_size=1000)

            # Guardar la imagen resultante
            with open(output_path, 'wb') as o:
                o.write(output_data)

        except Exception as e:
            print(f"Error al procesar {filename}: {str(e)}")

    # Actualizar la barra de progreso
    update_progress(i)


    tiempo_fin = time.time()
    utils.fin(tiempo_fin - tiempo_inicio)
    progress_label.config(text="Proceso completado.")
    progress_window.mainloop()


