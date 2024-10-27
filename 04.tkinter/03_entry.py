import tkinter as tk
import datetime as fecha_hora
from tkinter.ttk import Label

#Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("400x400")
ventana.resizable(True, False)
ventana.config(bg="gray")
ventana.maxsize(800, 400)
ventana.minsize(400, 400)


"""

#Creamos un label
label1 = tk.Label(ventana, text="Hola, soy un label", bg="red", fg="white")
label1.config(text="Hola, soy un label", bg="red", fg="white", font=("Arial", 20), padx=10, pady=10)
label1.pack()

# Crear un metodo para actualizar la hora
def actualizar_hora():

    hora = fecha_hora.datetime.now().strftime("%H:%M:%S")
    label1.config(text=hora)
    label1.after(1000, actualizar_hora)


#Creamos un boton
boton1 = tk.Button(ventana, text="Hola, soy un boton", bg="blue", fg="white")
boton1.config(text="Hola, soy un boton", bg="blue", fg="white", font=("Arial", 20), padx=10, pady=10)
boton1.pack()

label2 = tk.Label(ventana, text="Hola, soy un label", bg="red", fg="white")
label2.config(text="Hola, soy un label", bg="red", fg="white", font=("Arial", 20), padx=10, pady=10)
label2.pack()

#Creamos un metodo de boton presionado
def boton_presionado():
    label2.config(text="Boton presionado", bg="blue", fg="white", font=("Arial", 20), padx=10, pady=10)

#Creamos un metodo que introduzca un entry
def entrada():
    entrada = tk.Entry(ventana)
    entrada.pack()
    entrada.get()

label2.config(text=entrada.get(), bg="blue", fg="white", font=("Arial", 20), padx=10, pady=10)
label2.pack()


#LLamamos a los metodos
actualizar_hora()

"""

#Creamos un entry
txtNumero1 = tk.Entry(ventana)
txtNumero1.pack()

txtNumero2 = tk.Entry(ventana)
txtNumero2.pack()

labelResultado = tk.Label(ventana)
labelResultado.pack()


def sumar():
    numero1 = int(txtNumero1.get())
    numero2 = int(txtNumero2.get())
    resultado = numero1 + numero2
    labelResultado.config(text=resultado)

btnSumar = tk.Button(ventana, text="sumar", command=sumar)
btnSumar.pack()

#Mostramos la ventana
ventana.mainloop()