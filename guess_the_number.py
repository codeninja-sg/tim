import tkinter as tk
import random

root = tk.Tk()
root.title("Guess the Number")
root.geometry("400x300")


title_label = tk.Label(root, text="Guess the number!", font =("Arial", 18))
title_label.pack(pady=10)

prompt_label = tk.Label(root, text="Enter a number (1-100):")
prompt_label.pack()











root.mainloop()
