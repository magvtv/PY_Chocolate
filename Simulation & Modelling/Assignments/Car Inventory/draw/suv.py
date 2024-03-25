import tkinter as tk

class DrawSUV:
    def draw(self, canvas):
        # Draw SUV body
        canvas.create_rectangle(50, 50, 250, 100, fill="gray")

        # Draw windows
        canvas.create_rectangle(70, 60, 100, 80, fill="lightblue")
        canvas.create_rectangle(150, 60, 180, 80, fill="lightblue")
        canvas.create_rectangle(210, 60, 240, 80, fill="lightblue")

        # Draw wheels
        canvas.create_oval(70, 100, 100, 130, fill="black")
        canvas.create_oval(200, 100, 230, 130, fill="black")

def show_next_car():
    canvas.delete("all")  # Clear canvas
    drawer = DrawSUV()
    drawer.draw(canvas)

root = tk.Tk()
root.title("Car Inventory System")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

show_next_car_button = tk.Button(root, text="Show Next Car", command=show_next_car)
show_next_car_button.pack()

root.mainloop()
