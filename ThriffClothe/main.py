import tkinter as tk
from botones import Botones
from SinFondo import borrar_fondo
from visual import Visual

root = tk.Tk()

ventana = Visual(root)
ventana.configurar_ventana(400, 200)


ruta = ventana.crear_entrada(0, 1)
alto = ventana.crear_entrada(2, 1)
ancho = ventana.crear_entrada(2, 2)

botones = Botones(root, ruta, borrar_fondo)

ventana.crear_boton("Obtener Ruta", botones.obtener_ruta, 0, 0)
ventana.crear_boton("Borrar Fondo", botones.btn_borrar_fondo, 1, 0)
ventana.crear_boton("Color Fondo", botones.btn_borrar_fondo, 1, 1)
ventana.crear_boton("Redimensionar", botones.redimensionar, 2, 0)

root.mainloop()
