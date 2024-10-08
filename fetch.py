import tkinter as tk
import random
from shutil import which

from Results import mostrar_resultados
import os

# Funciones globales y variables
time_left = 100 # Tiempo en segundos para la cuenta atrás
def play_game():
    global selected_cards, matches_found, cards, buttons



    def flip_card(i, j):


        button = buttons[i][j]
        if button['text'] == '' and len(selected_cards) < 2:
            button['text'] = cards[i * 4 + j]  # Mostrar la carta
            selected_cards.append((i, j))

            if len(selected_cards) == 2:
                root.after(500, check_match)

    def check_match():
        global selected_cards, matches_found, cards, buttons

        (i1, j1), (i2, j2) = selected_cards
        if cards[i1 * 4 + j1] == cards[i2 * 4 + j2]:
            matches_found += 1
            if matches_found == len(cards) // 2:
                print("¡Has encontrado todos los pares!")
                root.after(500, lambda: [root.destroy(), mostrar_resultados(False,time_left)])


        else:
            # Si no es un par, ocultar las cartas de nuevo
            buttons[i1][j1]['text'] = ''
            buttons[i2][j2]['text'] = ''

        # Reiniciar la selección
        selected_cards = []

    # Inicialización del juego
    root = tk.Tk()
    root.title("MEMORANDUM")

    # Bloquea el redimensionamiento en ambos ejes
    root.resizable(False, False)
    # define la resolucion
    root.geometry("800x600")

    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']  # Lista de cartas

    random.shuffle(cards)  # Barajar las cartas

    buttons = []
    selected_cards = []
    matches_found = 0





    # ___________________________________________________________________________________________________
    def disable_all_buttons():
        for row in buttons:
            for button in row:
                button.config(state='disabled')

    def update_timer():
        global time_left
        if time_left > 0:
            time_left -= 1
            contadorr.config(text=f"Tiempo restante: {time_left}s")
            root.after(1000, update_timer)
        else:
            root.after(500, lambda: [root.destroy(), mostrar_resultados(True,time_left)])

            print("¡Tiempo agotado!")
            disable_all_buttons()  # Llamada a una función para deshabilitar botones





    # ____________________________________________________________________________________________________

    # frame de tiempo
    contadorr = tk.Label(root, text=f"Tiempo restante: {time_left}s", font=("Helvetica", 14))
    contadorr.pack(fill=tk.BOTH)

    # Crear un frame para centrar los botones
    frame = tk.Frame(root)
    frame.pack(expand=True)  # Expande el frame para ocupar todo el espacio disponible
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)



    for i in range(4):
        row = []
        for j in range(4):
            button = tk.Button(frame, text='', bg="#FEFADF", fg="black", font=("Helvetica", 10, "bold"),relief="groove",border=2, width=10, height=5, command=lambda i=i, j=j: flip_card(i, j))
            button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")  # Centramos usando sticky
            row.append(button)
        buttons.append(row)

    # Configurar el frame para que los botones se expandan uniformemente
    for i in range(4):
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(i, weight=1)
    update_timer()  # Iniciar el temporizador
    # Iniciar el bucle principal de la interfaz
    root.mainloop()

#play_game()