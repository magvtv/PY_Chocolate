import tkinter as tk

class DrawJeepWrangler:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw_front_view(self):
        # Simplified front view of a Jeep Wrangler
        self.canvas.create_rectangle(50, 50, 150, 100, fill="green")  # Main body
        self.canvas.create_rectangle(70, 70, 130, 80, fill="black")  # Grille
        for i in range(70, 131, 10):  # Grille slots
            self.canvas.create_line(i, 70, i, 80, fill="gray")
        self.canvas.create_rectangle(90, 50, 110, 70, fill="yellow")  # Windshield

    def draw_side_view(self):
        # More detailed side view of a Jeep Wrangler
        self.canvas.create_rectangle(30, 70, 170, 100, fill="green", outline="green")  # Main body lower part
        self.canvas.create_polygon(30, 70, 50, 60, 150, 60, 170, 70, fill="lightgreen")  # Roof
        self.canvas.create_oval(40, 90, 70, 120, fill="black", outline="gray")  # Front wheel
        self.canvas.create_oval(130, 90, 160, 120, fill="black", outline="gray")  # Rear wheel
        self.canvas.create_rectangle(150, 60, 170, 70, fill="black")  # Spare tire representation

    def draw_rear_view(self):
        # Simplified rear view of a Jeep Wrangler
        self.canvas.create_rectangle(50, 50, 150, 100, fill="green")  # Main body
        self.canvas.create_oval(120, 60, 140, 80, fill="black")  # Spare tire

# Tkinter setup to display the Jeep Wrangler
root = tk.Tk()
root.title("Jeep Wrangler Drawing")

canvas = tk.Canvas(root, width=200, height=150)
canvas.pack()

jeep = DrawJeepWrangler(canvas)
# You can call any of the three methods based on the view you want to display.
# For example, to draw the side view:
jeep.draw_rear_view()
# jeep.draw_side_view()

root.mainloop()
