"""
    implementing a hospital priority queue using the priority queue ADT
    thoughts on mankone together with scheduling people according to their
    appointment times
"""

import tkinter as tk

class HospitalQueue:
    def __init__(self):
        self.queue = []
        
    def add_patient(self, name, appointment_time):
        self.queue.append(name, appointment_time)
        self.queue.sort()
        
    def remove_min(self):
        if not self.is_empty():
            return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    
    def length(self):
        return len(self.queue)
    
root = tk.Tk()
root.title = 'Checkup Priority Queue'

queue = HospitalQueue()

def refresh_listbox():
    patient_listbox.delete(0, tk.END)
    for appointment_time, name in queue.queue:
        patient_listbox.insert(tk.END, f'{name} - {appointment_time}')
    



def add_patient():
    name = name_entry.get()
    appointment_time = int(time_entry.get())
    queue.add_patient(name, appointment_time)
    refresh_listbox()
    

def remove_next_patient():
    next_patient = queue.remove_min()
    if next_patient:
        refresh_listbox()


