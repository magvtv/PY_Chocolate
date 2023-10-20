import tkinter as tk
from datetime import datetime

class HospitalQueue:
    def __init__(self):
        self.queue = []

    def add_patient(self, name, checkin_time):
        name = name.title()
        # Accept 24-hour time and convert it to a 12-hour format for display
        fmt_24hr = "%H%M"
        fmt_12hr = "%I:%M %p"
        checkin_datetime = datetime.strptime(checkin_time, fmt_24hr)
        checkin_convert_12hr = checkin_datetime.strftime(fmt_12hr)

        # Add the patient as a tuple (checkin_time, name)
        self.queue.append((checkin_datetime, name, checkin_convert_12hr))
        self.queue.sort()  # Sort by checkin_time

    def remove_next_patient(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

# Create the tkinter application
root = tk.Tk()
root.title("Hospital Checkup Appointment")

queue = HospitalQueue()

# Function to add a patient
def add_patient():
    name = name_entry.get()
    checkin_time = checkin_time_entry.get()
    queue.add_patient(name, checkin_time)
    refresh_listbox()

# Function to remove the next patient
def remove_next_patient():
    next_patient = queue.remove_next_patient()
    if next_patient:
        refresh_listbox()

# Function to update the list of patients
def refresh_listbox():
    patients_listbox.delete(0, tk.END)
    for _, name, checkin_time_12hr in queue.queue:
        patients_listbox.insert(tk.END, f"{name}: {checkin_time_12hr}")

# Entry fields for name and check-in time
name_label = tk.Label(root, text="Patient Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

checkin_time_label = tk.Label(root, text="Check-in Time (24-hour format HHMM):")
checkin_time_label.pack()
checkin_time_entry = tk.Entry(root)
checkin_time_entry.pack()

# Option to display time in 12-hour format
show_12hr_time = tk.BooleanVar()
show_12hr_time.set(False)
show_12hr_time_checkbox = tk.Checkbutton(root, text="Show in 12-hour format", variable=show_12hr_time)
show_12hr_time_checkbox.pack()

# Buttons to add and remove patients
add_button = tk.Button(root, text="Add Patient", command=add_patient)
add_button.pack()

remove_button = tk.Button(root, text="Remove Next Patient", command=remove_next_patient)
remove_button.pack()

# Listbox to display patients
patients_listbox = tk.Listbox(root)
patients_listbox.pack()

# Function to handle time format conversion
def convert_time_format():
    refresh_listbox()  # Refresh the listbox to apply the format change

# Button to apply time format conversion
convert_time_button = tk.Button(root, text="Apply Time Format", command=convert_time_format)
convert_time_button.pack()

root.mainloop()
