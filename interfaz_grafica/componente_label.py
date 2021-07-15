# El componente label sirve para poner etiquetas de texto
# Para importar el modulo de tkinter en linux mint he tenido que instalar python3-tk con
#   sudo apt-get install python3-tk

import tkinter

# Esto nos devuelve el componente raíz del programa
raiz = tkinter.Tk()

raiz.title("Mi programa")

texto = "Hola mundo"

# Tiene dos parámetros, el componente sobre el que montarlo y el contenido
label = tkinter.Label(raiz,text=texto)
label.config(fg="green", bg="lightgray", font=("Cortana",30))
label.pack()
raiz.mainloop()