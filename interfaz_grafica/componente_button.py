# COmponente para botones 
# Para importar el modulo de tkinter en linux mint he tenido que instalar python3-tk con
#   sudo apt-get install python3-tk

import tkinter

# Esto nos devuelve el componente raíz del programa
raiz = tkinter.Tk()

raiz.title("Mi programa")

# Tenemos que definir un método a ejecutar por el boton
def accion():
    print("Hola mundo")

#Creamo el componente entry
boton = tkinter.Button(raiz, text='Ejecutar', command=accion)

boton.config(width=10, height=2, font=('Verdana', 15), justify='center', fg='white', bg='black', activebackground='black', activeforeground='white')
boton.pack()

raiz.mainloop()