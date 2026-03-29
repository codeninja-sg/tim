import tkinter as tk
import random
import math


root = tk.Tk()
root.title("Whack-A-Dot")
root.geometry("1000x1000")


canvas = tk.Canvas(root, bg="white", width=900,height=900)
canvas.pack(padx=10, pady=10)


score = 0
score_label = tk.Label(root, text="Score:0", font=("Arial",14))
score_label.pack(pady=4)


dot_x = 100
dot_y = 100


DOT_R = 100
MOVE_MS = 1000


def draw_dot(x, y):

    return canvas.create_oval(x-DOT_R, y-DOT_R, x+DOT_R, y+DOT_R, fill="red", outline="blue")

current_dot_id = draw_dot(dot_x, dot_y)


CAN_W = 460
CAN_H = 400


def move_dot():


    global dot_x, dot_y, current_dot_id
















root.mainloop()