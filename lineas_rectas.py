from tkinter import *
from tkinter import messagebox , ttk

# variables globales

BASE= 460
ALTURA=220

# ventana principal
ventana_principal = Tk()

ventana_principal.title("graficas 2d - lineas rectas")

ventana_principal.geometry("500x500")

ventana_principal.resizable(0, 0)

ventana_principal.config(bg="black")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white" , width=480 , height=240)
frame_graficacion.place(x=10 , y=10)


# creacion canvas
c = Canvas(frame_graficacion ,width=BASE , height=ALTURA)
c.config(bg="yellow")
c.place(x=10 , y=10)

# lineas
"""linea1 = c.create_line(10,10, BASE-10 , 10 , fill="red" , width=5)
linea2 = c.create_line(BASE -10,10, BASE-10 , ALTURA-10 , fill="red" , width=5)
linea3 = c.create_line(BASE -10, ALTURA - 10, 10 , ALTURA-10 , fill="red" , width=5)
linea4 = c.create_line(10,ALTURA -10, 10 , 10 , fill="red" ,width=5)
linea5 = c.create_line(10,10, BASE -10 , ALTURA -10 , fill="red")
linea6 = c.create_line(10,ALTURA -10, BASE -10 , 10 , fill="red")



# TEXTO 
texto1 = c.create_text(BASE/2 , ALTURA/2 , text="sistemas uis socorro" , anchor="center" , font=("arial", "20" ) , fill="green" , activefill="white")

# cuadrados y rectangulos
rect1= c.create_rectangle(20,20,120,120 , fill="blue" , outline="pink" , width="3")"""""


# poligonos
#poligono1 = c.create_polygon(BASE-100,ALTURA-10,BASE-10 , ALTURA-60 , BASE-220 , ALTURA-60, fill="red")
#poligono2 = c.create_polygon(BASE/2,3*ALTURA/4,3*BASE/4, ALTURA/2 , BASE-10,3*ALTURA/4, fill="red")

# ovalos-circulo
#elipse1=c.create_oval(BASE/2 -50, ALTURA/2 -50 ,BASE/2 +50, ALTURA/2 +50 ,fill="orange", )
elipse2=c.create_oval(BASE/2 , ALTURA/2 , BASE , ALTURA  ,fill="orange")
elipse1=c.create_oval(3*BASE/4 ,3*ALTURA/4 ,BASE/2,ALTURA/4,fill="orange", )
elipse2=c.create_oval(BASE/4 ,ALTURA/2 ,BASE/2,ALTURA/4,fill="orange", )

# arcos
arc1=c.create_arc( 3*BASE/4 ,3*ALTURA/4 ,BASE/2,ALTURA/4, start=20 , extent=320 , fill="black")






ventana_principal.mainloop()