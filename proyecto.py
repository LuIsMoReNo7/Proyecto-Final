import tkinter as tk
from tkinter import messagebox

class Formulario(tk.Frame):
    def __init__(self,vp=None):
        #Heredar las caracteristicas de la clase base de tkinter
        super().__init__(vp)
        vp.title("SISTEMA DE REGISTRO DE PEDIDOS")
        vp.geometry("600x600")
        
        self.lbl0=tk.Label(vp,text="FERRETERIA EL TORINILLO FELIZ:")#Etiqueta
        self.lbl0.grid(column=2,row=1,padx=8,pady=11)