import tkinter as tk
from tkinter import messagebox
import requests


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

    def check_url_content(url):
        try:
            response = requests.get(url)
            if response.status_code == 200 and response.text:
                return response.text
            else:
               print("sin acceso")
        except requests.exceptions.RequestException as e:
            return print("sin acceso")

    # def guardar():
