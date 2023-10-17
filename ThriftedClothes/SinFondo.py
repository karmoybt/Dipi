import os
from rembg import remove
from utils import utils

def borrar_fondo(input_folder):

    output_folder = os.path.join(os.path.dirname(input_folder), "Sin Fondo")
    os.makedirs(output_folder, exist_ok=True)

    files = [filename for filename in os.listdir(input_folder) if filename.endswith((".jpg", ".png"))]

    def process_files():
        for filename in files:
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with open(input_path, 'rb') as i_file:
                    input_data = i_file.read()

                output_data = remove(input_data, alpha_matting=True, alpha_matting_foreground_threshold=240,
                                    alpha_matting_background_threshold=10, alpha_matting_erode_structure_size=10,
                                    alpha_matting_base_size=1000)

                with open(output_path, 'wb') as o_file:
                    o_file.write(output_data)

            except Exception as e:
                print(f"Error al procesar {filename}: {str(e)}")

        progress_complete()

    def progress_complete():
        print("Proceso completado.")

    process_files()
