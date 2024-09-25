import tkinter
from fetch import play_game



def Crear_ventana_tutorial():
    ventanat = tkinter.Tk()
    # Bloquea el redimensionamiento en ambos ejes
    ventanat.resizable(False, False)
    # define la resolucion
    ventanat.geometry("800x600")

    etiqueta = tkinter.Label(ventanat, text="tutorial", font=("", 24))
    etiqueta2 = tkinter.Button(ventanat, text="Skip", width=15, height=1, bg="gray", fg="white", command=lambda: contar_clics(ventanat))

    etiqueta.pack(side=tkinter.TOP)
    etiqueta2.pack(side=tkinter.BOTTOM, padx=5, pady=5)

    # ejecutar ventana
    ventanat.mainloop()


def contar_clics(ventana):
    global contador
    contador += 1
    print(contador)
    if contador == 1:
        label = tkinter.Label(ventana, text="haz clic en dos recuadros y si no son pares espera a que se oculten", font=("Arial", 16))
        label.pack(pady=20)
    if contador == 2:
        label = tkinter.Label(ventana, text="despues busca otro par y sigue intentando hasta que encuentres pares", font=("Arial", 16))
        label.pack(pady=20)
    if contador == 3:
        label = tkinter.Label(ventana, text="tienes que encontrarlos todos antes de que se acabe el tiempo", font=("Arial", 16))
        label.pack(pady=20)
    if contador == 4:
        label = tkinter.Label(ventana, text="buena suerte!", font=("Arial", 16))
        label.pack(pady=20)

    if contador == 5:
        print("Hiciste clic 5 veces")
        ventana.destroy()
        # Aquí puedes llamar a la función para abrir la partida
        play_game()



# Inicializa el contador fuera de las funciones
contador = 0
#Crear_ventana_tutorial()
