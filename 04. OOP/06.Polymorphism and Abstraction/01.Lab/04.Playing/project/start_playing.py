class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()


def start_playing(guitar):
    return guitar.play()


print(start_playing(guitar))
