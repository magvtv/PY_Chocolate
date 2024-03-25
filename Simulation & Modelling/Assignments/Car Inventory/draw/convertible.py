import tkinter as tk

class DrawConvertible:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw_front_view(self):
        # Simplified front view
        self.canvas.create_rectangle(50, 50, 150, 100, fill="blue")  # Main body
        self.canvas.create_rectangle(70, 70, 130, 90, fill="lightgray")  # Windshield

    def draw_side_view(self):
        # More detailed side view
        self.canvas.create_rectangle(20, 60, 180, 100, fill="blue", outline="blue")  # Main body
        self.canvas.create_polygon(20, 60, 40, 40, 160, 40, 180, 60, fill="lightblue")  # Roof and windshield
        self.canvas.create_oval(40, 90, 70, 120, fill="black")  # Front wheel
        self.canvas.create_oval(130, 90, 160, 120, fill="black")  # Rear wheel

    def draw_rear_view(self):
        # Simplified rear view
        self.canvas.create_rectangle(50, 50, 150, 100, fill="blue")  # Main body
        self.canvas.create_rectangle(70, 70, 130, 90, fill="lightgray")  # Rear window

# Tkinter setup
root = tk.Tk()
root.title("Convertible Drawing")
canvas = tk.Canvas(root, width=200, height=150)
canvas.pack()

convertible = DrawConvertible(canvas)
# Here you can call any of the three functions to draw the respective view.
# For example:
convertible.draw_side_view()

root.mainloop()
