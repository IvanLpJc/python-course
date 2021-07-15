# COmponente de texto largo con varias lineas a introducir por teclado
# Para importar el modulo de tkinter en linux mint he tenido que instalar python3-tk con
#   sudo apt-get install python3-tk

import tkinter

# Esto nos devuelve el componente raíz del programa
raiz = tkinter.Tk()

raiz.title("Mi programa")

#Creamo el componente entry
texto = tkinter.Text(raiz)
# Le decimos que nos centre el texto y que muestre * cuando se introduce texto
# Configuramos que tenga 20 letras de largo, 10 de alto, fuente verdana de tamaño 15 
# que tenga un espaciado de 10 pixeles en x y en y y que al seleccionar el texto, el 
# color de seleccion sea verde claro
texto.config(width=20, height=10, font=('Verdana',15), padx=10,pady=10,fg='green', selectbackground='lightgreen')
texto.pack()


raiz.mainloop()