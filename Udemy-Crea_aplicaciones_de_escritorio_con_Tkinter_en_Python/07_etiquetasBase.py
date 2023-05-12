import tkinter as tk 
from tkinter import ttk,messagebox

#as es un alias para llamarlo posteriormente

#Creamos objeto de la clase TK
ventana = tk.Tk()

#Tamaño ancho x alto
ancho=600
alto=500
tamaño=str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)

#titulo
ventana.title("etiqueta mensaje")

icono_chico = tk.PhotoImage(file="icon-16.png")
icono_grande = tk.PhotoImage(file="icon.png")
#El primer argumento es un booleano que indica si ese mismo ícono debe aplicarse a ventanas secundaria
ventana.iconphoto(False, icono_grande, icono_chico)


#Variables
txtnombre=tk.StringVar()


#Funcion
def clic():
    lblMensaje.config(text=cajaNombre.get())
#Ventana emergente
def mensaje():
    mensaje="Hola "+txtnombre.get()+" Lo has logrado"
    messagebox.showinfo("Mensaje",mensaje)
    
#etiqueta
lblNombre=ttk.Label(ventana,text="Nombre")
lblNombre.grid(row=2,column=1,columnspan=2)

lblMensaje=ttk.Label(ventana,text="Mensaje")
lblMensaje.grid(row=5,column=3,columnspan=2)
#Entrada de texto
cajaNombre =ttk.Entry(ventana,width=20,textvariable=txtnombre,justify=tk.LEFT)#Crea un input , left es para posicion de escritura
cajaNombre.grid(row=2,column=3, padx=5, pady=5, ipadx=5,ipady=5) #Posicion del input, #Margen : padx=20, pady=20, ipadx=10,ipady=10


#creando boton
btnClick=ttk.Button(ventana,text="Pulsame", command=clic) #command para invocar una funcion,cambiar() se ejecuta cunado crea ael componente y sin ella solo cuando lo pulsemos
btnClick.grid(row=3,column=3,padx=15, pady=15, ipadx=5,ipady=5) #mostrar boton

#creando boton
btnMensaje=ttk.Button(ventana,text="mensaje", command=mensaje) #command para invocar una funcion,cambiar() se ejecuta cunado crea ael componente y sin ella solo cuando lo pulsemos
btnMensaje.grid(row=3,column=5,padx=15, pady=15, ipadx=5,ipady=5) #mostrar boton

#Poner siempre al final
ventana.mainloop() 