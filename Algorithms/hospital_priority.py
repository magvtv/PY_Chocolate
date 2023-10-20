"""
    implementing a hospital priority queue using the priority queue ADT
    thoughts on mankone together with scheduling people according to their
    appointment times
    add name and appointment time
    sort with reference to the early bird, the earliest appointment
    
"""

import tkinter as tk
from datetime import datetime

class HospitalQueue:
    def __init__(self):
        self.queue = []
        
    def add_patient(self, name, appointment_time):
        # calculate the duration of the appointment
        fmt = '%H%Mh'
        start_datetime = datetime.strptime(appointment_time, fmt)
        self.queue.append((name, appointment_time))
        self.queue.sort()
        
    def remove_next_patient(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def length(self):
        return len(self.queue)
    
root = tk.Tk()
root.title = ('Appointment Checkup')

queue = HospitalQueue()

def refresh_listbox():
    patient_listbox.delete(0, tk.END)
    for name, appointment_time in queue.queue:
        patient_listbox.insert(tk.END, f'{name.capitalize()}: {appointment_time}')

def add_patient():
    name = name_entry.get()
    appointment_time = appointment_time_entry.get()
    queue.add_patient(name, appointment_time)
    refresh_listbox()
    

def remove_next_patient():
    next_patient = queue.remove_next_patient()
    if next_patient:
        refresh_listbox()


name_label = tk.Label(root, text='Patient\'s Name:')
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

appointment_time_label = tk.Label(root, text='Booking Time (HHmm):')
appointment_time_label.pack()
appointment_time_entry = tk.Entry(root)
appointment_time_entry.pack()

add_button = tk.Button(root, text='Add', command=add_patient)
add_button.pack()

remove_button = tk.Button(root, text='Remove', command=remove_next_patient)
remove_button.pack()

patient_listbox = tk.Listbox(root)
patient_listbox.pack()

root.mainloop()