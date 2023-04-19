#Se importan las librerias
from tkinter import *

#Se importan los modulos
from tkinter import ttk #widgets tematicos
import math 

#Se crea la ventana tkinter
root = Tk()
root.title("Calculadora")
root.geometry("+500+80")

#Se crea el frame
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

