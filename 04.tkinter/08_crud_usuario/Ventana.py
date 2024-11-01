from tkinter import*
from tkinter import ttk,messagebox
import ttkbootstrap as tb
import sqlite3

class Ventana(tb.Window):
    def __init__(self):
        super().__init__()
        self.ventana_login()


    def eliminar_usuario(self):
        usuario_seleccionado_eliminar=self.tree_lista_usuarios.focus()
        valor_usuario_seleccionado_eliminar=self.tree_lista_usuarios.item(usuario_seleccionado_eliminar,'values')
        
        if valor_usuario_seleccionado_eliminar!='':
           respuesta=messagebox.askquestion('Eliminando Usuario', '¿Esta seguro de eliminar el usuario seleccionado?')       
           if respuesta == 'yes':
                    try:
                        miConexion = sqlite3.connect('./desktop/Venta.db')
                        miCursor = miConexion.cursor()
                        miCursor.execute("DELETE FROM Usuarios WHERE codigo=" + str(valor_usuario_seleccionado_eliminar[0]))
                        miConexion.commit()
                        messagebox.showinfo("Eliminando Usuario", "Registro eliminado correctamente")
                        self.mostrar_usuarios()
                        miConexion.close()

                    except:
                        messagebox.showerror('Eliminando Usuario', 'Usuario eliminado correctamente')
           else:
                    messagebox.showerror('Eliminando Usuario', 'Eliminacion cancelada')


    def modificar_usuarios(self):
        if self.txt_codigo_modificar_usuario.get=="" or self.txt_nombre_modificar_usuario.get() =="" or self.txt_clave_modificar_usuario.get()=="" or self.txt_rol_modificar_usuario.get()=="":
            messagebox.showwarning("Modificar Usuarios", "Algun campo no es valido por favor revise")
            return

        try:
            miConexion = sqlite3.connect('./desktop/Venta.db')
            miCursor = miConexion.cursor()
            
            datos_modificar_usuario = self.txt_nombre_modificar_usuario.get(),self.txt_clave_modificar_usuario.get(),self.txt_rol_modificar_usuario.get()

            miCursor.execute("UPDATE Usuarios SET nombre=?,clave=?,rol=? WHERE codigo="+self.txt_codigo_modificar_usuario.get(), (datos_modificar_usuario))
            messagebox.showinfo('Modificando Usuarios', 'Usuarios Modificando Correctamente')            
            miConexion.commit()
            self.val_mod_usu = self.tree_lista_usuarios.item(self.usuario_seleccionado,text='',values=(self.txt_codigo_modificar_usuario.get(),self.txt_nombre_modificar_usuario.get(), self.txt_clave_modificar_usuario.get(), self.txt_rol_modificar_usuario.get(),))
            self.frame_modificar_usuario.destroy()#Cerramos
            # self.ventana_lista_usuarios() #Cargamos
            
            miConexion.close()

        except Exception as err:
            messagebox.showerror('Modificando Usuarios', err)

    def llenar_entrys_modificar_usuario(self):
        self.txt_codigo_modificar_usuario.delete(0,END)
        self.txt_nombre_modificar_usuario.delete(0,END)
        self.txt_clave_modificar_usuario.delete(0,END)
        self.txt_rol_modificar_usuario.delete(0,END)

        self.txt_codigo_modificar_usuario.insert(0,self.val_mod_usu[0])
        self.txt_codigo_modificar_usuario.config(state='readonly')
        self.txt_nombre_modificar_usuario.insert(0,self.val_mod_usu[1])
        self.txt_clave_modificar_usuario.insert(0,self.val_mod_usu[2])
        self.txt_rol_modificar_usuario.insert(0,self.val_mod_usu[3])
        self.txt_rol_modificar_usuario.config(state='readonly')

    def ventana_modificar_usuario(self):
        self.usuario_seleccionado = self.tree_lista_usuarios.focus()
        self.val_mod_usu=self.tree_lista_usuarios.item(self.usuario_seleccionado,'values')
        
        if self.val_mod_usu!='':
            self.frame_modificar_usuario=Toplevel(self) #Ventana por encima de la lista de usuarios
            self.frame_modificar_usuario.title("Modificar Usuario")#Titulo de la ventana
            self.frame_modificar_usuario.geometry('400x300')
            # self.centrar_ventana_modificar_usuario(400,300)#Tamaño de la ventana
            self.frame_modificar_usuario.resizable(0,0)#Para que no se pueda minimizar y max
            self.frame_modificar_usuario.grab_set()#Para que no permita ninguna accionar

            lblframe_modificar_usuario=LabelFrame(self.frame_modificar_usuario)
            lblframe_modificar_usuario.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)

            lbl_codigo_modificar_usuario=Label(lblframe_modificar_usuario,text='Codigo')
            lbl_codigo_modificar_usuario.grid(row=0,column=0,padx=10,pady=10)
            self.txt_codigo_modificar_usuario=Entry(lblframe_modificar_usuario, width=40)
            self.txt_codigo_modificar_usuario.grid(row=0,column=1,padx=10,pady=10)

            lbl_nombre_modificar_usuario=Label(lblframe_modificar_usuario,text='Nombre')
            lbl_nombre_modificar_usuario.grid(row=1,column=0,padx=10,pady=10)
            self.txt_nombre_modificar_usuario=Entry(lblframe_modificar_usuario, width=40)
            self.txt_nombre_modificar_usuario.grid(row=1,column=1,padx=10,pady=10)

            lbl_clave_modificar_usuario=Label(lblframe_modificar_usuario,text='Clave')
            lbl_clave_modificar_usuario.grid(row=2,column=0,padx=10,pady=10)
            self.txt_clave_modificar_usuario=Entry(lblframe_modificar_usuario, width=40)
            self.txt_clave_modificar_usuario.grid(row=2,column=1,padx=10,pady=10)


            lbl_rol_modificar_usuario=Label(lblframe_modificar_usuario,text='Rol')
            lbl_rol_modificar_usuario.grid(row=3,column=0,padx=10,pady=10)
            self.txt_rol_modificar_usuario=ttk.Combobox(lblframe_modificar_usuario, values=('Administrador','Bodega','Vendedor'), width=38)
            self.txt_rol_modificar_usuario.grid(row=3,column=1,padx=10,pady=10)

            btn_modificar_usuario=ttk.Button(lblframe_modificar_usuario,text='Modificar', width=38, bootstyle='warning', command=self.modificar_usuarios)
            btn_modificar_usuario.grid(row=4,column=1,padx=10,pady=10)
            self.llenar_entrys_modificar_usuario()

            #Llamamos a la funcion del ultimo usuario
            self.txt_nombre_modificar_usuario.focus()

    def buscar_usuarios(self,event):
        try:
            miConexion = sqlite3.connect('./desktop/Venta.db')
            miCursor = miConexion.cursor()
            #Limpiamos treeview
            registros = self.tree_lista_usuarios.get_children()
            
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)

            miCursor.execute("SELECT * FROM Usuarios WHERE nombre LIKE ?", (self.txt_busqueda_usuarios.get()+'%',))
            datos = miCursor.fetchall()
            for row in datos:
                self.tree_lista_usuarios.insert("", 0, text=row[0], values=(row[0], row[1], row[2], row[3]))

            miConexion.commit()
            miConexion.close()

        except:
            messagebox.showerror('Busqueda de usuarios', 'Ocurrio un error al buscar usuarios')
        
    def centrar_ventana_nuevo_usuario(self, ancho, alto):
        ventana_ancho = ancho
        ventana_alto = alto
        pantalla_ancho=self.frame_rigth.winfo_screenwidth()
        pantalla_alto=self.frame_rigth.winfo_screenheight()
        coordenadas_x=int((pantalla_ancho/2) - (ventana_ancho/2))
        coordenadas_y=int((pantalla_alto/2) - (ventana_alto/2))
        self.frame_nuevo_usuario.geometry("{}x{}+{}+{}".format(ventana_ancho,ventana_alto,coordenadas_x,coordenadas_y))
      
    def guardar_usuarios(self):

        if self.txt_codigo_nuevo_usuario.get=="" or self.txt_nombre_nuevo_usuario.get() =="" or self.txt_clave_nuevo_usuario.get()=="" or self.txt_rol_nuevo_usuario.get()=="":
            messagebox.showwarning("Guardando Usuarios", "Algun campo no es valido por favor revise")
            return

        try:
            miConexion = sqlite3.connect('./desktop/Venta.db')
            miCursor = miConexion.cursor()
            
            datos_guardar_usuario = self.txt_codigo_nuevo_usuario.get(),self.txt_nombre_nuevo_usuario.get(),self.txt_clave_nuevo_usuario.get(),self.txt_rol_nuevo_usuario.get()

            miCursor.execute("INSERT INTO Usuarios VALUES(?,?,?,?)", (datos_guardar_usuario))
            messagebox.showinfo('Guardando Usuarios', 'Usuarios Guardado Correctamente')            
            miConexion.commit()
            self.frame_nuevo_usuario.destroy()#Cerramos
            self.ventana_lista_usuarios() #Cargamos
            
            miConexion.close()

        except Exception as err:
            messagebox.showerror('Guardando Usuarios', err)

    def ventana_nuevo_usuario(self):
        self.frame_nuevo_usuario=Toplevel(self) #Ventana por encima de la lista de usuarios
        self.frame_nuevo_usuario.title("Nuevo Usuario")#Titulo de la ventana
        self.centrar_ventana_nuevo_usuario(400,300)#Tamaño de la ventana
        self.frame_nuevo_usuario.resizable(0,0)#Para que no se pueda minimizar y max
        self.frame_nuevo_usuario.grab_set()#Para que no permita ninguna accionar

        lblframe_nuevo_usuario=LabelFrame(self.frame_nuevo_usuario)
        lblframe_nuevo_usuario.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)

        lbl_codigo_nuevo_usuario=Label(lblframe_nuevo_usuario,text='Codigo')
        lbl_codigo_nuevo_usuario.grid(row=0,column=0,padx=10,pady=10)
        self.txt_codigo_nuevo_usuario=Entry(lblframe_nuevo_usuario, width=40)
        self.txt_codigo_nuevo_usuario.grid(row=0,column=1,padx=10,pady=10)

        lbl_nombre_nuevo_usuario=Label(lblframe_nuevo_usuario,text='Nombre')
        lbl_nombre_nuevo_usuario.grid(row=1,column=0,padx=10,pady=10)
        self.txt_nombre_nuevo_usuario=Entry(lblframe_nuevo_usuario, width=40)
        self.txt_nombre_nuevo_usuario.grid(row=1,column=1,padx=10,pady=10)

        lbl_clave_nuevo_usuario=Label(lblframe_nuevo_usuario,text='Clave')
        lbl_clave_nuevo_usuario.grid(row=2,column=0,padx=10,pady=10)
        self.txt_clave_nuevo_usuario=Entry(lblframe_nuevo_usuario, width=40)
        self.txt_clave_nuevo_usuario.grid(row=2,column=1,padx=10,pady=10)


        lbl_rol_nuevo_usuario=Label(lblframe_nuevo_usuario,text='Rol')
        lbl_rol_nuevo_usuario.grid(row=3,column=0,padx=10,pady=10)
        self.txt_rol_nuevo_usuario=ttk.Combobox(lblframe_nuevo_usuario, values=('Administrador','Bodega','Vendedor'), width=38, state='readonly')
        self.txt_rol_nuevo_usuario.grid(row=3,column=1,padx=10,pady=10)
        self.txt_rol_nuevo_usuario.current(0)

        btn_guardar_nuevo_usuario=ttk.Button(lblframe_nuevo_usuario,text='Guardar', width=38,command=self.guardar_usuarios)
        btn_guardar_nuevo_usuario.grid(row=4,column=1,padx=10,pady=10)

        #Llamamos a la funcion del ultimo usuario
        self.ultimo_usuario()

    def mostrar_usuarios(self):
        try:
            miConexion = sqlite3.connect('./desktop/Venta.db')
            miCursor = miConexion.cursor()
            #Limpiamos treeview
            registros = self.tree_lista_usuarios.get_children()
            
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)

            miCursor.execute("SELECT * FROM Usuarios")
            datos = miCursor.fetchall()
            for row in datos:
                self.tree_lista_usuarios.insert("", 0, text=row[0], values=(row[0], row[1], row[2], row[3]))

            miConexion.commit()
            miConexion.close()

        except:
            messagebox.showerror('Lista de Usuarios', 'Ocurrio un error al mostrar usuarios')

    def ventana_lista_usuarios(self):
        self.frame_lista_usuarios = Frame(self.frame_center)
        self.frame_lista_usuarios.grid(row=0,column=0,columnspan=2,sticky=NSEW)

        self.lblframe_botones_listausu = LabelFrame(self.frame_lista_usuarios)
        self.lblframe_botones_listausu.grid(row=0,column=0,padx=10, pady=10, sticky=NSEW)

        btn_nuevo_usuario = tb.Button(self.lblframe_botones_listausu,text='Nuevo', width=15,bootstyle="success"
                                      ,command=self.ventana_nuevo_usuario)
        btn_nuevo_usuario.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_usuario = tb.Button(self.lblframe_botones_listausu,text='Modificar', width=15,bootstyle="warning", command=self.ventana_modificar_usuario)
        btn_modificar_usuario.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_usuario = tb.Button(self.lblframe_botones_listausu,text='Eliminar', width=15,bootstyle="danger", command=self.eliminar_usuario)
        btn_eliminar_usuario.grid(row=0,column=2,padx=5,pady=5)

        self.lblframe_busqueda_listausu = LabelFrame(self.frame_lista_usuarios)
        self.lblframe_busqueda_listausu.grid(row=1, padx=10, pady=10, column=0,sticky=NSEW)

        self.txt_busqueda_usuarios = ttk.Entry(self.lblframe_busqueda_listausu,width=95)
        self.txt_busqueda_usuarios.grid(row=0,column=0,padx=5,pady=5)
        self.txt_busqueda_usuarios.bind('<Key>',self.buscar_usuarios)


        #============Treeview===============================
        self.lblframe_tree_listausu = LabelFrame(self.frame_lista_usuarios)
        self.lblframe_tree_listausu.grid(row=2,column=0,padx=10, pady=10,sticky=NSEW)
        columnas = ('codigo', 'nombre', 'clave', 'rol')
        
        self.tree_lista_usuarios = tb.Treeview(self.lblframe_tree_listausu, columns=columnas
                                           , height=17, show='headings', bootstyle='dark')
        self.tree_lista_usuarios.grid(row=0,column=0)

        self.tree_lista_usuarios.heading("codigo", text="Codigo", anchor=W)
        self.tree_lista_usuarios.heading("nombre", text="Nombre", anchor=W)
        self.tree_lista_usuarios.heading("clave", text="Clave", anchor=W)
        self.tree_lista_usuarios.heading("rol", text="Rol", anchor=W)
        self.tree_lista_usuarios['displaycolumns'] = ('codigo','nombre', 'rol')

        #Cerrar el scrolbar
        tree_scroll_listausu=tb.Scrollbar(self.frame_lista_usuarios, bootstyle='round-success')
        tree_scroll_listausu.grid(row=2,column=1)
        #Configurar el scrolbar
        tree_scroll_listausu.config(command=self.tree_lista_usuarios.yview)

        #LLamamos a nuestra funcion mostrar usuarios
        self.mostrar_usuarios()

    def ventana_menu(self):

        self.frame_left = Frame(self, width=200)
        self.frame_left.grid(row=0,column=0,sticky=NSEW)
        self.frame_center = Frame(self)
        self.frame_center.grid(row=0,column=1,sticky=NSEW)
        self.frame_rigth=Frame(self, width=400)
        self.frame_rigth.grid(row=0,column=2,sticky=NSEW)

        btn_productos=ttk.Button(self.frame_left,text='Productos', width=15)
        btn_productos.grid(row=0,column=0,padx=10,pady=10)
        btn_ventas=ttk.Button(self.frame_left,text='Ventas', width=15)
        btn_ventas.grid(row=1,column=0,padx=10,pady=10)
        btn_clientes=ttk.Button(self.frame_left,text='Clientes', width=15)
        btn_clientes.grid(row=2,column=0,padx=10,pady=10)
        btn_compras=ttk.Button(self.frame_left,text='Compras', width=15)
        btn_compras.grid(row=3,column=0,padx=10,pady=10)
        btn_usuarios=ttk.Button(self.frame_left,text='Usuarios', width=15, command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=4,column=0,padx=10,pady=10)
        btn_reportes=ttk.Button(self.frame_left,text='Reportes', width=15)
        btn_reportes.grid(row=5,column=0,padx=10,pady=10)
        btn_backup=ttk.Button(self.frame_left,text='Backup', width=15)
        btn_backup.grid(row=6,column=0,padx=10,pady=10)      
        btn_restaurarbd=ttk.Button(self.frame_left,text='Restarurar DB', width=15)
        btn_restaurarbd.grid(row=7,column=0,padx=10,pady=10)   

        lbl2=Label(self.frame_center,text='Aqui pondremos las ventanas para la venta')
        lbl2.grid(row=0,column=0,padx=10,pady=10)

        lbl3=Label(self.frame_rigth,text='Aqui podremos las busquedas para la venta')
        lbl3.grid(row=0,column=0,padx=10,pady=10)

    def logueo(self):
         
        try:
            miConexion = sqlite3.connect('./desktop/Venta.db')
            miCursor = miConexion.cursor()

            nombre_usuario=self.txt_usuario.get()
            clave_usuario=self.txt_clave.get()

            miCursor.execute("SELECT * FROM Usuarios WHERE nombre=? AND clave=?", (nombre_usuario,clave_usuario))
            datos_logueo = miCursor.fetchall()
            if datos_logueo!="":
                for row in datos_logueo:
                    cod_usu=row[0]
                    nom_usu=row[1]
                    cla_usu=row[2]
                    rol_usu=row[3]
                if(nom_usu==self.txt_usuario.get() and cla_usu==self.txt_clave.get()):
                    self.frame_login.pack_forget() #Aqui ocultamos la ventana login
                    self.ventana_menu()#Aqui abrimos nuestra ventana menu

            
            
            miConexion.commit()
            miConexion.close()

        except:
            messagebox.showerror('Acceso', 'El usuario o clave son incorrectos!')

    def ventana_login(self):
        self.frame_login = Frame(self)
        self.frame_login.pack()
        self.lblframe_login = LabelFrame(self.frame_login, text="Acceso")  
        self.lblframe_login.pack(padx=10, pady=30)

        lbltitulo = ttk.Label(self.lblframe_login, text="Inicio de sesion", font=('Arial', 18))
        lbltitulo.pack(padx=10,pady=10)

        self.txt_usuario = ttk.Entry(self.lblframe_login, width=40, justify=CENTER)
        self.txt_usuario.pack(padx=10,pady=10)
        self.txt_clave = ttk.Entry(self.lblframe_login,width=40,justify=CENTER)
        self.txt_clave.pack(padx=10, pady=10)
        self.txt_clave.configure(show='*')
        btn_acceso = ttk.Button(self.lblframe_login,text='LogIn',command=self.logueo, width=38)
        btn_acceso.pack(padx=10,pady=10)

    def ultimo_usuario(self):
        try:
            miConexion = sqlite3.connect('./desktop/Venta.db')
            miCursor = miConexion.cursor()

            miCursor.execute("SELECT MAX(codigo) FROM Usuarios")
            datos = miCursor.fetchone()
            for codusu in datos:
                if codusu==None:
                    self.ultusu=(int(1))
                    self.txt_codigo_nuevo_usuario.config(state=NORMAL)
                    self.txt_codigo_nuevo_usuario.insert(0,self.ultusu)
                    self.txt_codigo_nuevo_usuario.config(state='readonly')
                    break
                if codusu=="":
                    self.ultusu=(int(1))
                    self.txt_codigo_nuevo_usuario.config(state=NORMAL)
                    self.txt_codigo_nuevo_usuario.insert(0,self.ultusu)
                    self.txt_codigo_nuevo_usuario.config(state='readonly')
                    break
                else:
                    self.ultusu=(int(codusu)+1)
                    self.txt_codigo_nuevo_usuario.config(state=NORMAL)
                    self.txt_codigo_nuevo_usuario.insert(0,self.ultusu)
                    self.txt_codigo_nuevo_usuario.config(state='readonly')
                    break

    
            miConexion.commit()
            miConexion.close()

        except:
            messagebox.showerror('Lista de Usuarios', 'Ocurrio un error al mostrar usuarios')

        
        


def main():
    app=Ventana()
    app.title('Sistema de Ventas')
    app.state('zoomed')
    tb.Style('superhero')
    app.mainloop()

if __name__ == '__main__':
    main()