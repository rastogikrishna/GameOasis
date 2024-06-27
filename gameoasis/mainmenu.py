import tkinter as tk
from tkinter import messagebox, ttk, font, PhotoImage
import subprocess
from ttkbootstrap import Style



def launch_game(game_file):
    try:
        subprocess.run(["python3", game_file], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to start the game: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def launch_flappy_bird():
    launch_game("flappy_bird_game.py")

def launch_dots_and_boxes():
    launch_game("dots_and_boxes.py")

def launch_tic_tac_toe():
    launch_game("tic_tac_toe.py")

def launch_snake():
    launch_game("snake.py")

app = tk.Tk()
app.title("GAME OASIS")
app.geometry("1280x800")  # Width x Height

# Load the logo image
logo_image = PhotoImage(file="whitelogo.png")  

# Logo Label
logo_label = ttk.Label(app, image=logo_image)
logo_label.image = logo_image  # Keep a reference to avoid garbage collection
logo_label.place(x=10, y=10)

style = Style()
style.theme_use("superhero")

# Custom Font for Title
title_font = font.Font(family="times new roman", size=60, weight="bold")

# Title Label
title_label = ttk.Label(app, text="GAME OASIS", font=title_font)
title_label.pack(pady=20)


# Frame for buttons
frame = ttk.Frame(app)
frame.pack(pady=80)

# Using ttk.Button for better theming
btn_flappy_bird = ttk.Button(frame, text="Flappy Bird", command=launch_flappy_bird)
btn_flappy_bird.grid(row=0, column=0, padx=10, pady=10)

btn_xoxo = ttk.Button(frame, text="Dots and Boxes", command=launch_dots_and_boxes)
btn_xoxo.grid(row=0, column=1, padx=10, pady=10)

btn_tic_tac_toe = ttk.Button(frame, text="Tic Tac Toe", command=launch_tic_tac_toe)
btn_tic_tac_toe.grid(row=1, column=0, padx=10, pady=10)

btn_snake = ttk.Button(frame, text="Greedy Snake", command=launch_snake)
btn_snake.grid(row=1, column=1, padx=10, pady=10)

app.mainloop()

