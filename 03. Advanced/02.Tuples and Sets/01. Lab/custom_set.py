class CustomSet:
    resize_factor = 0.7

    def __init__(self):
        self.count = 0
        self.capacity = 8
        self.values = [None] * self.capacity

    def execute_resize_check(self):
        return self.capacity * self.resize_factor <= self.count

    def resize(self):
        old_values = self.values
        self.count = 0
        self.capacity += 2
        self.values = [None] * self.capacity

        for nested_list in old_values:
            if nested_list:
                for values in nested_list:
                    self.add(values)

    def get_index(self, value):
        value_hash = hash(value)

        return abs(value_hash) % self.capacity

    def add(self, value):
        index = self.get_index(value)

        if not self.values[index]:
            self.values[index] = []

        if value not in self.values[index]:
            self.values[index].append(value)
            self.count += 1

        if self.execute_resize_check():
            self.resize()

    def remove(self, value):
        if not self.contains(value):
            return

        index = self.get_index(value)
        self.values[index].remove(value)
        self.count -= 1

    def contains(self, value):
        index = self.get_index(value)

        if not self.values[index]:
            return False

        if value not in self.values[index]:
            return False

        return True

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return self.count


'''
Capacity : 8
Count: 0
|N|N|N|N|N|N|N|N|
'''

ss = CustomSet()

values = [1, -1, 0, 3.14, 'Pesho', True, False, 'Pesho', 5, 77, 1, "Gosho"]

for x in values:
    ss.add(x)
    print(x, hash(x))

print(ss.values)
print(5 in ss)

ss.remove(5)
print(ss.contains(5))

# for x in values:
#     print(x, hash(x))

# print(hash(1))
# print(hash(-1))
# print(hash(0))
# print(hash(-1))
