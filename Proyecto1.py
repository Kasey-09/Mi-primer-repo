from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from random import *
from tkinter import messagebox
from CTkMenuBar import *


#----apariencia de la interfáz-----
set_appearance_mode('dark')
set_default_color_theme('green')

#-----creando interfaz-----

def juego():
    root = CTk()
    root.geometry('800x600+300+100')
    root.resizable(False,False)
    root.title('Piedra Papel O Tijeras')

    #----frames---
    frame1 = CTkFrame(root,corner_radius=20,width=380,height=560,fg_color='blue')
    frame2 = CTkFrame(root,corner_radius=20,width=380,height=560,fg_color='red')
    frame1.place(relx=0.02,rely=0.03)
    frame2.place(relx=0.5,rely=0.03)

    #-----imagenes------
    def piedra():
    
        img1 = CTkImage(dark_image=Image.open('imagenes/piedra.png'),size=(300,300))
        mostrar_img1 = CTkLabel(frame1,image=img1,text='').place(relx=0.1,rely=0.15)
        

    def papel():
        img2 = CTkImage(dark_image=Image.open('imagenes/papel.png'),size=(300,300))
        mostrar_img1 = CTkLabel(frame1,image=img2,text='').place(relx=0.1,rely=0.15)

    def tijeras():
        img3 = CTkImage(dark_image=Image.open('imagenes/tijeras.png'),size=(300,300))
        mostrar_img1 = CTkLabel(frame1,image=img3,text='').place(relx=0.1,rely=0.15)


    #-----etiquetas----
    label1 = CTkLabel(frame1,text='PLAYER',bg_color='blue',
                      font=('Impact',50,'bold')).place(relx=0.32,rely=0.01)

    label2 = CTkLabel(frame2,text='PC',bg_color='red',
                      font=('Impact',50,'bold')).place(relx=0.45,rely=0.01)
    
    label3 = CTkLabel(root,text='VS',font=('Impact',80,'bold'),
                      bg_color='black').place(relx=0.5,rely=0.5,anchor=CENTER)

    

    

    
        

    #------Resultados------

    def resultado(player):
        elecciones = [1,2,3]
    
        

        pc = choice(elecciones)

        if player == 1:
            piedra()

        elif player == 2:
            papel()
        
        else:
            tijeras()

        if pc == 1:
            img1 = CTkImage(dark_image=Image.open('imagenes/piedra.png'),size=(300,300))
            mostrar_img1 = CTkLabel(frame2,image=img1,text='').place(relx=0.15,rely=0.15)

        elif pc == 2:
            img2 = CTkImage(dark_image=Image.open('imagenes/papel.png'),size=(300,300))
            mostrar_img1 = CTkLabel(frame2,image=img2,text='').place(relx=0.15,rely=0.15)
        
        else:
            img3 = CTkImage(dark_image=Image.open('imagenes/tijeras.png'),size=(300,300))
            mostrar_img1 = CTkLabel(frame2,image=img3,text='').place(relx=0.15,rely=0.15)

        #-----resultados-------

        if pc == player:
            resul= '¡EMPATE!'

        elif (player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
            resul = 'PLAYER GANA'
        
        elif (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
            resul = 'PC GANA'
        
        #-----label para mostrar resultados--------
        
        label4 = CTkLabel(root,text=resul,corner_radius=20,text_color='black',width=250,bg_color='white',
                         height=50,font=('Yamaka',40,'bold')).place(relx=0.50,rely=0.76,anchor=CENTER)

            
        
    #-------botones--------

    btn1 = CTkButton(frame1,text='PIEDRA',fg_color='#732425',hover_color='#3C2424',
                    font=('Impact',30),corner_radius=20,
                    width=80,command=lambda:resultado(1)).place(relx = 0.02,rely=0.9)

    btn2 = CTkButton(frame1,text='PAPEL',fg_color='#B8812D',hover_color='#8B6730',
                    font=('Impact',30),corner_radius=20,
                    width=100,command=lambda:resultado(2)).place(relx = 0.35,rely=0.9)

    btn3 = CTkButton(frame1,text='TIJERA',fg_color='#91A03F',hover_color='#6A7534',
                    font=('Impact',30),corner_radius=20,
                    width=100,command=lambda:resultado(3)).place(relx = 0.65,rely=0.9)


    

    #-------Menu de opciones------

    def info():
        messagebox.showinfo(title='Creador',message='El creador de este juego fué un ambicioso a la programación, y lo sigue siendo, sigue aprendiendo por su cuenta.\nfue creado un 10 de julio del año 2024.')

    def mensaje_1():
        messagebox.showinfo(title='¿Como jugar?',message='Si no sabeis jugar salite de aquí.')
    
    
    menu = CTkTitleMenu(root,x_offset=50)
    boton1 = menu.add_cascade("Ayuda",hover_color='#3C2428',font=('Arial',15))
    opcion1 = CustomDropdownMenu(widget=boton1)
    opcion1.add_option(option='Creador',command=lambda:info())
    opcion1.add_separator()
    opcion1.add_option('Ayuda',command=lambda:mensaje_1())


 
    

    
    root.mainloop()









if __name__ == '__main__':
    juego()

    
    
