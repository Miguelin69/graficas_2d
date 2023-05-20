from tkinter import *
import random

# variables globales

BASE= 460
ALTURA=220
RADIO=50
# funcion para modificar arco
def modificar_arco(angulo):

    c.itemconfig(arco , extent=angulo)





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

tri = c.create_polygon(BASE/2,ALTURA/2,BASE+20, ALTURA-10, BASE+20,ALTURA-10, fill="red")
# arco
arco = c.create_arc(BASE/2 -RADIO , ALTURA/2-RADIO , BASE/2 + RADIO , ALTURA/2 + RADIO , start=0 , extent=45 , fill="blue")
aspa2 = c.create_arc(BASE/2 -RADIO , ALTURA/2-RADIO , BASE/2 + RADIO , ALTURA/2 + RADIO , start=90 , extent=45 , fill="yellow")
aspa3 = c.create_arc(BASE/2 -RADIO , ALTURA/2-RADIO , BASE/2 + RADIO , ALTURA/2 + RADIO , start=180 , extent=45 , fill="red")
aspa4 = c.create_arc(BASE/2 -RADIO , ALTURA/2-RADIO , BASE/2 + RADIO , ALTURA/2 + RADIO , start=270 , extent=45 , fill="green")





# frame controles
frame_controles= Frame(ventana_principal)
frame_controles.config(bg="green" , width=480 , height=230)
frame_controles.place(x=10 , y=260)
# barra deslizamiento
barra_deslizamiento = Scale(frame_controles , label="Angulo" , from_=0 , to=360 , orient="horizontal" , length=455 ,tickinterval=45 , command=modificar_arco )



barra_deslizamiento.place(x= 10 , y=10)

ventana_principal.mainloop()