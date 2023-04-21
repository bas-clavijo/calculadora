#Se importan las librerias
from tkinter import *

#Se importan los modulos
from tkinter import ttk #widgets tematicos
import math 

#Se crea la ventana tkinter
root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Se crea el frame
mainframe = ttk.Frame(root,style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

#Se crean los label de respuesta
entrada1 = StringVar()
labelEntrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
labelEntrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))

entrada2 = StringVar()
labelEntrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
labelEntrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))

#Botones
button0 = ttk.Button(mainframe,text="0", style="BtnNum.TButton")
button1 = ttk.Button(mainframe,text="1", style="BtnNum.TButton")
button2 = ttk.Button(mainframe,text="2", style="BtnNum.TButton")
button3 = ttk.Button(mainframe,text="3", style="BtnNum.TButton")
button4 = ttk.Button(mainframe,text="4", style="BtnNum.TButton")
button5 = ttk.Button(mainframe,text="5", style="BtnNum.TButton")
button6 = ttk.Button(mainframe,text="6", style="BtnNum.TButton")
button7 = ttk.Button(mainframe,text="7", style="BtnNum.TButton")
button8 = ttk.Button(mainframe,text="8", style="BtnNum.TButton")
button9 = ttk.Button(mainframe,text="9", style="BtnNum.TButton")

buttonBorrar= ttk.Button(mainframe, text=chr(9003), style="BtnBorrar.TButton")
buttonBorrarTodo= ttk.Button(mainframe, text="C", style="BtnBorrar.TButton")
buttonParentesisIzq = ttk.Button(mainframe, text="(", style="Btn.TButton")
buttonParentesisDer = ttk.Button(mainframe, text=")", style="Btn.TButton")
buttonPunto = ttk.Button(mainframe, text=".", style="Btn.TButton")

buttonDivision = ttk.Button(mainframe, text=chr(247), style="Btn.TButton")
buttonMultiplicacion = ttk.Button(mainframe, text="x", style="Btn.TButton")
buttonResta = ttk.Button(mainframe, text="-", style="Btn.TButton")
buttonSuma = ttk.Button(mainframe, text="+", style="Btn.TButton")

buttonIgual = ttk.Button(mainframe, text="=", style="Btn.TButton")
buttonRaizCuadrada = ttk.Button(mainframe, text="√", style="Btn.TButton")

#Se muestran los botones en pantalla
buttonParentesisIzq.grid(column=0, row=2, sticky=(W,N,E,S))
buttonParentesisDer.grid(column=1, row=2, sticky=(W,N,E,S))
buttonBorrarTodo.grid(column=2, row=2, sticky=(W,N,E,S))
buttonBorrar.grid(column=3, row=2, sticky=(W,N,E,S))

button7.grid(column=0, row=3, sticky=(W,N,E,S))
button8.grid(column=1, row=3, sticky=(W,N,E,S))
button9.grid(column=2, row=3, sticky=(W,N,E,S))
buttonDivision.grid(column=3, row=3, sticky=(W,N,E,S))

button4.grid(column=0, row=4, sticky=(W,N,E,S))
button5.grid(column=1, row=4, sticky=(W,N,E,S))
button6.grid(column=2, row=4, sticky=(W,N,E,S))
buttonMultiplicacion.grid(column=3, row=4, sticky=(W,N,E,S))

button1.grid(column=0, row=5, sticky=(W,N,E,S))
button2.grid(column=1, row=5, sticky=(W,N,E,S))
button3.grid(column=2, row=5, sticky=(W,N,E,S))
buttonSuma.grid(column=3, row=5, sticky=(W,N,E,S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W,N,E,S))
buttonPunto.grid(column=2, row=6, sticky=(W,N,E,S))
buttonResta.grid(column=3, row=6, sticky=(W,N,E,S))

buttonIgual.grid(column=0, row=7, columnspan=3, sticky=(W,N,E,S))
buttonRaizCuadrada.grid(column=3, row=7, sticky=(W,N,E,S))

#Se agregan los estilos 
estilos = ttk.Style()
estilos.configure('mainframe.TFrame', background="#DBDBDB")
estilos.theme_use('clam')

#estilos label
estilosLabel1 = ttk.Style()
estilosLabel1.configure('Label1.TLabel', font="arial 15", anchor="e")

estilosLabel2 = ttk.Style()
estilosLabel2.configure('Label2.TLabel', font="arial 40", anchor="e")

#estilos botones
estilosBtnNum = ttk.Style()
estilosBtnNum.configure('BtnNum.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")
estilosBtnNum.map('BtnNum.TButton',background=[('active', '#858585')])

estilosBtnBorrar = ttk.Style()
estilosBtnBorrar.configure('BtnBorrar.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")
estilosBtnBorrar.map('BtnBorrar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

estilosBtn = ttk.Style()
estilosBtn.configure('Btn.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")
estilosBtn.map('Btn.TButton',background=[('active', '#858585')])

#funcion para dar espacio a los botones
for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)



root.mainloop()