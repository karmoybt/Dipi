import os,time
from wand.image import Image
from utils import utils

def redimensionar_imagen(ruta, ancho, alto):
    print("Procesando la carpeta:", ruta)

    # Carpeta de entrada y salida
    input_folder = os.path.abspath(ruta)
    output_folder = os.path.abspath(os.path.join(os.path.dirname(ruta), "Redimensionar"))

    # Asegurar que la carpeta de salida exista
    os.makedirs(output_folder, exist_ok=True)

    tiempo_inicio = time.time()

    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".png")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image(filename=input_path) as img:
                img.transform(resize=f'{ancho}x{alto}')
                img.extent(width=ancho, height=alto, gravity='center')
                img.save(filename=output_path)
    
    tiempo_fin = time.time()
    utils.fin(tiempo_fin-tiempo_inicio)
