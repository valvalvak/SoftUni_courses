from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        if not songs or songs is None:
            self.songs = []
        else:
            self.songs = list(x for x in songs)
        self.published = False

    def add_song(self, song):
        if song in self.songs:
            return f"Song is already in the album."
        else:
            if song.single:
                return f"Cannot add {song.name}. It's a single"
            elif self.published:
                return f"Cannot add songs. Album is published."
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published is True:
            return f"Cannot remove songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        else:
            return f"Song is not in the album."

    def publish(self):
        if self.published is False:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"
        result += "".join([f"== {Song.get_info(s)}\n" for s in self.songs])
        return result
