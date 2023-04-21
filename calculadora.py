#Se importan las librerias
from tkinter import *

#Se importan los modulos
from tkinter import ttk #widgets tematicos
import math 

#funcion modo oscuro
def temaOscuro(*args):
    estilos.configure('mainframe.TFrame', background="#010924")

    estilosLabel1.configure('Label1.TLabel', background="#010924",foreground="white")
    estilosLabel2.configure('Label2.TLabel', background="#010924",foreground="white")

    estilosBtnNum.configure('BtnNum.TButton',background="#00044A",foreground="white")
    estilosBtnNum.map('BtnNum.TButton', background=[('active', '#020A90')])

    estilosBtnBorrar.configure('BtnBorrar.TButton',background="#010924",foreground="white")
    estilosBtnBorrar.map('BtnBorrar.TButton', background=[('active', '#000AB1')])

    estilosBtn.configure('Btn.TButton', background="#010924",foreground="white")
    estilosBtn.map('Btn.TButton', background=[('active', '#000AB1')])
#funcion modo claro
def temaClaro(*args):
    estilos.configure('mainframe.TFrame', background="#DBDBDB", foreground="black")

    estilosLabel1.configure('Label1.TLabel', background="#DBDBDB",foreground="black")
    estilosLabel2.configure('Label2.TLabel', background="#DBDBDB",foreground="black")

    estilosBtnNum.configure('BtnNum.TButton', background="#FFFFFF", foreground="black")
    estilosBtnNum.map('BtnNum.TButton', background=[('active', '#B9B9B9')])

    estilosBtnBorrar.configure('BtnBorrar.TButton',background="#CECECE",foreground="black")
    estilosBtnBorrar.map('BtnBorrar.TButton', background=[('active', '#858585')])

    estilosBtn.configure('Btn.TButton', background="#CECECE", foreground="black")
    estilosBtn.map('Btn.TButton', background=[('active', '#858585')])
#funcion ingresar valor
def ingresarValores(tecla):
    if tecla >='0' and tecla <='9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')

        entrada2.set('')

    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)
#funcion para ingresar valores desde el teclado    
def ingresarValoresTeclado(event):
    tecla = event.char

    if tecla >='0' and tecla <='9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')

        entrada2.set('')

    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)
#funcion raiz cuadrada
def raizCuadrada():
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)
#funcion borrar de 1 a 1
def borrar(event):
    inicio = 0
    final = len(entrada2.get())

    entrada2.set(entrada2.get()[inicio:final-1])
#funcion borrar todo
def borrarTodo(event):
    entrada1.set('')
    entrada2.set('')
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
button0 = ttk.Button(mainframe,text="0", style="BtnNum.TButton",command=lambda:ingresarValores('0'))
button1 = ttk.Button(mainframe,text="1", style="BtnNum.TButton",command=lambda:ingresarValores('1'))
button2 = ttk.Button(mainframe,text="2", style="BtnNum.TButton",command=lambda:ingresarValores('2'))
button3 = ttk.Button(mainframe,text="3", style="BtnNum.TButton",command=lambda:ingresarValores('3'))
button4 = ttk.Button(mainframe,text="4", style="BtnNum.TButton",command=lambda:ingresarValores('4'))
button5 = ttk.Button(mainframe,text="5", style="BtnNum.TButton",command=lambda:ingresarValores('5'))
button6 = ttk.Button(mainframe,text="6", style="BtnNum.TButton",command=lambda:ingresarValores('6'))
button7 = ttk.Button(mainframe,text="7", style="BtnNum.TButton",command=lambda:ingresarValores('7'))
button8 = ttk.Button(mainframe,text="8", style="BtnNum.TButton",command=lambda:ingresarValores('8'))
button9 = ttk.Button(mainframe,text="9", style="BtnNum.TButton",command=lambda:ingresarValores('9'))

buttonBorrar= ttk.Button(mainframe, text=chr(9003), style="BtnBorrar.TButton",command=lambda:borrar())
buttonBorrarTodo= ttk.Button(mainframe, text="C", style="BtnBorrar.TButton",command=lambda:borrarTodo())
buttonParentesisIzq = ttk.Button(mainframe, text="(", style="Btn.TButton",command=lambda:ingresarValores('('))
buttonParentesisDer = ttk.Button(mainframe, text=")", style="Btn.TButton",command=lambda:ingresarValores(')'))
buttonPunto = ttk.Button(mainframe, text=".", style="Btn.TButton", command=lambda:ingresarValores('.'))

buttonDivision = ttk.Button(mainframe, text=chr(247), style="Btn.TButton",command=lambda:ingresarValores('/'))
buttonMultiplicacion = ttk.Button(mainframe, text="x", style="Btn.TButton",command=lambda:ingresarValores('*'))
buttonResta = ttk.Button(mainframe, text="-", style="Btn.TButton",command=lambda:ingresarValores('-'))
buttonSuma = ttk.Button(mainframe, text="+", style="Btn.TButton",command=lambda:ingresarValores('+'))

buttonIgual = ttk.Button(mainframe, text="=", style="Btn.TButton",command=lambda:ingresarValores('='))
buttonRaizCuadrada = ttk.Button(mainframe, text="√", style="Btn.TButton",command=lambda:raizCuadrada())

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

#evento modo oscuro
root.bind('<KeyPress-o>', temaOscuro)
root.bind('<KeyPress-c>', temaClaro)
root.bind('<Key>', ingresarValoresTeclado)
root.bind('<KeyPress-b>', borrar)
root.bind('<KeyPress-q>', borrarTodo)
root.mainloop()