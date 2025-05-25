import time
from tkinter import *

root = Tk()
root.title("Digital Clock")

# Initial theme and font settings
is_dark_theme = True
current_font = ("Courier", 60)

# Theme colors
dark_theme = {"bg": "black", "fg": "green"}
light_theme = {"bg": "white", "fg": "blue"}

# Apply theme
def apply_theme():
    theme = dark_theme if is_dark_theme else light_theme
    root.configure(bg=theme["bg"])
    clock_label.config(bg=theme["bg"], fg=theme["fg"])
    toggle_button.config(bg=theme["bg"], fg=theme["fg"])

# Clock update function
def start():
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour format
    clock_label.config(text=current_time)
    clock_label.after(1000, start)

# Theme toggle
def toggle_theme():
    global is_dark_theme
    is_dark_theme = not is_dark_theme
    apply_theme()

# Clock Label
clock_label = Label(root, font=current_font, bd=50)
clock_label.grid(row=0, column=0, padx=20, pady=20)

# Toggle Button
toggle_button = Button(root, text="mode", command=toggle_theme, font=("Arial", 14))
toggle_button.grid(row=1, column=0, pady=10)

apply_theme()
start()
root.mainloop()