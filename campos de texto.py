from tkinter import *
ventana=Tk()
ventana.geometry("1500x1300+100+100")
ventana.title("Formulario de Practicas")
lblDIdentidad=Label(text="D.Identidad:",font=("Arial",14)).place(x=10,y=30)
#creando un campo de texto para Usuario
entradaD=StringVar()
entradaD.set("Solo Numeros")
txtDIdentidad=Entry(ventana,textvariable=entradaD).place(x=120,y=40)
lblNombre=Label(text="Nombre:",font=("Arial",14)).place(x=300,y=30)
#creando campo de texto para nombre
entradaN=StringVar()
entradaN.set("Solo letras")
txtNombre=Entry(ventana,textvariable=entradaN).place(x=380,y=40)
#creando el campo Email
lblEmail=Label(text="Email:",font=("Arial",14)).place(x=550,y=30)
entradaE=StringVar()
entradaE.set("su correo electronico")
txtEmail=Entry(ventana,textvariable=entradaE).place(x=610,y=40)
#creando campo carrera
lblCarrera=Label(text="Carrera:",font=("Arial",14)).place(x=780,y=30)
entradaC=StringVar()
entradaC.set("Su carrera")
txtCarrera=Entry(ventana,textvariable=entradaC).place(x=855,y=40)
#creando campo telefon
lblCarrera=Label(text="Carrera:",font=("Arial",14)).place(x=780,y=30)
entradaC=StringVar()
entradaC.set("Su carrera")
txtCarrera=Entry(ventana,textvariable=entradaC).place(x=855,y=40)
#creando campo empresa donde hace practicas
lblCarrera=Label(text="Carrera:",font=("Arial",14)).place(x=780,y=30)
entradaC=StringVar()
entradaC.set("Su carrera")
txtCarrera=Entry(ventana,textvariable=entradaC).place(x=855,y=40)
#creando campo carrera
lblCarrera=Label(text="Carrera:",font=("Arial",14)).place(x=780,y=30)
entradaC=StringVar()
entradaC.set("Su carrera")
txtCarrera=Entry(ventana,textvariable=entradaC).place(x=855,y=40)
#Botones
bntSaludar=Button(ventana,text="Saludar",font=("Arial",14),width=10).place(x=300,y=20)
bntDespedir=Button(ventana,text="Despedir",font=("Arial",14),width=10).place(x=300,y=70)
ventana.mainloop()
