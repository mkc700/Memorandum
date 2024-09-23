import tkinter
from fetch import play_game
ventanat = tkinter.Tk()
contador = 0


def Crear_ventana_tutorial():

    # Bloquea el redimensionamiento en ambos ejes
    ventanat.resizable(False, False)
    # define la resolucion
    ventanat.geometry("800x600")


    etiqueta = tkinter.Label(ventanat, text="tutorial", font=("", 24))
    etiqueta2 = tkinter.Button(ventanat, text="Skip", width=15, height=1, bg="gray", fg="white", command=lambda: contar_clics(contador))

    etiqueta.pack(side=tkinter.TOP)
    etiqueta2.pack(side=tkinter.BOTTOM, padx=5, pady=5)

    # ejecutar ventana
    ventanat.mainloop()

def contar_clics(contador):
    print(contador)

    if contador == 5:

       print("Hiciste clic 5 veces")
       # aqui abro ya la partida
       #
    else:
        contador = + 1

    return contador


