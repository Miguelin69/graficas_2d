from tkinter import *
from tkinter import messagebox , ttk

ventana_principal = Tk()


ventana_principal.title("Miguel")

ventana_principal.geometry("500x500")

ventana_principal.resizable(0, 0)

ventana_principal.config(bg="white")


ventana_principal.mainloop()


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="lightblue1" , width=480 , height=250)
frame_entrada.place(x=10 , y=10)



