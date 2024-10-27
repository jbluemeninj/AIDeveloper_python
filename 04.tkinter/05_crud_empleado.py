import tkinter as tk
from tkinter import messagebox

#Crear una CRUD de Empleados

#Declaracion de variables
empleados = []

#Funciones
def agregar():
    nombre = txtNombre.get()
    edad = txtEdad.get()

    if nombre and edad.isdigit():
        empleado = {"nombre": nombre, "edad": edad}
        empleados.append(empleado)
        lstEmpleados.insert(tk.END, empleado["nombre"] + " - " + empleado["edad"])
        actualizar_listbox()
        txtNombre.delete(0, tk.END)
        txtEdad.delete(0, tk.END)
        messagebox.showinfo("Agregado", "Empleado agregado correctamente")

    print("Agregar")

def eliminar():
    indice_seleccionado = lstEmpleados.curselection()
    if indice_seleccionado:
        indice = indice_seleccionado[0]
        empleados.pop(indice)
        actualizar_listbox()
    else:
        messagebox.showwarning("Advertencia", "Seleccione un empleado")


def modificar():
    indice = txtIndice.get()
    if indice.isdigit():
        indice = int(indice)
        nombre = txtNombre.get()
        edad = txtEdad.get()
        if nombre and edad.isdigit() and 0 <= indice < len(empleados):
            empleados[indice] = {"nombre": nombre, "edad": int(edad)}
            actualizar_listbox()
            txtNombre.delete(0, tk.END)
            txtEdad.delete(0, tk.END)
            txtIndice.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingrese datos validos")
    else:
        messagebox.showwarning("Advertencia", "Ingrese un indice valido")


def cargar_editar():
    selecionar_index = lstEmpleados.curselection()
    if selecionar_index:
        index = selecionar_index[0]
        empleado = empleados[index]
        txtNombre.delete(0, tk.END)
        txtNombre.insert(tk.END, empleado["nombre"])
        txtEdad.delete(0, tk.END)
        txtEdad.insert(tk.END, empleado["edad"])
        txtIndice.delete(0, tk.END)
        txtIndice.insert(tk.END, index)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un empleado")

def actualizar_listbox():
    lstEmpleados.delete(0, tk.END)
    for indice, empleado in enumerate(empleados):
        lstEmpleados.insert(tk.END, f" {indice + 1} - {empleado['nombre']} - {empleado['edad']} años")

#Interfaz de usuario
ventana_principal = tk.Tk()
ventana_principal.title("CRUD de Empleados")
ventana_principal.config( bg="gray", bd=5,)
ventana_principal.resizable(False, False)

#Etiquetas y campos de entrada
#Nombre
lblNombre = tk.Label(ventana_principal, text="Nombre")
lblNombre.grid(row=0, column=0, padx=5, pady=5)
txtNombre = tk.Entry(ventana_principal)
txtNombre.grid(row=0, column=1, padx=5, pady=5)
#Edad
lblEdad = tk.Label(ventana_principal, text="Edad")
lblEdad.grid(row=1, column=0, padx=5, pady=5)
txtEdad = tk.Entry(ventana_principal)
txtEdad.grid(row=1, column=1, padx=5, pady=5)
#Campo para el indice
lblIndice = tk.Label(ventana_principal, text="Indice")
lblIndice.grid(row=4, column=0, padx=5, pady=5)
txtIndice = tk.Entry(ventana_principal)
txtIndice.grid(row=4, column=1, padx=5, pady=5)

#Botones
btnAgregar = tk.Button(ventana_principal, text="Agregar", command=agregar)
btnAgregar.grid(row=2, column=0, padx=5, pady=5)
btnEliminar = tk.Button(ventana_principal, text="Eliminar", command=eliminar)
btnEliminar.grid(row=2, column=1, padx=5, pady=5)
btnModificar = tk.Button(ventana_principal, text="Modificar", command=modificar)
btnModificar.grid(row=3, column=0, padx=5, pady=5)
btnCargarParaEditar = tk.Button(ventana_principal, text="Cargar para editar", command=cargar_editar)
btnCargarParaEditar.grid(row=3, column=1, padx=5, pady=5)

#ListBox para la lista de empleados
lstEmpleados = tk.Listbox(ventana_principal,  width=40, height=10)
lstEmpleados.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

#Mostrar
ventana_principal.mainloop()