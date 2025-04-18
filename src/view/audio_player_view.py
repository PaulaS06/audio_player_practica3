import time
import sys
sys.path.append("src")
from src.logic.audio_player_logic import AudioPlayer, Song

def data_song():
    print("Introduce los datos de la canción")
    name = input("Título: ")
    artist = input("Artista: ")
    duration = float(input("Duración (en segundos): "))
    return name, artist, duration

def show_menu():
    print("\n=== Bienvenido - Reproductor de música ===")
    print("Ingresa el número de la opción que deseas realizar")
    print("1. Añadir canción a la playlist")
    print("2. Reproducir canción")
    print("3. Avanzar a la siguiente canción")
    print("4. Devolverse a la canción anterior")
    print("5. Eliminar canción por su nombre")
    print("6. Mostrar canción actual")
    print("7. Mostrar playlist")
    print("8. Activar modo aleatorio") # PENDIENTE
    print("9. Adelantar canción") # PENDIENTE
    print("10. Generar una subplaylist") # PENDIENTE
    print("_______________________________\n")
    print("11. Salir")


player = AudioPlayer()
player.playlist.add_song(Song("Song 1", "Artist 1", 3.5))
player.playlist.add_song(Song("Song 2", "Artist 2", 4.0))
player.playlist.add_song(Song("Song 3", "Artist 3", 2.5))
player.playlist.add_song(Song("Song 4", "Artist 4", 5.0))

while True:
    show_menu()
    option = input("Selecciona una opción: ")

    if option == "1":
        title, artist, duration = data_song()
        song = Song(title, artist, duration)
        player.playlist.add_song(song)
        print(f"Se ha añadido la canción: {song.title} de {song.artist} a la playlist exitosamente")

    elif option == "2": ## REVISAR
        print(player.play())
        print(player.simulate_playback())


    elif option == "3":
        if player.playlist.get_size() == 1:
            print("Solo hay una canción en la playlist, se seguirá reproduciendo la misma canción")
        print(player.next_song())

    elif option == "4":
        if player.playlist.get_size() == 1:
            print("Solo hay una canción en la playlist, se seguirá reproduciendo la misma canción")
        print(player.previous_song())

    elif option == "5":
        title = input("Introduce el título de la canción a eliminar: ")
        player.playlist.remove_song(title)
        print(f"Se ha eliminado la canción: {title} de la playlist exitosamente")

    elif option == "6":
        print(player.show_current_song())

    elif option == "7":
        print(player.show_playlist())

    elif option == "8":
        print("Activando modo aleatorio...")
        time.sleep(3)  
        print(player.shuffle())

    elif option == "9":
        ...
    elif option == "10":
        print("La playlist actual tiene las siguientes canciones:")
        print(player.show_playlist())
        titles_ = input("Introduce los títulos de las canciones que quiere agregar en la subplaylist (separados por coma): ")
        titles = titles_.split(", ")
        sub_playlist = player.generate_subplaylist(titles)
        print("Subplaylist generada:")
        print(sub_playlist)

    elif option == "11":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

