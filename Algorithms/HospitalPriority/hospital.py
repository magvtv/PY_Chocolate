import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, Listbox, END, Button, Text
from turtle import width
from priority_queue import (
    PriorityQueue,
    validate_time_format,
    convert_to_12hr,
    convert_to_24hr,
)
import random

font_path = "/home/pharoh/.fonts/p/Plus_Jakarta_Sans/static/PlusJakartaSans-Light.ttf"
"""
    to get a unique code for any patient
    in the hospital appointment schedule
"""


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


"""
    insert any patient
    into the hospital appointment schedule
    capitalize the name, process the check in timestamp
"""


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
    patient_condition = condition_entry.get().upper()
    queue.enqueue(
        {
            "Name": patient_name,
            "Code": patient_code,
            "Time": (formatted_time),
            "Condition": patient_condition,
        }
    )
    name_entry.delete(0, tk.END)
    condition_entry.delete(0, tk.END)
    code_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    refresh_listbox()


def cancel_appointment():
    patient = simpledialog.askstring("Cancel Appointment", "Patient Name")
    patient_name = format_name(patient)
    patient_code = simpledialog.askstring("Cancel Appointment", "Health Service Code:")

    for patient in queue:
        if patient["Name"].title() == patient_name and patient["Code"] == patient_code:
            queue.remove(patient)
            messagebox.showinfo(
                "Cancel Apointment",
                f"{patient_name}'s appointment [{patient_code}] has been successfully cancelled",
            )
            refresh_listbox()
            return

    messagebox.showinfo(
        "Cancel Appointment",
        f"No appointment found for {patient_name} [{patient_code}].",
    )


"""
    the hospital serves the next patient,
    removing them from the appointment listing 
    sorts in order of timestamps (check in times)
"""


def remove_next_patient():
    next_patient = queue.dequeue()
    if next_patient:
        messagebox.showinfo(
            "Hospital Alert",
            f"Currently treating... \nName:  {next_patient['Name']} \nCondition: {next_patient['Condition']}",
        )
        refresh_listbox()
    if queue.is_empty():
        messagebox.showinfo("Hospital Alert", "All patients are treated!")


"""
function to check patient condition
GOOD means patient is comfortable and 
okay within the normal measures. priority weight of 2. color of green on the tkinter listbox display
FAIR means uncomfortable, the vital signs are alright, 
indicators can be questions, acutely ill. priority weight of 1. can be yellow in color on the tkinter display
CRITICAL means patient indicators are unfavorable 
unstable vital signs,either unconscious, had sudden accident.
"""


def get_priority_color(condition):
    if condition == "GOOD":
        return "chartreuse3"
    elif condition == "FAIR":
        return "darkgoldenrod1"
    elif condition == "CRITICAL":
        return "brown1"
    else:
        return None


"""
gives an updated version of the appointment schedule
clears the labels for a new entry
"""


def refresh_listbox():
    patients_listbox.delete(0, tk.END)
    # patient_text.delete("1.0", END)
    for patient in queue:
        priority_color = get_priority_color(patient["Condition"])
        formatted_text = f"Name: {patient['Name']}     ID: {patient['Code']}       Time:    {patient['Time']}h"
        patients_listbox.insert(END, formatted_text)
        patients_listbox.itemconfig(
            tk.END,
            {
                "bg": priority_color,
                "fg": "black",
            },
        )
        # patient_text.insert(END, formatted_text, "\n")


"""
    the main program incorporating all the functions above
    adding the titles, packing the entries, configuring fonts
    the whole program is executed with tkinter mainloop
"""
if __name__ == "__main__":
    queue = PriorityQueue()
    root = tk.Tk()
    root.title("Hospital Checkup Appointment")
    root.option_add("*Font", f"{{PlusJakartaSans}} {12}")

    font_style = ttk.Style()
    font_style.configure("CustomFont.TFont", font=("PlusJakartaSans", 12))

    name_label = tk.Label(root, text="Patient Name:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    code_label = tk.Label(
        root, text=f"Health Service Code (eg. {generate_patient_code()}):"
    )
    code_label.pack()
    code_entry = tk.Entry(root)
    code_entry.pack()

    condition_label = tk.Label(root, text="Patient Condition (Good/Fair/Critical):")
    condition_label.pack()
    condition_entry = tk.Entry(root)
    condition_entry.pack()

    time_label = tk.Label(root, text="Check In Time (HHMM in 24h):")
    time_label.pack()
    time_entry = tk.Entry(root)
    time_entry.pack()

    add_button = Button(root, text="Add Patient", command=add_appointment)
    add_button.pack()

    cancel_button = tk.Button(
        root, text="Cancel Appointment", command=cancel_appointment
    )
    cancel_button.pack()

    remove_button = Button(root, text="Treat Next Patient", command=remove_next_patient)
    remove_button.pack()

    patients_listbox = Listbox(root, width=50, height=10, background="lightgoldenrod3")
    patients_listbox.pack()

    refresh_listbox()

    root.mainloop()
