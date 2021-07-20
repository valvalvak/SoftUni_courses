from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for flat in self.rooms:
            if room_number == flat.number:
                if not isinstance(flat.take_room(people), str):
                    self.guests += flat.guests
                break

    def free_room(self, room_number):
        for flat in self.rooms:
            if room_number == flat.number:
                self.guests -= flat.guests
                flat.free_room()

    def status(self):
        status_result = ""
        free_rooms = ', '.join([str(x.number) for x in self.rooms if not x.is_taken])
        taken_rooms = ', '.join([str(x.number) for x in self.rooms if x.is_taken])

        status_result += f"Hotel {self.name} has {self.guests} total guests\n" \
                         f"Free rooms: {free_rooms}\n" \
                         f"Taken rooms: {taken_rooms}\n"
        return status_result
