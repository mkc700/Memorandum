import tkinter
import pygame
#from WelcomWindow import iniciar_ventana
from Tutorial import Crear_ventana_tutorial


#iniciar_ventana()
def Crear_ventana_menu():
    ventanam = tkinter.Tk()  # ventana de menu principal
    #
    # ventana de bienvenida
    #
    # _____________________________________________________

    # Bloquea el redimensionamiento en ambos ejes
    ventanam.resizable(False, False)
    # define la resolucion
    ventanam.geometry("800x600")

    # creando un frame para centrar mi texto
    frame = tkinter.Frame(ventanam)
    frame.pack(fill="both", expand=True)

    inner_frame = tkinter.Frame(frame, padx=20, pady=20)
    inner_frame.pack(expand=True)
    # _________________________________________________________

    etiqueta = tkinter.Label(inner_frame, text="MEMORANDUM", font=("", 24))
    etiqueta2 = tkinter.Button(inner_frame, text="Start", width=15, height=1, bg="gray", fg="white",command=lambda: abrir_ventana(ventanam))

    etiqueta2.pack(side=tkinter.BOTTOM, pady=15)
    etiqueta.pack(side=tkinter.BOTTOM)

    # ejecutar ventana
    ventanam.mainloop()


def abrir_ventana(ventana):
    ventana.destroy()
    Crear_ventana_tutorial()


