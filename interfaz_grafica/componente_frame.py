# Para importar el modulo de tkinter en linux mint he tenido que instalar python3-tk con
#   sudo apt-get install python3-tk

import tkinter

# Esto nos devuelve el componente raíz del programa
raiz = tkinter.Tk()

raiz.title("Mi programa")

# Es un componente que permite incluir otros componentes en el 
# tenemos que indicarle sobre que componente lo vamos a montar
frame = tkinter.Frame(raiz)

# Podemos modificar sus propiedades
frame.config(bg='blue', width=400,height=300)
# Lo tenemos que empaquetar
frame.pack()


raiz.mainloop()