"""
    implementing a hospital priority queue using the priority queue ADT
    thoughts on mankone together with scheduling people according to their
    appointment times
"""

import tkinter as tk
from datetime import datetime

class HospitalQueue:
    def __init__(self):
        self.queue = []
        
    def add_patient(self, name, start_time, end_time):
        # calculate the duration of the appointment
        fmt = '%H%Mh'
        start_datetime = datetime.strptime(start_time, fmt)
        end_datetime = datetime.strptime(end_time, fmt)
        
        # duration in minutes first then bigger into hours and minutes
        duration_mins = ((end_datetime - start_datetime).total_seconds()) / 60
        duration_hr = duration_mins // 60
        duration_rem_mins = duration_mins % 60
        
        
        
        self.queue.append((name, start_time, end_time, duration_hr, duration_rem_mins))
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
root.title = 'Checkup Priority Queue'

queue = HospitalQueue()

def refresh_listbox():
    patient_listbox.delete(0, tk.END)
    for name, start_time, end_time, duration_hr, duration_rem_mins in queue.queue:
        patient_listbox.insert(tk.END, f'{name.capitalize()}:  {int(duration_hr)}h {int(duration_rem_mins)}m - [{start_time} - {end_time}]')

def add_patient():
    name = name_entry.get()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    queue.add_patient(name, start_time, end_time)
    refresh_listbox()
    

def remove_next_patient():
    next_patient = queue.remove_next_patient()
    if next_patient:
        refresh_listbox()


name_label = tk.Label(root, text='Patient\'s Name:')
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

start_time_label = tk.Label(root, text='Start Time (HHmm):')
start_time_label.pack()
start_time_entry = tk.Entry(root)
start_time_entry.pack()

end_time_label = tk.Label(root, text='End Time (HHmm):')
end_time_label.pack()
end_time_entry = tk.Entry(root)
end_time_entry.pack()

add_button = tk.Button(root, text='Add', command=add_patient)
add_button.pack()

remove_button = tk.Button(root, text='Remove', command=remove_next_patient)
remove_button.pack()

patient_listbox = tk.Listbox(root)
patient_listbox.pack()

root.mainloop()