# COmponente filedialog para abrir ficheros
# Para importar el modulo de tkinter en linux mint he tenido que instalar python3-tk con
#   sudo apt-get install python3-tk

import tkinter
# Hay que importar el componente expresamente
from tkinter import filedialog

# Esto nos devuelve el componente raíz del programa
raiz = tkinter.Tk()

raiz.title("Mi programa")

#Creamos un método para abrir un fichero
def abrirfichero():
    #Devuelve el path al fichero
    fichero = filedialog.askopenfile(title='Abrir fichero')
    print(fichero.name)

# Creamos un componente boton para activar el filedialog
button = tkinter.Button(raiz, text='Pulsar para empezar', command=abrirfichero)
button.pack()
raiz.mainloop()