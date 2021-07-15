from tkinter import * 

window = Tk()

window.title('Calculadora')
# Establecemos el tamaño
window.geometry('415x600')
# Que el tamaño no sea modificable
window.resizable(False,False)
# Background gris
window.configure(bg='gray')

# Functions
operacion = ""
result = StringVar()

def borrar():
    # Recuperamos las variables definidas anteriormente
    global operacion
    global result
    # Borra lo que hay en la operacion
    operacion = ""
    # Utilizamos delete para borrar desde la posicion 0 al final
    results.delete(0,END)

def click(valor):
    global operacion
    global result
    # Concatenamos lo que ya tenemos con lo nuevo clickado
    operacion = operacion + str(valor)
    # Limpiamos la pantalla
    results.delete(0,END)
    # Insertamos la operacion desde la posicion 0
    results.insert(0, operacion)

def calcular():
    global operacion
    global result
    try:
        result = str(eval(operacion))
    except:
        result = 'ERROR'
    finally:
        operacion = ""
        results.delete(0,END)
        results.insert(0, result)
# Display de los resultados

results = Entry(window, font=('arial',20,'bold'), borderwidth=2)
# Para el posicionamiento utilizamos grid, que divide la ventana en filas y columnas
#   Indicamos la fila y columna inicial (0,0)
#   Indicamos que se estire 3 columnas
#   Indicamos que deje 10px de espacio con el borde de arriba y  5 con el de la izq
results.grid(row=0,column=0, columnspan=3,pady=10, padx=5)

# Boton para reiniciar operacion
reset_button = Button(window, text='AC', width=6,height=1, command=lambda:borrar())
reset_button.grid(row=0,column=3, pady=10, padx=1)

# Botones numericos de la primera fila
# Definimos variables comunes a los botones
width = 6
height = 2

button1 = Button(window, text='1', width=width, height=height, command=lambda:click('1'))
button1.grid(row=1, column=0, pady=5, padx=5)
button2 = Button(window, text='2', width=width, height=height, command=lambda:click('2'))
button2.grid(row=1, column=1, pady=5, padx=5)
button3 = Button(window, text='3', width=width, height=height, command=lambda:click('3'))
button3.grid(row=1, column=2, pady=5, padx=5)
button4 = Button(window, text='4', width=width, height=height, command=lambda:click('4'))
button4.grid(row=1, column=3, pady=5, padx=5)

button5 = Button(window, text='5', width=width, height=height, command=lambda:click('5'))
button5.grid(row=2, column=0, pady=5, padx=5)
button6 = Button(window, text='6', width=width, height=height, command=lambda:click('6'))
button6.grid(row=2, column=1, pady=5, padx=5)
button7 = Button(window, text='7', width=width, height=height, command=lambda:click('7'))
button7.grid(row=2, column=2, pady=5, padx=5)
button8 = Button(window, text='8', width=width, height=height, command=lambda:click('8'))
button8.grid(row=2, column=3, pady=5, padx=5)

button9 = Button(window, text='9', width=width, height=height, command=lambda:click('9'))
button9.grid(row=3, column=0, pady=5, padx=5)
button0 = Button(window, text='0', width=width, height=height, command=lambda:click('0'))
button0.grid(row=3, column=1, pady=5, padx=5)
# Botones para las operaciones

button_dot = Button(window, text='.', width=width, height=height, command=lambda:click('.'))
button_dot.grid(row=3, column=2, pady=5, padx=5)
button_sum = Button(window, text='+', width=width, height=height, command=lambda:click('+'))
button_sum.grid(row=3, column=3, pady=5, padx=5)

button_minus = Button(window, text='-', width=width, height=height, command=lambda:click('-'))
button_minus.grid(row=4, column=0, pady=5, padx=5)
button_product = Button(window, text='*', width=width, height=height, command=lambda:click('*'))
button_product.grid(row=4, column=1, pady=5, padx=5)
button_division = Button(window, text='/', width=width, height=height, command=lambda:click('/'))
button_division.grid(row=4, column=2, pady=5, padx=5)
button_equal = Button(window, text='=', width=width, height=height, command=lambda:calcular())
button_equal.grid(row=4, column=3, pady=5, padx=5)
window.mainloop()
