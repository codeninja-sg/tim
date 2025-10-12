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
result_label = tk.Label(root,text="Result: --", font=("Arial", 14))


result_label = tk.Label(root, text="Result: --", font=("Arial", 14))
result_label.grid(row=2, column=0, columnspan=4, pady=8)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=4)

def parse_inputs():
    a_text = entry_a.get().strip()
    b_text = entry_b.get().strip()
    if a_text == "" or b_text == "":
        raise ValueError("Please enter botj A and B")
    

root.mainloop()
