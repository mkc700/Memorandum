import tkinter
from fetch import play_game


def Crear_ventana_tutorial():
    global etiqueta2
    ventanat = tkinter.Tk()
    ventanat.title("MEMORANDUM")

    # Bloquea el redimensionamiento en ambos ejes
    ventanat.resizable(False, False)
    # define la resolucion
    ventanat.geometry("800x600")



    etiqueta = tkinter.Label(ventanat, text="Tutorial", font=("", 24))
    etiqueta2 = tkinter.Button(ventanat, text="Siguiente instrucción", width=18, height=2, bg="#E0E0C8", fg="black",relief="groove",border=2, command=lambda: contar_clics(ventanat))
    label = tkinter.Label(ventanat, text="¡Este es un juego de cartas!",
                          font=("Arial", 16))


    etiqueta.pack(side=tkinter.TOP)
    etiqueta2.pack(side=tkinter.BOTTOM, padx=5, pady=5)
    label.pack(pady=20)

    # ejecutar ventana
    ventanat.mainloop()
    return etiqueta2

def contar_clics(ventana):
    global contador
    global etiqueta2
    contador += 1
    print(contador)
    if contador == 1:
        label = tkinter.Label(ventana, text="Haz clic en dos recuadros para descubrir las cartas.", font=("Arial", 16))
        label.pack(pady=20)
    if contador == 2:
        label = tkinter.Label(ventana, text="Si las cartas son iguales, ¡las has emparejado!", font=("Arial", 16))
        label.pack(pady=20)
    if contador == 3:
        label = tkinter.Label(ventana, text="Busca todos los pares antes de que se agote el tiempo.", font=("Arial", 16))
        label.pack(pady=20)
    if contador == 4:
        label = tkinter.Label(ventana, text="¡Buena suerte!", font=("Arial", 16))
        label.pack(pady=20)
        etiqueta2.config(text="Iniciar juego")

    if contador == 5:
        print("Hiciste clic 5 veces")
        ventana.destroy()

        # Aquí puedes llamar a la función para abrir la partida
        play_game()





# Inicializa el contador fuera de las funciones
contador = 0
#Crear_ventana_tutorial()
