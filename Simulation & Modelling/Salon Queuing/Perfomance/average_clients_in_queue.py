import json
from datetime import datetime, timedelta

with open("Salon Queuing/Data/clients.json", "r") as infile:
    data = json.load(infile)
    
# defining the interval as quarter an hour
interval_duration = 15

total_clients_in_queue = 0
total_intervals = 0
current_time = datetime.strptime("07:00", "%H:%M")
close_time = datetime.strptime("21:00", "%H:%M")

while current_time < close_time:
    client_in_queue = sum(1 for entry in data if datetime.strptime(entry["arrival"], "%H:%M") <= current_time <= datetime.strptime(entry["service_start"], "%H:%M"))
    total_clients_in_queue += client_in_queue
    total_intervals += 1
    current_time += timedelta(minutes=interval_duration)
    
average_clients_in_queue = total_clients_in_queue / total_intervals
print(f"Average number of clients in queue: {average_clients_in_queue}")