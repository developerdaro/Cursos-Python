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

#creando boton
boton=ttk.Button(ventana,text="Pulsame")
boton.pack() #mostrar boton

#Poner siempre al final
ventana.mainloop() 