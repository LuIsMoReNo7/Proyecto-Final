import tkinter as tk
from tkinter import messagebox

class Formulario(tk.Frame):
    def __init__(self,vp=None):
        #Heredar las caracteristicas de la clase base de tkinter
        super().__init__(vp)
        vp.title("SISTEMA DE REGISTRO DE PEDIDOS")
        vp.geometry("600x600")
        
        self.lbl0=tk.Label(vp,text="FERRETERIA EL TORINILLO FELIZ")#Etiqueta
        self.lbl0.grid(column=3,row=1,padx=8,pady=11)
        
        self.lbl1=tk.Label(vp,text="DNI:")#Etiqueta
        self.lbl1.grid(column=0,row=2,padx=8,pady=11)
        
        self.txtn1=tk.Entry(vp,width=20)
        self.txtn1.grid(column=2,row=2)
        
        self.lbl2=tk.Label(vp,text="Nombres:")#Etiqueta
        self.lbl2.grid(column=3,row=3,padx=8,pady=11)
        
        self.txtn2=tk.Entry(vp,width=20)
        self.txtn2.grid(column=4,row=3)
        
        self.lbl3=tk.Label(vp,text="apellidos:")#Etiqueta
        self.lbl3.grid(column=0,row=3,padx=8,pady=11)
        
        self.txtn3=tk.Entry(vp,width=20)
        self.txtn3.grid(column=2,row=3)