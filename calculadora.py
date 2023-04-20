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

entrada1 = StringVar()
labelEntrada1 = ttk.Label(mainframe, textvariable=entrada1)
labelEntrada1.grid(column=0, row=0)

entrada2 = StringVar()
labelEntrada2 = ttk.Label(mainframe, textvariable=entrada2)


#Botones
button0 = ttk.Button(mainframe,text="0")
button1 = ttk.Button(mainframe,text="1")
button2 = ttk.Button(mainframe,text="2")
button3 = ttk.Button(mainframe,text="3")
button4 = ttk.Button(mainframe,text="4")
button5 = ttk.Button(mainframe,text="5")
button6 = ttk.Button(mainframe,text="6")
button7 = ttk.Button(mainframe,text="7")
button8 = ttk.Button(mainframe,text="8")
button9 = ttk.Button(mainframe,text="9")

buttonBorrar= ttk.Button(mainframe, text=chr(9003))
buttonBorrarTodo= ttk.Button(mainframe, text="C")
buttonParentesisIzq = ttk.Button(mainframe, text="(")
buttonParentesisDer = ttk.Button(mainframe, text=")")
buttonPunto = ttk.Button(mainframe, text=".")

buttonDivision = ttk.Button(mainframe, text=chr(247))
buttonMultiplicacion = ttk.Button(mainframe, text="x")
buttonResta = ttk.Button(mainframe, text="-")
buttonSuma = ttk.Button(mainframe, text="+")

buttonIgual = ttk.Button(mainframe, text="=")
buttonRaizCuadrada = ttk.Button(mainframe, text="√")

#Se muestran los botones en pantalla

