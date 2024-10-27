import tkinter as tk

ventana = tk.Tk()
ventana.config(width=300, height=200, bg="gray",  bd=5, cursor="pirate")
ventana.title("Ventana ")


#Eventos
def saludar():
    print("Hola mundo")

labelSaludo = tk.Label(ventana)
labelSaludo.config(text="Hola mundo")
labelSaludo.pack()
btnSaludar = tk.Button(ventana, text="Saludar", command=saludar)
btnSaludar.pack()

btnSaludar.config(bg="red", fg="white", bd=5, cursor="pirate")
labelSaludo.config(bg="red", fg="white", bd=5, cursor="pirate")


ventana.mainloop()