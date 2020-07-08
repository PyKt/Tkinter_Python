from tkinter import *

ventana = Tk()
ventana.geometry("450x250")
ventana.title("Formulario")

#Texto encabezado
encabezado = Label(ventana, text="Formulario tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Ubuntu",15)
)
encabezado.grid(row=0, column=0, columnspan=3 ,sticky=W)

campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=0, padx=5, sticky=W)
campo_texto.config(justify="right",state="normal")

#Label para el campo
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, sticky=W)


ventana.mainloop()