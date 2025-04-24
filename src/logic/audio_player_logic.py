import time
import random
import sys

sys.path.append("src")
from exceptions.exceptions import AlreadyExistsError, EmptyPlaylistError, InvalidSongError


class Song():
    def __init__(self, title: str, artist: str, duration: float):
        self.title: str = title
        self.artist: str = artist
        self.duration: float = duration

    def __str__(self):
        return f"{self.title} - {self.artist} - {self.duration}s"


class DoubleNode:
    def __init__(self, song: Song, next = None, prev = None):
        self.song = song
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"{self.song}"


class Playlist(): # Va a ser la lista enlazada circular
    def __init__(self, head: DoubleNode = None, tail: DoubleNode = None):
        self.__head : DoubleNode = head
        self.__tail: DoubleNode = tail
        self.__size: int = 0

    # Métodos para acceder a los atributos privados
    def get_head(self) -> DoubleNode:
        return self.__head

    def get_tail(self) -> DoubleNode:
        return self.__tail

    def get_size(self) -> int:
        return self.__size


    def add_song(self, new_song: Song) -> None:
        new_song_node = DoubleNode(new_song)

        if (self.__size > 0):
            current_song = self.__head
            for _ in range(self.__size):
                if (current_song.song.title == new_song.title):
                    raise AlreadyExistsError("La canción ya existe")
                current_song = current_song.next

        if (self.__size == 0):
            self.__head = new_song_node
            self.__tail = new_song_node # como está vacía, el inicio y el final es el mismo
            self.__head.prev = new_song_node
            self.__tail.next = self.__head
        else:
            new_song_node.prev = self.__tail
            self.__tail.next = new_song_node
            self.__tail = new_song_node
            self.__head.prev = new_song_node # Se asigna al prev de la cabeza la cola, para que sea circular
            self.__tail.next = self.__head # Se asigna a la cola que su next es el head, para que sea circular
        self.__size += 1
        return


    def remove_song(self, song_title: str) -> None:

        if (self.__size == 0):
            raise EmptyPlaylistError("La playlist está vacía")

        current_song = self.__head

        for _ in range(self.__size):
            if (current_song.song.title == song_title):
                if self.__size == 1:  # Si solo hay un elemento
                    self.__head = None
                    self.__tail = None

                else:
                    if current_song == self.__head:  # Si es el primer elemento, la cabeza pasa a ser el siguiente
                        self.__head = current_song.next
                    elif current_song == self.__tail:  # Si es el último elemento, la cola pasa a ser el anterior
                        self.__tail = current_song.prev

                    current_song.prev.next = current_song.next
                    current_song.next.prev = current_song.prev

                self.__size -= 1
                return

            current_song = current_song.next

        raise InvalidSongError("La canción que quiere eliminar no existe en esta playlist")


    def __repr__(self) -> str:
        songs = []
        current = self.__head
        for _ in range(self.__size):
            songs.append(str(current.song.title))
            current = current.next
        return " <-> ".join(songs)
    

class AudioPlayer():
    def __init__(self):
        self.playlist = Playlist()
        self.sub_playlist = None
        self.current_playlist = self.playlist
        self.current = None

    def play_current_song(self) -> None:
        if (self.current_playlist.get_size() == 0):
            raise EmptyPlaylistError("La playlist está vacía")

        if self.current is None:
            self.current = self.current_playlist.get_head()
        message_start = f"🎧 Reproduciendo: {self.current.song.title} de {self.current.song.artist}"
        return (message_start)
    
    def play_song(self, title: str) -> str:
        if self.current_playlist.get_size() == 0:
            raise EmptyPlaylistError("La playlist está vacía")

        current = self.current_playlist.get_head()
        for _ in range(self.current_playlist.get_size()):
            if title == current.song.title:
                self.current = current  
                return f"🎧 Reproduciendo: {current.song.title} de {current.song.artist}"
            current = current.next

        return "⛔ No hay canción seleccionada para reproducir."


    def simulate_playback(self):
        if self.current:
            time.sleep(self.current.song.duration)  
            message_end = "🎶 Canción finalizada."
            return (message_end)
        else:
            message_end = "⛔ No hay canción seleccionada para reproducir."
            return (message_end)

    def next_song(self):
        if (self.current_playlist.get_size() == 0):
            raise EmptyPlaylistError("La playlist está vacía")

        if self.current:
            self.current = self.current.next                
            return f"Reproduciendo la siguiente canción de la playlist: {self.current.song}"
        else:
            return f"No se está reproduciendo actualmente ninguna canción"

    def previous_song(self):
        if (self.current_playlist.get_size() == 0):
            raise EmptyPlaylistError("La playlist está vacía")

        if self.current:
            self.current = self.current.prev
            return f"Reproduciendo anterior canción de la playlist: {self.current.song}"
        else:
            return f"No se está reproduciendo actualmente ninguna canción"

    def show_current_song(self):
        if self.current:
            return f"Actualmente suena '{self.current.song.title}', de {self.current.song.artist} y dura {self.current.song.duration}s."
        else:
            return "No hay ninguna canción seleccionada."

    def show_playlist(self):
        if (self.current_playlist.get_size() == 0):
            return f"La playlist está vacía"
        return str(self.current_playlist)

    def shuffle(self):
        if self.current_playlist.get_size() == 0:
            raise EmptyPlaylistError("La playlist está vacía")

        songs = [] 
        current = self.current_playlist.get_head()
        for _ in range(self.current_playlist.get_size()):
            songs.append(current.song.title)
            current = current.next

        while songs: 
            random_title = random.choice(songs)
            songs.remove(random_title)

            current = self.current_playlist.get_head()

            for _ in range(self.current_playlist.get_size()):
                if current.song.title == random_title:
                    self.current = current
                    print(f"Reproduciendo aleatoriamente: {self.current.song.title} de {self.current.song.artist}")
                    print(self.simulate_playback())
                    time.sleep(2)
                    break
                current = current.next

    def generate_subplaylist(self, songs_titles: list[str]) -> Playlist:
        if (self.current_playlist.get_size() == 0):
            raise EmptyPlaylistError("La playlist original está vacía, no hay canciones para generar una subplaylist")

        sub_playlist = Playlist()
        current = self.current_playlist.get_head()
        for _ in range(self.current_playlist.get_size()):
            if current.song.title in songs_titles:
                sub_playlist.add_song(current.song)
            current = current.next

        self.sub_playlist = sub_playlist
        return sub_playlist

    def play_playlist(self):
        if self.current_playlist.get_size() == 0:
            raise EmptyPlaylistError("La playlist está vacía")
        
        self.current = self.current_playlist.get_head()                                  
        for _ in range(self.current_playlist.get_size()):
            print(self.play_current_song())
            print(self.simulate_playback())
            time.sleep(2)
            self.next_song()

    def advance_song(self, percent: float) -> list[str]:
        messages = []

        if self.current is None:
            if self.current_playlist.get_size() == 0:
                raise EmptyPlaylistError("La playlist está vacía")
            self.current = self.current_playlist.get_head()
            messages.append(f"No había canción seleccionada. Iniciando desde la primera: {self.current.song.title}")

        duration = self.current.song.duration
        avance = duration * (percent / 100)

        messages.append(f"Adelantando {percent}% de la canción: {self.current.song.title}")
        messages.append(f"Simulando adelanto de {avance:.2f}s...")

        time.sleep(avance)

        if avance >= duration:
            messages.append("Tiempo adelantado excede la duración. Pasando a la siguiente canción...")
            self.current = self.current.next
            messages.append(f"🎧 Reproduciendo: {self.current.song.title} de {self.current.song.artist}")
            time.sleep(self.current.song.duration)
            messages.append("🎶 Canción finalizada.")
        else:
            restante = duration - avance
            messages.append(f"Reproduciendo los últimos {restante:.2f}s de la canción...")
            time.sleep(restante)
            messages.append("🎶 Canción finalizada.")

        return messages