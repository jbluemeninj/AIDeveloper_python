import tkinter as tk

ventana = tk.Tk()

ventana.title("Demo")
ventana.geometry("400x400")

ventana.maxsize(800, 400)
ventana.minsize(400, 400)
ventana.resizable(True, False)
ventana.config(bg="black")
#ventana.iconbitmap("calculadora.ico")
#ventana.columnconfigure(0, weight=1)
#ventana.columnconfigure(1, weight=1)
#ventana.columnconfigure(2, weight=1)
#ventana.columnconfigure(3, weight=1)
ventana.attributes("-alpha", 0.8)
ventana.mainloop()