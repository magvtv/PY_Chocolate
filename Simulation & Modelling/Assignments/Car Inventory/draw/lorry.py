import tkinter as tk

def draw_actros_side_view(canvas):
    # Cabin
    canvas.create_polygon(100, 180, 160, 140, 300, 140, 320, 180, fill="silver", outline="black")
    canvas.create_rectangle(160, 180, 300, 250, fill="darkgray", outline="black")  # Lower part of the cabin
    canvas.create_rectangle(100, 200, 160, 240, fill="darkgray", outline="black")  # Behind cabin
    
    # Wheels
    for x in [120, 280, 400, 520]:
        canvas.create_oval(x, 240, x+60, 300, fill="black", outline="gray")  # Large wheels
    
    # Chassis
    canvas.create_line(100, 250, 600, 250, fill="black", width=3)  # Main chassis line

# Tkinter setup
root = tk.Tk()
root.title("Mercedes Benz Actros Side View")
canvas = tk.Canvas(root, width=700, height=350)
canvas.pack()

draw_actros_side_view(canvas)

root.mainloop()
