import tkinter as tk
from tkinter import messagebox

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
        
        self.lbl3=tk.Label(vp,text="Apellidos:")#Etiqueta
        self.lbl3.grid(column=0,row=3,padx=8,pady=11)
        
        self.txtn3=tk.Entry(vp,width=20)
        self.txtn3.grid(column=1,row=3)

        self.lbl4=tk.Label(vp,text="Dirección:")#Etiqueta
        self.lbl4.grid(column=0,row=4,padx=8,pady=11)        
       
        self.txtn4=tk.Entry(vp,width=20)
        self.txtn4.grid(column=1,row=4)
        
        self.lbl5=tk.Label(vp,text="Telefono:")#Etiqueta
        self.lbl5.grid(column=0,row=5,padx=8,pady=11)        
       
        self.txtn5=tk.Entry(vp,width=20)
        self.txtn5.grid(column=1,row=5)
        
        self.lbl6=tk.Label(vp,text="Cod_prod:")#Etiqueta
        self.lbl6.grid(column=0,row=6,padx=8,pady=11)        
       
        self.txtn6=tk.Entry(vp,width=20)
        self.txtn6.grid(column=1,row=6)
        
        self.lbl7=tk.Label(vp,text="Descripcion:")#Etiqueta
        self.lbl7.grid(column=0,row=7,padx=8,pady=11)        
       
        self.txtn7=tk.Entry(vp,width=20)
        self.txtn7.grid(column=1,row=7)
        
        self.lbl8=tk.Label(vp,text="Unidad:")#Etiqueta
        self.lbl8.grid(column=0,row=8,padx=8,pady=11)        
       
        self.txtn8=tk.Entry(vp,width=20)
        self.txtn8.grid(column=1,row=8)
        
        self.lbl9=tk.Label(vp,text="Cantidad:")#Etiqueta
        self.lbl9.grid(column=2,row=6,padx=8,pady=11)        
       
        self.txtn9=tk.Entry(vp,width=20)
        self.txtn9.grid(column=3,row=6)
        
        self.lbl10=tk.Label(vp,text="Precio:")#Etiqueta
        self.lbl10.grid(column=2,row=7,padx=8,pady=11)        
       
        self.txtn10=tk.Entry(vp,width=20)
        self.txtn10.grid(column=3,row=7)
        
        self.lbl11=tk.Label(vp,text="Subtotal:")#Etiqueta
        self.lbl11.grid(column=2,row=8,padx=8,pady=11)        
       
        self.txtn11=tk.Entry(vp,width=20)
        self.txtn11.grid(column=3,row=8)
        
        self.lbl12=tk.Label(vp,text="Total:")#Etiqueta
        self.lbl12.grid(column=2,row=9,padx=8,pady=11)        
       
        self.txtn12=tk.Entry(vp,width=20)
        self.txtn12.grid(column=3,row=9)


#creamos un boton para enviar los datos ingresados
        self.btnenviar=tk.Button(vp,text="enviar",width=10)
        self.btnenviar.grid(column=0,row=10)      
        
#creamos boton para la impresion de datos
        self.btnimprimir=tk.Button(vp,text="imprimir",width=10)
        self.btnimprimir.grid(column=1,row=10)
        
        
base=tk.Tk()

frm=Formulario(vp=base)
frm.mainloop()