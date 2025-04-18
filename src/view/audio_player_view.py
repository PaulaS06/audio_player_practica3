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

while True:
    show_menu()
    option = int(input("Selecciona una opción: "))

    if option == "1":
        title, artist, duration = data_song()
        song = Song(title, artist, duration)
        player.playlist.add_song(song)
        print(f"Se ha añadido la canción: {song.title} de {song.artist} a la playlist exitosamente")

    elif option == "2": ## REVISAR
        player.play()
        messages = player.simulate_playback()
        for msg in messages:
            print(msg)

    elif option == "3":
        print(player.next_song())
    elif option == "4":
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
        print(player.shuffle())
        print("Modo aleatorio activado")

    elif option == "9":
        ...
    elif option == "10":
        ...

    elif option == "11":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

