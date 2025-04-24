import time
import sys
sys.path.append("src")
from logic.audio_player_logic import AudioPlayer, Song

def data_song():
    print("🎶 Introduce los datos de la canción 🎶")
    name = input("🎵 Título: ")
    artist = input("🎤 Artista: ")
    duration = float(input("⏱️ Duración (en segundos): "))
    return name, artist, duration

def show_menu():
    print("\n🎼 === Bienvenido - Reproductor de música === 🎼")
    print("📋 Ingresa el número de la opción que deseas realizar")
    print("1. Añadir canción a la playlist desde el principio")
    print("2. Reproducir la primera canción de la playlist")
    print("3. Reproducir canción por su nombre")
    print("4. Avanzar a la siguiente canción ⏭️")
    print("5. Devolverse a la canción anterior ⏮️")
    print("6. Eliminar canción por su nombre ❌")
    print("7. Mostrar canción actual 🎧")
    print("8. Mostrar playlist 📜")
    print("9. Reproducir playlist ▶️")
    print("10.  Activar modo aleatorio 🔀") 
    print("11. Adelantar canción ⏩") # PENDIENTE
    print("12. Generar una subplaylist 🧩") 
    print("20. !!! SUSTENTACION - top 3 canciones que más duran")
    print("_______________________________\n")
    print("13. Salir 🚪")

def ask_playlist():
    print("🎵 ¿Quieres usar la playlist original o una subplaylist?")
    choise = input("Escribe 'p' (playlist original) o 's' (subplaylist): ")
    if choise.lower() == "p":
        return choise
    elif choise.lower() == "s":
        return choise
    else:
        print("⚠️ Opción no válida. Intenta de nuevo.")
        ask_playlist()

player = AudioPlayer()
player.playlist.add_song(Song("Song 1", "Artist 1", 3.5))
player.playlist.add_song(Song("Song 2", "Artist 2", 4.0))
player.playlist.add_song(Song("Song 3", "Artist 3", 2.5))
player.playlist.add_song(Song("Song 4", "Artist 4", 5.0))

while True:
    input("\nPresiona Enter para mostrar el menú...")
    show_menu()

    if player.sub_playlist is not None:
        choise = ask_playlist() 
        if choise == "p":
            player.current_playlist = player.playlist
        elif choise == "s":
            player.current_playlist = player.sub_playlist
    else:
        print("No hay subplaylist creada, se usará la playlist original")
    
    option = input("Selecciona una opción: ")

    if option == "1":
        title, artist, duration = data_song()
        song = Song(title, artist, duration)
        player.playlist.add_song(song)
        print(f"✅ Se ha añadido la canción: {song.title} de {song.artist} a la playlist 🎶")

    elif option == "2":
        if player.current_playlist.get_size() == 0:
            print("La playlist está vacía, no se puede reproducir ninguna canción")
        else:
            print(player.play_current_song())
            print(player.simulate_playback())

    elif option == "3": 
        song_title = input("Introduce el título de la canción a reproducir: ")
        print(player.play_song(song_title))
        print(player.simulate_playback())


    elif option == "4":
        if player.current_playlist.get_size() == 1:
            print("ℹ️ Solo hay una canción, se seguirá reproduciendo la misma 🎵")
        print(player.next_song())

    elif option == "5":
        if player.current_playlist.get_size() == 1:
            print("ℹ️ Solo hay una canción, se seguirá reproduciendo la misma 🎵")
        print(player.previous_song())

    elif option == "6":
        title = input("Introduce el título de la canción a eliminar: ")
        player.current_playlist.remove_song(title)
        print(f"🗑️ Se ha eliminado la canción: {title} de la playlist")

    elif option == "7":
        print(player.show_current_song())

    elif option == "8":
        print(player.show_playlist())

    elif option == "9":
        print("▶️ Reproduciendo playlist completa...")
        player.play_playlist()
        print("✅ Playlist finalizada")

    elif option == "10":
        print("🔄 Activando modo aleatorio, espera un momento...")
        time.sleep(3)  
        print(player.shuffle())

    elif option == "11":
        try:
            percent = float(input("¿Cuánto porcentaje quieres adelantar? (ej: 25): "))
            result = player.advance_song(percent)
            for msg in result:
                print(msg)
        except ValueError:
            print("⚠️ Porcentaje inválido. Debe ser un número.")

    elif option == "12":
        print("La playlist actual tiene las siguientes canciones:")
        print(player.show_playlist())
        titles_ = input("Introduce los títulos de las canciones que quiere agregar en la subplaylist (separados por coma): ")
        titles = titles_.split(", ")
        sub_playlist = player.generate_subplaylist(titles)
        print("Subplaylist generada:")
        print(sub_playlist)
    
    elif option == "20":
        print("Las 3 canciones que mas duran son: ")
        top_sub_playlist = player.top_canciones_largas()
        print(player.show_playlist())

    elif option == "13":
        print("👋 ¡Hasta pronto! Cerrando el reproductor...")
        break
    else:
        print("❌ Opción no válida. Por favor, elige una opción del menú.")


