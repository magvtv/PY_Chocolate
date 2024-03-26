import tkinter as tk

def draw_porsche_911_side_view(canvas):
    # Main body curve without sunroof for a sleek look
    canvas.create_polygon(40, 160, 90, 110, 250, 110, 310, 160, smooth=True, fill="red", outline="black")  

    # Lower part of the body
    canvas.create_rectangle(40, 160, 310, 200, fill="darkred", outline="black")  

    # Wheels - larger and more pronounced for a sporty look
    canvas.create_oval(80, 170, 130, 220, fill="black", outline="gray")  # Front wheel
    canvas.create_oval(220, 170, 270, 220, fill="black", outline="gray")  # Rear wheel

    # Enhancements for a more detailed look
    # Headlights
    canvas.create_oval(260, 130, 280, 150, fill="yellow", outline="black")
    # Rearview mirror
    canvas.create_polygon(150, 130, 155, 135, 150, 140, fill="darkred", outline="black")
    # Door handle
    canvas.create_rectangle(180, 160, 190, 165, fill="black", outline="black")

# Tkinter setup
root = tk.Tk()
root.title("Porsche 911 Turbo S Side View")
canvas = tk.Canvas(root, width=350, height=250)
canvas.pack()

draw_porsche_911_side_view(canvas)

root.mainloop()
