import tkinter as tk 
from tkinter import ttk

#as es un alias para llamarlo posteriormente

#Creamos objeto de la clase TK
ventana = tk.Tk()

#Tamaño ancho x alto
ancho=600
alto=400
tamaño=str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)

#titulo
ventana.title('Titulo de la ventana')

icono_chico = tk.PhotoImage(file="icon-16.png")
icono_grande = tk.PhotoImage(file="icon.png")
#El primer argumento es un booleano que indica si ese mismo ícono debe aplicarse a ventanas secundaria
ventana.iconphoto(False, icono_grande, icono_chico)

def click2():
    print("Has pulsado el boton 01")
    boton02.config(text="Cambiando el nombre al boton 02")

def click():
    print("Me han pulsado")
    boton01.config(text="has pulsado el boton 02")

#creando boton
boton01=ttk.Button(ventana,text="Pulsame",command=click2)
boton01.pack() #mostrar boton

boton02=ttk.Button(ventana,text="click",command=click)
boton02.pack()



#Poner siempre al final
ventana.mainloop() 