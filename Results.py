import tkinter
import pygame
from tkinter import messagebox



#
#ventana de resultados


def mostrar_resultados(resultado,time):
    # Global variables
    title_r = ""
    score_r = 0  # puntaje
    comment = ""
    principal_result = resultado  # informacion de si gano o perdio

    if principal_result == True:
        title_r = "perdiste :("
        score_r = 0
    else:
        title_r = "Ganaste!"
        score_r = 1000

    ventana = tkinter.Tk()
    ventana.title("MEMORANDUM")

    # Bloquea el redimensionamiento en ambos ejes
    ventana.resizable(False, False)
    # define la resolucion
    ventana.geometry("800x600")
    #evaluar tiempo

    print("tu tiempo fue: "+str(time))
    if time > 80:
        score_r = score_r + 2000
        comment = "Apoco si mi todo tieso?"
    if time > 60:
        score_r = score_r + 1000
        comment= "Eres un tryhard!"
    if time > 40 and time < 75:
        score_r = score_r + 800
        comment = "Nada mal mi amigo :)"
    if time > 20 and time < 50:
        score_r = score_r + 100
        comment = "De verdad se te dificulto tanto?"

    # creando un frame para centrar mi texto
    frame = tkinter.Frame(ventana)
    frame.pack(fill="both", expand=True)

    inner_frame = tkinter.Frame(frame, padx=20, pady=20)
    inner_frame.pack(expand=True)
    # _________________________________________________________

    etiqueta = tkinter.Label(inner_frame, text=title_r, font=("", 32))
    etiqueta2 = tkinter.Label(inner_frame, text="Tu puntaje es: " + str(score_r))
    etiqueta3 = tkinter.Label(inner_frame, text=comment)

    etiqueta2.pack(side=tkinter.BOTTOM)
    etiqueta.pack(side=tkinter.BOTTOM)
    etiqueta3.pack(side=tkinter.BOTTOM)
    ventana.after(4000, ventana.destroy)

    # ejecutar ventana
    ventana.mainloop()

