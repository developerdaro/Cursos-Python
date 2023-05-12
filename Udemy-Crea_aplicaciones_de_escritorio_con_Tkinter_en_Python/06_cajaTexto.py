import tkinter as tk 
from tkinter import ttk

#as es un alias para llamarlo posteriormente

#Creamos objeto de la clase TK
ventana = tk.Tk()

#Tamaño ancho x alto
ancho=600
alto=500
tamaño=str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)

#titulo
ventana.title('Titulo de la ventana')

icono_chico = tk.PhotoImage(file="icon-16.png")
icono_grande = tk.PhotoImage(file="icon.png")
#El primer argumento es un booleano que indica si ese mismo ícono debe aplicarse a ventanas secundaria
ventana.iconphoto(False, icono_grande, icono_chico)


#Variables
textocaja=tk.StringVar(value='valor por defecto')
textocaja01=tk.StringVar()

#Entrada de texto
entradaTextos01 =ttk.Entry(ventana,width=40,textvariable=textocaja01,justify=tk.LEFT)#Crea un input , left es para posicion de escritura
entradaTextos01.grid(row=2,column=4, padx=20, pady=20, ipadx=10,ipady=10) #Posicion del input, #Margen : padx=20, pady=20, ipadx=10,ipady=10
entradaTextos01.insert(0,'texto por defecto') #Texto por defecto, el cero es la posicion
entradaTextos01.insert(tk.END,'//') # Texto por defecto al final
entradaTextos01.insert(7,'....') #Inserta texto en la posicion del texto 7

#Otras ´propiedades entry
entradaTextos02=tk.Entry(ventana,width=40,justify=tk.RIGHT,show='*') #El asterisco es para que muestr en pantalla como si fuera contraseña
entradaTextos02.grid(row=3,column=4,padx=20, pady=20, ipadx=10,ipady=10) #Margen : padx=20, pady=20, ipadx=10,ipady=10

entradaTextos02.config(state='readonly') #solo lectura, campo deshabilitado
entradaTextos02.config(state=tk.DISABLED) #solo lectura, campo deshabilitado

#funcion
def pulsar():
    print(entradaTextos01.get()) #Para imprimir el texto que este en el input
    boton01.config(text=entradaTextos01.get()) #renombramos el boton a lo que tengamos en el input
    entradaTextos01.delete(0,tk.END) #Borramos el input desde la posicion0 hasta el final
    entradaTextos01.focus() #Foco en el input


def cambiar():
    boton02.config(text=textocaja.get()) #Cambia al nombre de la variable
    textocaja01.set('cambiando texto por el de variable')#set es para enviar datos al input
    entradaTextos02.insert(0,textocaja)
    
entradaTextos03=tk.Entry(ventana,width=40, textvariable=textocaja, justify=tk.LEFT ) #textvariable para dar el valor de la variable
entradaTextos03.grid(row=4,column=4,padx=20, pady=20, ipadx=10,ipady=10) #Margen : padx=20, pady=20, ipadx=10,ipady=10

#creando boton
boton01=ttk.Button(ventana,text="cambiar",command=pulsar) #command para invocar una funcion
boton01.grid(row=5,column=2,padx=20, pady=20, ipadx=10,ipady=10) #mostrar boton


#creando boton
boton02=ttk.Button(ventana,text="Pulsame",command=cambiar) #command para invocar una funcion,cambiar() se ejecuta cunado crea ael componente y sin ella solo cuando lo pulsemos
boton02.grid(row=5,column=4,padx=20, pady=20, ipadx=10,ipady=10) #mostrar boton

#Poner siempre al final
ventana.mainloop() 