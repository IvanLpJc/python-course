# COmponente de  seleccion multiple
# Para importar el modulo de tkinter en linux mint he tenido que instalar python3-tk con
#   sudo apt-get install python3-tk

import tkinter

# Esto nos devuelve el componente raíz del programa
raiz = tkinter.Tk()

raiz.title("Mi programa")

def seleccionar():
    print("La opcion seleccionada es {}".format(opcion.get()))

#Creamos la variable opcion en tkinter
opcion = tkinter.IntVar()
# Creamos el componente radiobutton
radiobutton = tkinter.Radiobutton(raiz, text='Opcion 1', variable=opcion, value=1, command=seleccionar)
radiobutton.pack()

radiobutton2 = tkinter.Radiobutton(raiz, text='Opcion 2', variable=opcion, value=2, command=seleccionar)
radiobutton2.pack()

radiobutton3 = tkinter.Radiobutton(raiz, text='Opcion 3', variable=opcion, value=3, command=seleccionar)
radiobutton3.pack()

raiz.mainloop()