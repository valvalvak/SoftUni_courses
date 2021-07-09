from typing import List

from project.song import Song


class Album:
    published = False

    def __init__(self, name: str):
        self.name = name
        self.songs: List = []

    def add_song(self, song: Song):

        if song is None:
            return self.songs

        elif song.single:
            return f"Cannot add {song.name}. It's a single"

        elif self.published is True:
            return f"Cannot add songs. Album is published."

        elif song in self.songs:
            return f"Song is already in the album."

        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):

        if self.published is True:
            return f"Cannot remove songs. Album is published."

        if song_name in self.songs:
            self.songs.remove(song_name)
            return f"Removed song {song_name} from album {self.name}."

        else:
            return f"Song is not in the album."

    def publish(self):

        if self.published is True:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        result += "".join([f"== {Song.get_info(s)}\n" for s in self.songs])

        return result
