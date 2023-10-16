# This code is creating a graphical user interface (GUI) using the tkinter library in Python.
import tkinter as tk
from botones import Botones
from SinFondo import borrar_fondo
from visual import Visual

# In the given code, `root = tk.Tk()` creates the main window or the root window of the GUI
# application using the `Tk()` class from the `tkinter` library. This root window is the main
# container for all the other GUI elements.
root = tk.Tk()
ventana = Visual(root)
ventana.configurar_ventana(400, 200)


# These lines of code are creating input fields (entry widgets) in the graphical user interface (GUI).
ruta = ventana.crear_entrada(0, 1)
alto = ventana.crear_entrada(2, 1)
ancho = ventana.crear_entrada(2, 2)

botones = Botones(root, ruta, borrar_fondo)

# These lines of code are creating buttons in the graphical user interface (GUI).
ventana.crear_boton("Obtener Ruta", botones.obtener_ruta, 0, 0)
ventana.crear_boton("Borrar Fondo", botones.btn_borrar_fondo, 1, 0)
ventana.crear_boton("Color Fondo", botones.btn_borrar_fondo, 1, 1)
ventana.crear_boton("Redimensionar", botones.redimensionar, 2, 0)

root.mainloop()
