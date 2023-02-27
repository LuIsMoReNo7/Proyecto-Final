import tkinter as tk
from tkinter import messagebox

class Formulario(tk.Frame):
    def __init__(self,vp=None):
        #Heredar las caracteristicas de la clase base de tkinter
        super().__init__(vp)
        vp.title("SISTEMA DE REGISTRO DE PEDIDOS")
        vp.geometry("600x400")
        
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


        
base=tk.Tk()

frm=Formulario(vp=base)
frm.mainloop()
        