import tkinter as tk
from tkinter import ttk, messagebox, Listbox, END, Button, Text
from turtle import width
from priority_queue import PriorityQueue, validate_time_format, convert_to_24hr
import random


font_path = "/home/pharoh/.fonts/h/Handlee/Handlee-Regular.ttf"


def generate_patient_code():
    while True:
        code = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678990", k=3))
        if not any(
            ord(code[i]) + 1 == ord(code[i + 1]) == ord(code[i + 2])
            for i in range(len(code) - 2)
        ):
            break
    return code


def format_name(name):
    return name.title()


def add_appointment():
    patient_name = format_name(name_entry.get())
    if not patient_name:
        messagebox.showerror("Input Error", "Please enter patient name")
    patient_code = (
        code_entry.get().upper() if code_entry.get() else generate_patient_code()
    )
    checkin_time = time_entry.get()

    if not validate_time_format(checkin_time):
        messagebox.showerror(
            "Invalid Format! Use HHMM.", "eg. 0612 for 06:12h, 1212 for 1212h."
        )
        return

    formatted_time = convert_to_24hr(checkin_time)

    queue.enqueue(
        {"Name": patient_name, "Code": patient_code, "Time": (formatted_time)}
    )

    name_entry.delete(0, tk.END)
    code_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    refresh_listbox()


def remove_next_patient():
    next_patient = queue.dequeue()
    if next_patient:
        messagebox.showinfo(
            "Hospital Alert",
            f"Currently serving... \nName: {next_patient['Name']} \nID: {next_patient['Code']}",
        )
        refresh_listbox()
    if queue.is_empty():
        messagebox.showinfo("Hospital Alert", "All patients have been served!")


def refresh_listbox():
    # patients_listbox.delete(0, tk.END)
    patient_text.delete("1.0", END)
    for patient in queue:
        formatted_text = f"Name: {patient['Name']} \nID: {patient['Code']} \nTime: {patient['Time']}h\n\n"
        # patients_listbox.insert(END, formatted_text)
        patient_text.insert(END, formatted_text, "\n")


if __name__ == "__main__":
    queue = PriorityQueue()
    root = tk.Tk()
    root.title("Hospital Checkup Appointment")
    root.option_add('*Font', f'{{Handlee}} {12}')
    
    font_style = ttk.Style()
    font_style.configure("CustomFont.TFont", font=("Handlee", 'bold', 12))

    name_label = tk.Label(root, text="Patient Name:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    code_label = tk.Label(
        root, text=f"Optional Patient Code (eg. {generate_patient_code()}):"
    )
    code_label.pack()
    code_entry = tk.Entry(root)
    code_entry.pack()

    time_label = tk.Label(root, text="Check In Time (HHMM in 24h):")
    time_label.pack()
    time_entry = tk.Entry(root)
    time_entry.pack()

    add_button = Button(root, text="Add Patient", command=add_appointment)
    add_button.pack()

    remove_button = Button(root, text="Serve Next Patient", command=remove_next_patient)
    remove_button.pack()

    patient_text = Text(root, width=50, height=10, wrap="word")
    patient_text.tag_configure("CustomFont", font=("Handlee", 12))
    patient_text.configure(font="CustomFont.TFont")
    patient_text.pack()

    refresh_listbox()

    root.mainloop()
