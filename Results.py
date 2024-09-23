import tkinter
import pygame
#
#ventana de resultados


def mostrar_resultados():
    # Global variables
    title_r = ""
    score_r = 0  # puntaje
    principal_result = False  # informacion de si gano o perdio

    if principal_result == False:
        title_r = "perdiste :("
    else:
        title_r = "Ganaste!"

    ventana = tkinter.Tk()
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

    etiqueta = tkinter.Label(inner_frame, text=title_r, font=("", 24))
    etiqueta2 = tkinter.Label(inner_frame, text="Tu puntaje es: " + str(score_r))

    etiqueta2.pack(side=tkinter.BOTTOM)
    etiqueta.pack(side=tkinter.BOTTOM)

    # ejecutar ventana
    ventana.mainloop()
    ventana.after(3000)



