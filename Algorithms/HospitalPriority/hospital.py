from priority_queue import (
    PriorityQueue,
    validate_time_format,
    convert_to_12hr,
    convert_to_24hr,
)
import tkinter as tk
from tkinter import messagebox


def add_appointment():
    patient_name = name_entry.get()
    appointment_time = entry.get()
    if not validate_time_format(appointment_time):
        messagebox.showerror("Invalid Format", "Invalid time format. Please use HH:MM.")
        return

    queue.enqueue({"name": patient_name, "time": appointment_time})
    entry.delete(0, tk.END)


def display_queue():
    if queue.is_empty():
        messagebox.showinfo("Empty Queue", "The hospital priority queue is empty.")
    else:
        display_text = "Hospital Priority Queue:\n"
        for appointment in queue.queue:
            display_text += (
                f"Name: {appointment['name']}, Time: {appointment['time']}\n"
            )
        messagebox.showinfo("Current Queue", display_text)


def convert_time():
    appointment_time = entry.get()
    if appointment_time:
        if validate_time_format(appointment_time):
            if time_format.get() == 12:
                converted_time = convert_to_12hr(appointment_time)
            else:
                converted_time = convert_to_24hr(appointment_time)
            entry.delete(0, tk.END)
            entry.insert(0, converted_time)
        else:
            messagebox.showerror(
                "Invalid Format", "Invalid time format. Please use HH:MM."
            )


if __name__ == "__main__":
    queue = PriorityQueue()

    root = tk.Tk()

    label_name = tk.Label(root, text="Enter Patient Name:")
    name_entry = tk.Entry(root)
    label_time = tk.Label(root, text="Enter Appointment Time (HH:MM):")
    entry = tk.Entry(root)
    add_button = tk.Button(root, text="Add Appointment", command=add_appointment)
    display_button = tk.Button(root, text="Display Queue", command=display_queue)
    convert_button = tk.Button(root, text="Convert Time", command=convert_time)

    time_format = tk.IntVar()
    time_format.set(24)
    time_format_24hr = tk.Radiobutton(root, text="24hr", variable=time_format, value=24)
    time_format_12hr = tk.Radiobutton(root, text="12hr", variable=time_format, value=12)

    label_name.pack()
    name_entry.pack()
    label_time.pack()
    entry.pack()
    add_button.pack()
    display_button.pack()
    time_format_24hr.pack()
    time_format_12hr.pack()
    convert_button.pack()

    root.mainloop()
