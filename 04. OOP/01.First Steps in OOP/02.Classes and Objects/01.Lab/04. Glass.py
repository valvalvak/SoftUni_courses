class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml_val):
        if ml_val <= Glass.capacity:
            self.content += ml_val
            return f"Glass filled with {ml_val} ml"
        else:
            return f"Cannot add {ml_val} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
