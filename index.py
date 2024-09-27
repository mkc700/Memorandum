
from WelcomWindow import iniciar_ventana
import pygame
# Ejecutar el script 'mi_script.py'

def init():
    iniciar_ventana()


init()

# reproducir canciones


# Inicializar Pygame y su módulo mixer
pygame.mixer.init()

# Lista de reproducción de canciones (archivos .mp3 o .wav)
playlist = ["whispering.mp3", "cards.mp3"]


# Función para reproducir una canción
def reproducir_cancion(indice):
    # Cargar y reproducir la canción del índice actual
    pygame.mixer.music.load(playlist[indice])
    pygame.mixer.music.play()
    pygame.mixer.play(loops=-1)

    # Configurar un evento que ocurra cuando la canción termine
    pygame.mixer.music.set_endevent(pygame.USEREVENT)


# Índice de la canción actual
indice_cancion = 1
reproducir_cancion(indice_cancion)

# Bucle principal para detectar cuando termina una canción
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.USEREVENT:
            # Incrementar el índice para la siguiente canción
            indice_cancion = (indice_cancion + 1) % len(playlist)

            # Reproducir la siguiente canción (o volver a la primera si estamos al final)
            reproducir_cancion(indice_cancion)






