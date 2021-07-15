# El componente entry sirve para la entrada de texto
# Para importar el modulo de tkinter en linux mint he tenido que instalar python3-tk con
#   sudo apt-get install python3-tk

import tkinter

# Esto nos devuelve el componente raíz del programa
raiz = tkinter.Tk()

raiz.title("Mi programa")

#Creamo el componente entry
entrada = tkinter.Entry(raiz)
# Le decimos que nos centre el texto y que muestre * cuando se introduce texto
entrada.config(justify='center', show='*')
entrada.pack()


raiz.mainloop()