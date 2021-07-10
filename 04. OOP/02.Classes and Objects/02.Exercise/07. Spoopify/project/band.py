from project.album import Album, List


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List = []

    def add_album(self, album: Album):
        if album.name not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        if Album.IS_ALBUM_PUBLISHED:
            return f"Album has been published. It cannot be removed."

        for album in self.albums:
            if album_name == album.name:
                self.albums.remove(album.name)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        result += "\n".join([f"{Album.details(a)}" for a in self.albums])
        return result
