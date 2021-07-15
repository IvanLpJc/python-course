# COmponente popup para preguntar
# Para importar el modulo de tkinter en linux mint he tenido que instalar python3-tk con
#   sudo apt-get install python3-tk

import tkinter
# Hay que importar el componente expresamente
from tkinter import messagebox

# Esto nos devuelve el componente raíz del programa
raiz = tkinter.Tk()

raiz.title("Mi programa")
def preguntar():
    resultado = messagebox.askquestion('Titulo de la pregunta', '¿Quiere borrar el fichero?')
    print('Sí, quiero borrar el fichero') if resultado else print('No quiero borrar el fichero')

# Creamos un componente boton para activar el popup
button = tkinter.Button(raiz, text='Pulsar para aviso', command=preguntar)
button.pack()
raiz.mainloop()