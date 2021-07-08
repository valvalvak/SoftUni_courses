from typing import List

from project.song import Song


class Album:
    SINGLE = 1
    IS_ALBUM_PUBLISHED = False

    def __init__(self, name: str, songs):
        self.name = name
        self.songs: List = []
        self.published = Album.IS_ALBUM_PUBLISHED

    def add_song(self, song: Song):
        if song.name is None or all([len(s) for s in song.name]) < 1:
            return self.songs

        elif len(song.name) == Album.SINGLE:
            return f"Cannot add {song.name}. It's a single"

        elif self.published is True:
            return f"Cannot add songs. Album is published."

        if song.name not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

        else:
            return f"Song is already in the album."

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
        Album.IS_ALBUM_PUBLISHED = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        result += "\n".join([f"== {Song.get_info(s)}\n" for s in self.songs])
        return result
