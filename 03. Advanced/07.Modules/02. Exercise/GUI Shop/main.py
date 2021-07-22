import tkinter as tk

from helpers import clear_screen


def register_form(screen: tk.Tk):
    clear_screen(screen)
    inputs = [
        tk.Entry(screen),
        tk.Entry(screen),
        tk.Entry(screen),
        tk.Entry(screen),
    ]
    for index, input_widget in enumerate(inputs):
        input_widget.grid(row=index, column=0)

    tk.Button(screen, text="Submit", command=lambda: print(inputs[0].get())).grid(row=len(inputs), column=0)


def register_log(**users_log):
    with open("user_log.txt", 'a') as usernames:
        usernames.write(f"{users_log} - {users_log['password']}")
        pass
    print(users_log)


if __name__ == "__main__":
    window = tk.Tk()
    window.title = "My App"
    window.geometry("600x600")

    tk.Button(window, text="login", background="black", foreground="green",
              command=lambda: print("Clicked")).grid(row=0, column=0)
    tk.Button(window, text="register", command=lambda: print("Clicked")).grid(row=0, column=1)

    tk.Button(window, text="register", command=lambda: clear_screen(window)).grid(row=1, column=1)

    window.mainloop()
