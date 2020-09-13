from tkinter import Tk
import os.path
import mysql


#crear la ventana

class Main:
    def __init__(self):
        self.title = "Proyecto calculadora"
        self.size = "360x250"
        self.resizable = True

    def carga(self):
        ventana = Tk()

        #Dimensiones de ventana
        ventana.geometry("980x650")

        #Titulo de ventana
        ventana.title("Hola mundo")

        #Para dimensionar o no
        ventana.resizable(0,0)

        #Arrancar la ventana 
        ventana.mainloop()

run = Main()
run.carga()
