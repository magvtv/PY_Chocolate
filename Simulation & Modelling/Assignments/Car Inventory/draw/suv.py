import tkinter as tk

def draw_sportage_side_view(canvas):
    # Main body
    canvas.create_polygon(50, 150, 100, 120, 250, 120, 300, 150, fill="blue", outline="black")  # Roof and windows
    canvas.create_rectangle(50, 150, 300, 200, fill="navy", outline="black")  # Lower body
    
    # Wheels
    canvas.create_oval(80, 180, 130, 230, fill="black", outline="gray")  # Front wheel
    canvas.create_oval(220, 180, 270, 230, fill="black", outline="gray")  # Rear wheel
    
    # Details
    canvas.create_line(100, 120, 100, 150, fill="lightgray")  # Front window divider
    canvas.create_line(250, 120, 250, 150, fill="lightgray")  # Rear window divider

# Tkinter setup
root = tk.Tk()
root.title("Kia Sportage Side View")
canvas = tk.Canvas(root, width=350, height=250)
canvas.pack()

draw_sportage_side_view(canvas)

root.mainloop()
