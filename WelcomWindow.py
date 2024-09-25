import tkinter
import pygame
from PrincipalMenu import Crear_ventana_menu

def iniciar_ventana():
    #
    # ventana de bienvenida
    #
    ventana = tkinter.Tk()
    ventana.title("desarrollo")
    # Bloquea el redimensionamiento en ambos ejes
    ventana.resizable(False, False)
    # define la resolucion
    ventana.geometry("800x600")

    # creando un frame para centrar mi texto
    frame = tkinter.Frame(ventana)
    frame.pack(fill="both", expand=True)

    inner_frame = tkinter.Frame(frame, padx=20, pady=20)
    inner_frame.pack(expand=True)
    # _________________________________________________________

    etiqueta = tkinter.Label(inner_frame, text="MEMORANDUM", font=("", 24))
    etiqueta2 = tkinter.Label(inner_frame, text="Bienvenido a")

    etiqueta.pack(side=tkinter.BOTTOM)
    etiqueta2.pack(side=tkinter.BOTTOM)

    # Cerrar la ventana después de 3 segundos (3000 milisegundos)

    ventana.after(2000, ventana.destroy)

    #Todavia no agrego el que habra la ventana del menu
    # ventana.after(2000, lambda: [ventana.destroy])}
    # Crear_ventana_menu()

    # ejecutar ventana
    ventana.mainloop()

    Crear_ventana_menu()






