from tkinter import *
from PIL import Image, ImageTk


def datos(nombre, apellido, nacionalidad):

    return f"mi nombre es {nombre} {apellido} y soy {nacionalidad}"

ventana = Tk()
ventana.geometry("720x480")
ventana.title("Inicio")


#Objeto Frame

marcos = Frame(ventana, width=300, height=260)
marcos.config(
    bg="#3D85C6",
    bd=12,
    relief=RAISED
)
marcos.pack()
marcos.pack_propagate(False)

text_label = Label(marcos, text="Hola mundo")
text_label.config(
    bg="red",
    font=("Ubuntu", 12),
    relief=SOLID
)
text_label.pack(anchor=CENTER, fill=Y)



imagen = Image.open("/home/alberto/Desarrollo/Python/Tkinter_Python/image/arch.jpg")
render = ImageTk.PhotoImage(imagen)

#Label(ventana, imagen=render).pack()

texto = Label(ventana, text=datos(nombre="alberto",apellido="valerio", nacionalidad="dominicano"))
texto.config(
    fg="white",
    bg="black",
    font=("Ubuntu", 20),
    cursor="spider"
)
texto2 = Label(ventana, text="Hola mundo python")

texto2.config(
    fg="white",
    bg="green",
    font=("Ubuntu", 20),
    cursor="clock"
)

#texto.pack(side=LEFT, fill=Y, expand=YES)
#texto2.pack(fill=Y, expand=YES)



ventana.mainloop()