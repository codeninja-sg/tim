import tkinter as tk
root = tk.Tk()
root.title("Tkinter Calculator")

title = tk.Label(root, text="Simple Calculator", font=("Arial", 18))
title.grid(row=0, column=0, columnspan=4,pady=10)


tk.Label(root, text="A:").grid(row=1, column=0, sticky="e", padx=5)
entry_a = tk.Entry(root, width=12, justify="right")
entry_a.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="B:").grid(row=1, column=2, sticky="e", padx=5)
entry_b = tk.Entry(root, width=12, justify="left")
entry_b.grid(row=1, column=3, padx=5, pady=5)







root.mainloop()
