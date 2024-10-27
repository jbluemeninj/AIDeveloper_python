import tkinter as tk

ventana = tk.Tk()

#Titulo de la ventana
ventana.title("Mi primera ventana")

#Tamaño de la ventana
ventana.geometry("400x400")
ventana.maxsize(800, 400)
ventana.minsize(400, 400)
ventana.resizable(True, False)

#Color de bg de la ventana
ventana.config(bg="gray")

#Creacion de Frames
frame1 = tk.Frame(ventana, bg="red")
frame2 = tk.Frame(frame1, bg="blue")

#Configuracion del frame
frame1.config(width=200, height=200, bg="red", bd=5, cursor="pirate")
frame2.config(width=100, height=100, bg="blue", bd=5,  cursor="pirate")

#Crear un boton
boton1 = tk.Button(frame1, text="Hola, soy un boton", bg="blue", fg="white")
boton1.pack()

#Crear un label
label1 = tk.Label(frame1, text="Hola, soy un label", bg="red", fg="white")
label1.pack()

#Crear un labelframe
label2 = tk.LabelFrame(frame1, text="Hola, soy un labelframe", bg="red", fg="white")
label2.config(width=200, height=200, bg="red", bd=5, cursor="pirate")
label2.pack()


#Mostrar el frame
frame1.pack()
frame2.pack()

#Mostrar la ventana
ventana.mainloop()