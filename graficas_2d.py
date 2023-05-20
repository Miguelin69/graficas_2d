from tkinter import *
from tkinter import messagebox , ttk
import random
# variables globales

BASE= 460
ALTURA=220

# ventana principal
ventana_principal = Tk()

ventana_principal.title("graficas 2d - lineas rectas")

ventana_principal.geometry("500x500")

ventana_principal.resizable(0, 0)

ventana_principal.config(bg="white")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green" , width=480 , height=240)
frame_graficacion.place(x=10 , y=10)


# creacion canvas
c = Canvas(frame_graficacion ,width=BASE , height=ALTURA)
c.config(bg="black")
c.place(x=10 , y=10)


# graficacion
color="#ff78ab"
for i in range(100):
    x = random.randint(0 , BASE-20)
    y = random.randint(0 , ALTURA-20)
    color= "#"
    for caracter in range(6):
        color = color + random.choice("0123456789ABCDEF")
    circulo = c.create_oval(x,y,x+20,y+20,fill=color)
    x = x + 30



ventana_principal.mainloop()