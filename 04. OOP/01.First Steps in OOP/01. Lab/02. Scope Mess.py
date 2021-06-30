x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)  # EXPECTED OUTPUT @ ROW 3: "inner: nonlocal"

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)  # EXPECTED OUTPUT @ ROW 2: "outer: local"
    inner()
    print("outer:", x)  # EXPECTED OUTPUT @ ROW 4: "outer: nonlocal"
    change_global()


print(x)  # EXPECTED OUTPUT @ ROW 1: "global"
outer()
print(x)  # EXPECTED OUTPUT @ ROW 5: "global: changed!"
