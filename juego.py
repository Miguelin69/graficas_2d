import tkinter as tk
from tkinter import *
import random
import pygame

BASE= 460
ALTURA=220

def move_up():
    canvas.move(object_id, 0, -10)
    

def move_down():
    canvas.move(object_id, 0, 10)

def move_left():
    canvas.move(object_id, -10, 0)

def move_right():
    canvas.move(object_id, 10, 0)
def reproducir_musica():
    pygame.mixer.music.load("img/musica5.mp3")  # Ruta del archivo de música
    pygame.mixer.music.play()

def detener_musica():
    pygame.mixer.music.stop()
# Crear ventana



ventana_principal = Tk()

ventana_principal.title("graficas 2d - lineas rectas")

ventana_principal.geometry("500x500")

ventana_principal.resizable(0, 0)

ventana_principal.config(bg="gray63")


frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="bisque" , width=480 , height=240)
frame_graficacion.place(x=10 , y=10)


logo = PhotoImage(file="img/logogame1111.png")
lb_logo = Label(ventana_principal, image=logo  , bg="gray")
lb_logo.place(x=150 , y=260 ,width=240 , height=40)

boto = PhotoImage(file="img/boto1234.png")
lb_boto = Label(ventana_principal, image=boto  , bg="gray")
lb_boto.place(x=20 , y=400 ,width=40 , height=40)

boto1 = PhotoImage(file="img/boto1234.png")
lb_boto1 = Label(ventana_principal, image=boto1 , bg="gray")
lb_boto1.place(x=40 , y=350 ,width=40 , height=40)

boto2 = PhotoImage(file="img/ece1.png")
lb_boto2 = Label(ventana_principal, image=boto2 , bg="gray")
lb_boto2.place(x=440 , y=260 ,width=45 , height=33)

# Crear lienzo
canvas = tk.Canvas(frame_graficacion, width=BASE , height=ALTURA)
canvas.pack()
canvas.config(bg="black")
canvas.place(x=10 , y=10)


color="#ff78ab"
for i in range(15):
    x = random.randint(0 , BASE-20)
    y = random.randint(0 , ALTURA-20)
    radius = random.randint(10, 30)

        # Dibuja el círculo en el lienzo
    
    color= "#"
    for caracter in range(6):
        color = color + random.choice("0123456789ABCDEF")
    circulo= canvas.create_oval(x , y , x + radius, y + radius, fill=color)
    x = x + 30


# Cargar imágenes de flechas
arrow_up = PhotoImage(file=("img/flechas4.png"))
arrow_down = PhotoImage(file=("img/flechas2.png"))
arrow_left = PhotoImage(file=("img/flechas1.png"))
arrow_right = PhotoImage(file=("img/flechas3.png"))



# Crear botones de flechas
btn_up = tk.Button(ventana_principal, image=arrow_up, command=move_up)
btn_up.config(bg="gray63")
btn_up.place(x=230 , y=320 , width=70 , height=70)

btn_down = tk.Button(ventana_principal, image=arrow_down, command=move_down)
btn_down.config(bg="gray63")
btn_down.place(x=230 , y=420 , width=70 , height=70)

btn_left = tk.Button(ventana_principal, image=arrow_left, command=move_left)
btn_left.config(bg="gray63")
btn_left.place(x=150 , y=375 , width=70 , height=70)

btn_right = tk.Button(ventana_principal, image=arrow_right, command=move_right)
btn_right.config(bg="gray63")
btn_right.place(x=310 , y=375 , width=70 , height=70)

pygame.mixer.init()

# Crear botones para reproducir y detener la música
btn_reporr = tk.Button(ventana_principal, image=boto, command=reproducir_musica)
btn_reporr.config(bg="gray63")
btn_reporr.place(x=20 , y=400 , width=40 , height=40)




boton_detener = tk.Button(ventana_principal, image=boto1, command=detener_musica)
boton_detener.config(bg="gray63")
boton_detener.place(x=40 , y=350 , width=40 , height=40)



# Crear objeto en el lienzo

nave = PhotoImage(file="img/nave1.png" , width=50)
object_id = canvas.create_image(200, 200, image=nave)

# Ejecutar la ventana
ventana_principal.mainloop()


