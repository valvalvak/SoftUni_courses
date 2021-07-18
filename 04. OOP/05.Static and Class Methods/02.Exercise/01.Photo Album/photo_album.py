class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = list([] for _ in range(self.pages))
        self.page = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        if len(self.photos) <= self.page + 1:
            return "No more free slots"
        if len(self.photos[self.page]) == 4:
            self.page += 1
        self.photos[self.page].append(label)
        return f"{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}"

    def display(self):
        string_representation = ""
        if self.pages:
            pass


# pa = PhotoAlbum(3)
# print(pa.photos)
album = PhotoAlbum(5)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.photos)
print(len(album.photos))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
