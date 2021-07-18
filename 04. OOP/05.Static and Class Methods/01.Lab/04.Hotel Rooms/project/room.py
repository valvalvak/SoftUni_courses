class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int):
        if self.is_taken is True:
            return f"Room number {self.number} cannot be taken"
        elif self.capacity < people:
            return f"Room number {self.number} cannot be taken"
        self.guests += people
        self.is_taken = True
        return

    def free_room(self):
        if self.is_taken is False:
            return f"Room number {self.number} is not taken"
        else:
            self.guests = 0
            self.is_taken = False
            return
