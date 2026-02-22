import tkinter as tk

root = tk.Tk()
root.title("Drawing Pad")
root.geometry("800x600")


controls = tk.Frame(root)
controls.grid(row=0, column=0, sticky="ew", padx=8, pady=8)


canvas = tk.Canvas(root, bg="white",width=760,height=480)
canvas.grid(row=1, column=0,sticky="nsew",padx=8,pady=8)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


current_color = "red"
pen_size = 2
last_x, last_y = None, None


def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y


def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y, fill=current_color, width=pen_size)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)


def set_black():
    global current_color
    current_color = "black"

def set_red():
    global current_color
    current_color = "red"



def set_blue():
    global current_color
    current_color = "blue"


def set_orange(): 
    global current_color
    current_color = "orange"


btn_black= tk.Button(controls, text="Black",command=set_black)
btn_black.grid(row=0, column=0, padx=2)
btn_red= tk.Button(controls, text="Red",command=set_red)
btn_red.grid(row=0, column=1, padx=2)
btn_blue= tk.Button(controls, text="Blue",command=set_blue)
btn_blue.grid(row=0, column=2, padx=2)
btn_orange= tk.Button(controls, text="Orange",command=set_orange)
btn_orange.grid(row=0, column=3, padx=2)


    




root.mainloop()















root.mainloop()
