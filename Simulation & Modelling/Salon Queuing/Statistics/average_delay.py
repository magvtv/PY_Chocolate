import json
from datetime import datetime

with open("Salon Queuing/Data/clients.json", "r") as infile:
    data = json.load(infile)
    
total_delay = 0
for entry in data:
    arrival_time = datetime.strptime(entry["arrival"], "%H:%M")
    service_start_time = datetime.strptime(entry["service_start"], "%H:%M")
    
    delay = ((service_start_time - arrival_time).total_seconds()) / 60
    total_delay += delay
    
average_delay = total_delay / len(data)
print(f"Average delay: {average_delay} minutes ")