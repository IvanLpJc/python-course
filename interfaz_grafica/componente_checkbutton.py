# COmponente de verificacion
# Para importar el modulo de tkinter en linux mint he tenido que instalar python3-tk con
#   sudo apt-get install python3-tk

import tkinter

# Esto nos devuelve el componente raíz del programa
raiz = tkinter.Tk()

raiz.title("Mi programa")

def verificar():
    valor = opcion.get()
    print("El check está activado") if valor else print("El check no está activo")

#Creamos la variable opcion en tkinter
opcion = tkinter.IntVar()
# Creamos el componente checkbutton
check = tkinter.Checkbutton(raiz, text='Opcion 1', variable=opcion, onvalue=1, offvalue=0, command=verificar)
check.pack()

raiz.mainloop()