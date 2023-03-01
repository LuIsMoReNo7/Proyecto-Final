import tkinter as tk


def submit():
                    
         
            
         #obtenemos los valores de las cajas de texto                   
          DNI = DNI_entry.get()
          Nombres = Nombres_entry.get()
          apellidos = apellidos_entry.get()
          Dirección = Dirección_entry.get()
          Telefono = Telefono_entry.get()
          Cod_Prod = Cod_Prod_entry.get()
          Descripcion = Descripcion_entry.get()
          Unidad = Unidad_entry.get()
          Cantidad = Cantidad_entry.get()
          Precio = Precio_entry.get()
          subtotal = subtotal_entry.get()
          Total = Total_entry.get("1.0", tk.end)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
           #imprimimos los valores por consola
                print("DNI :", DNI)
                print("Nombres :", Nombres)
                print("apellidos :", apellidos)
                print("Dirección :", Dirección)
                print("Telefono :", Telefono)
                print("Cod_Prod :", Cod_Prod)
                print("Descripcion :", Descripcion)
                print("Unidad :", Unidad)
                print("Cantidad :", CAntidad)
                print("Precio :", Precio)
                print("Subtotal :", Subtotal)
                print("Total :", Total)


           #limpiamos las cajas de texto
           DNI_entry.delete(0, tk.end)
           Nombres_entry.delete(0, tk.end)
           apellidos_entry.delete(0, tk.end)
           Dirección_entry.delete(0, tk.end)
           Telefono_entry.delete(0, tk.end)
           Cod_Prod_entry.delete(0, tk.end)
           Descripcion_entry.delete(0, tk.end)
           Unidad_entry.delete(0, tk.end)
           Cantidad_entry.delete(0, tk.end)
           Precio_entry.delete(0, tk.end)
           Subtotal_entry.delete(0, tk.end)
           Total_entry.delete(0, tk.end)

class Formulario(tk.Frame):
    def __init__(self,vp=None):
        #Heredar las caracteristicas de la clase base de tkinter
        super().__init__(vp)
        vp.title("SISTEMA DE REGISTRO DE PEDIDOS")
        vp.geometry("600x500")
        
        self.lbl0=tk.Label(vp,text="FERRETERIA EL TORINILLO FELIZ")#Etiqueta
        self.lbl0.grid(column=2,row=1,padx=8,pady=11)
        
        self.lbl1=tk.Label(vp,text="DNI:")#Etiqueta
        self.lbl1.grid(column=0,row=2,padx=8,pady=11)
        
        self.txtn1=tk.Entry(vp,width=20)
        self.txtn1.grid(column=1,row=2)
        
        self.lbl2=tk.Label(vp,text="Nombres:")#Etiqueta
        self.lbl2.grid(column=2,row=3,padx=8,pady=11)
        
        self.txtn2=tk.Entry(vp,width=20)
        self.txtn2.grid(column=3,row=3)
        
        self.lbl3=tk.Label(vp,text="apellidos:")#Etiqueta
        self.lbl3.grid(column=0,row=3,padx=8,pady=11)
        
        self.txtn3=tk.Entry(vp,width=20)
        self.txtn3.grid(column=1,row=3)

        self.lbl4=tk.Label(vp,text="Dirección:")#Etiqueta
        self.lbl4.grid(column=0,row=4,padx=8,pady=11)        
       
        self.txtn4=tk.Entry(vp,width=20)
        self.txtn4.grid(column=1,row=4)
        
        self.lbl4=tk.Label(vp,text="Telefono:")#Etiqueta
        self.lbl4.grid(column=0,row=5,padx=8,pady=11)        
       
        self.txtn5=tk.Entry(vp,width=20)
        self.txtn5.grid(column=1,row=5)
        
        self.lbl6=tk.Label(vp,text="Cod_Prod:")#Etiqueta
        self.lbl6.grid(column=0,row=6,padx=8,pady=11)        
       
        self.txtn6=tk.Entry(vp,width=20)
        self.txtn6.grid(column=1,row=6)
        
        self.lbl6=tk.Label(vp,text="Descripcion:")#Etiqueta
        self.lbl6.grid(column=0,row=7,padx=8,pady=11)        
       
        self.txtn6=tk.Entry(vp,width=20)
        self.txtn6.grid(column=1,row=7)
        
        self.lbl6=tk.Label(vp,text="Unidad:")#Etiqueta
        self.lbl6.grid(column=0,row=8,padx=8,pady=11)        
       
        self.txtn6=tk.Entry(vp,width=20)
        self.txtn6.grid(column=1,row=8)
        
        self.lbl9=tk.Label(vp,text="Cantidad:")#Etiqueta
        self.lbl9.grid(column=2,row=6,padx=8,pady=11)        
       
        self.txtn9=tk.Entry(vp,width=20)
        self.txtn9.grid(column=3,row=6)
        
        self.lbl10=tk.Label(vp,text="Precio:")#Etiqueta
        self.lbl10.grid(column=2,row=7,padx=8,pady=11)        
       
        self.txtn10=tk.Entry(vp,width=20)
        self.txtn10.grid(column=3,row=7)
        
        self.lbl11=tk.Label(vp,text="subtotal:")#Etiqueta
        self.lbl11.grid(column=2,row=8,padx=8,pady=11)        
       
        self.txtn11=tk.Entry(vp,width=20)
        self.txtn11.grid(column=3,row=8)
        
        self.lbl12=tk.Label(vp,text="total:")#Etiqueta
        self.lbl12.grid(column=2,row=9,padx=8,pady=11)        
       
        self.txtn12=tk.Entry(vp,width=20)
        self.txtn12.grid(column=3,row=9)        


#creamos un boton para enviar los datos
        self.btnenviar=tk.Button(vp,text="enviar",width=10)
        self.btn["command"]=self.enviar,command=submit()
        self.btnenviar.grid(column=0,row=10)


#creamos un boton para la impresion de datos
        self.btnimprimir=tk.Button(vp,text="imprimir",width=10)
        self.btn["command"]=self.imprimir,command=submit()
        self.btnimprimir.grid(column=1,row=10)
        




base=tk.Tk()

frm=Formulario(vp=base)
frm.mainloop()