import tkinter as tk
from tkinter import messagebox

class utils:
    def fin(Tiempo):
        horas = int(Tiempo) // 3600
        minutos = (int(Tiempo) % 3600) // 60
        segundos = int(Tiempo) % 60

        # Calcula milisegundos
        milisegundos = int((Tiempo - int(Tiempo)) * 1000)

        mensaje = "Tiempo transcurrido:\n{} horas, {} minutos, {} segundos y {} milisegundos".format(horas, minutos, segundos, milisegundos)
        
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Tiempo Transcurrido", mensaje)
        root.destroy()

    # def 