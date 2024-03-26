import tkinter as tk

def draw_tesla_model_s_side_view(canvas):
    # Main body and roof as one smooth curve to capture the sleek design
    canvas.create_polygon(50, 150, 100, 120, 250, 120, 300, 150, smooth=True, fill="silver", outline="black")

    # Lower part of the body to complete the side profile
    canvas.create_rectangle(50, 150, 300, 190, fill="darkgray", outline="black")

    # Wheels - designed to be sleek yet noticeable
    canvas.create_oval(90, 170, 130, 210, fill="black", outline="gray")  # Front wheel
    canvas.create_oval(220, 170, 260, 210, fill="black", outline="gray")  # Rear wheel

    # Enhancements for a more detailed look
    # Door handles (Tesla's are known for their retractable handles, so we'll represent them as small lines)
    canvas.create_line(130, 160, 140, 160, fill="black", width=2)
    canvas.create_line(200, 160, 210, 160, fill="black", width=2)

    # Windows - a single large piece for the front and rear passenger sections
    canvas.create_polygon(105, 122, 120, 130, 230, 130, 245, 122, fill="lightblue", smooth=True)

# Tkinter setup
root = tk.Tk()
root.title("Tesla Model S Side View")
canvas = tk.Canvas(root, width=350, height=250)
canvas.pack()

draw_tesla_model_s_side_view(canvas)

root.mainloop()
