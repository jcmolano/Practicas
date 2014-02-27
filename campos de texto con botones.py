from tkinter import *
ventana=Tk()
ventana.geometry("500x300+100+100")
ventana.title("Formulario de Practicas")
lblUsuario=Label(text="Usuario:",font=("Arial",14)).place(x=10,y=10)
#creando un campo de texto para Usuario
entradaU=StringVar()
#entradaU.set("Solo Numeros")
txtUsuario=Entry(ventana,textvariable=entradaU).place(x=80,y=20)
lblNombre=Label(text="Nombre:",font=("Arial",14)).place(x=10,y=50)
#creando campo de texto para nombre
entradaN=StringVar()
#entradaN.set("Solo letras")
txtNOmbre=Entry(ventana,textvariable=entradaN, width=20).place(x=80,y=70)
#crer botones
bntSaludar=Button(ventana,text="Saludar",font=("Arial",14),width=10).place(x=300,y=20)
bntDespedir=Button(ventana,text="Despedir",font=("Arial",14),width=10).place(x=300,y=70)
ventana.mainloop()
