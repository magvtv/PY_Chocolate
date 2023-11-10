from priority_queue import (
    PriorityQueue,
    validate_time_format,
    convert_to_12hr,
    convert_to_24hr,
)
import tkinter as tk
from tkinter import messagebox, Listbox, END, StringVar


class CustomPriorityQueue(PriorityQueue):
    def __str_(self):
        return str(list(self.queue))

    def enqueue(self, patient):
        self.put(patient)

    def dequeue(self):
        return self.get()


queue = CustomPriorityQueue()
root = tk.Tk()
root.title("Hospital Checkup Appointment")


def refresh_listbox():
    patient_listbox.delete(0, tk.END)
    for patient in queue:
        time_str = (
            convert_to_12hr(patient["time"])
            if time_format.get() == "12hr"
            else convert_to_24hr(patient["time"])
        )
        patient_listbox.insert(END, f"Name: {patient['name']}, Time: {time_str}")


def add_appointment():
    patient_name = name_entry.get()
    checkin_time = time_entry.get()
    if not validate_time_format(checkin_time):
        messagebox.showerror("Invalid Format!", "Please use HH:MM.")
        return
    queue.enqueue({"Name": patient_name.title(), "Time": checkin_time})
    name_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    refresh_listbox()


def remove_patient():
    queue.dequeue()
    refresh_listbox()


def toggle_time_format():
    refresh_listbox()


def display_queue():
    if queue.is_empty():
        messagebox.showinfo("Empty Queue", "The hospital priority queue is empty.")


if __name__ == "__main__":
    name_label = tk.Label(root, text="Patient Name:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()
    time_label = tk.Label(root, text="Appointment Time (HH:MM):")
    time_label.pack()
    time_entry = tk.Entry(root)
    time_entry.pack()

    time_format = StringVar()
    time_format.set("24hr")

    time_format_label = tk.Label(root, text="Time Format")
    time_format_label.pack()
    time_format_24hr = tk.Radiobutton(
        root, text="24hr", variable=time_format, value="24hr", command=refresh_listbox
    )
    time_format_24hr.pack()
    time_format_12hr = tk.Radiobutton(
        root, text="12hr", variable=time_format, value="12hr", command=refresh_listbox
    )
    time_format_12hr.pack()

    add_button = tk.Button(root, text="Add Appointment", command=add_appointment)
    add_button.pack()
    remove_button = tk.Button(root, text="Remove Next Queue", command=remove_patient)
    remove_button.pack()

    patient_listbox = Listbox(root)
    patient_listbox.pack()

    root.mainloop()
