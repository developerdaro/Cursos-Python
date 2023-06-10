import tkinter as tk 
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

#Poner siempre al final
ventana.mainloop() #Para que se ejecute continuamente