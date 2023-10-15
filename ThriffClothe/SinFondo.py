import os
import io
import time
from rembg import remove
from PIL import Image
from utils import utils

def borrar_fondo(ruta):
    print("Procesando la carpeta:", ruta)

    # Carpeta de entrada y salida
    input_folder = os.path.abspath(ruta)
    output_folder = os.path.abspath(os.path.join(os.path.dirname(ruta), "Sin Fondo"))

    # Asegurar que la carpeta de salida exista
    os.makedirs(output_folder, exist_ok=True)

    tiempo_inicio = time.time()
    # Procesar archivos en la carpeta de entrada
    for filename in os.listdir(input_folder):
        print(filename + str(time.time()))

        if filename.endswith((".jpg", ".png")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # Leer los datos de la imagen en formato de bytes
                with open(input_path, 'rb') as i:
                    input_data = i.read()

                # Eliminar el fondo usando rembg con los parámetros definidos
                output_data = remove(input_data, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10,
                                    alpha_matting_erode_structure_size=10, alpha_matting_base_size=1000)

                # Guardar la imagen resultante
                with open(output_path, 'wb') as o:
                    o.write(output_data)

            except Exception as e:
                print(f"Error al procesar {filename}: {str(e)}")

    tiempo_fin = time.time()
    utils.fin(tiempo_fin - tiempo_inicio)
