import tkinter as tk

class DrawSedan:
    def draw(self, canvas):
        # Draw sedan body
        canvas.create_polygon(50, 100, 100, 50, 400, 50, 450, 100, 450, 150, 50, 150, fill="gray")

        # Draw windows
        canvas.create_polygon(110, 60, 390, 60, 440, 100, 440, 150, 390, 190, 110, 190, fill="lightblue")

        # Draw wheels
        canvas.create_oval(100, 140, 160, 200, fill="black")
        canvas.create_oval(340, 140, 400, 200, fill="black")

        # Draw headlights
        canvas.create_oval(450, 100, 460, 110, fill="yellow")
        canvas.create_oval(450, 140, 460, 150, fill="yellow")

        # Draw taillights
        canvas.create_oval(40, 100, 50, 110, fill="red")
        canvas.create_oval(40, 140, 50, 150, fill="red")

def show_sedan(canvas):
    canvas.delete("all")
    drawer = DrawSedan()
    drawer.draw(canvas)

root = tk.Tk()
root.title("Sedan Side View Drawing")

canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

show_sedan_button = tk.Button(root, text="Show Sedan", command=lambda: show_sedan(canvas))
show_sedan_button.pack()

root.mainloop()

