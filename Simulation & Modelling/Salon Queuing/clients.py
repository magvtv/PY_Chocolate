import json
import random
from datetime import datetime, timedelta


client_names = [
    'Jenifer',
    'Katie',
    'Tiffany',
    'Sarah',
    'Rachel',
    'Ashley',
    'Jessica',
    'Amanda',
    'Emily',
    'Gabriella',
    'Elizabeth',
    'Heidi',
    'Melissa',
    'Courtney',
    'Nicole',
    'Stephanie',
    'Megan',
    'Brittny',
    'Lauren',
    'Daisy',
]

data = []
initial_service_start = datetime.strptime("07:00", "%H:%M")
for i in range(20):
    client_name = random.choice(list(set(client_names) - set([entry["name"] for entry in data])))
    
    # arrival times: 
    arrival_delay = random.randint(2, 819)
    arrival_time = initial_service_start + timedelta(minutes=arrival_delay)
    
    
    # generate random choice of service to be done on client at the salon
    service_types = [
        'Hair styling',
        'Trimming',
        'Hair Color',
        'Hair Wash',
        'Scalp Treatment',
        'Olaplex',
        'Deep Conditioning Treatment',
        'Keratin Hair Treatment',
        'Bleach & Tone',
        'Hair Straightening',
        'Blow Dry',
    ]
    service_type = random.choice(service_types)

    # service times: ensuring the service stop never exceeds closing hours
    service_delay = random.randint(10, 34)
    service_start = arrival_time + timedelta(minutes=service_delay)
    service_stop = service_start + timedelta(minutes=random.randint(9, 74))
    service_stop = min(service_stop, arrival_time.replace(hour=21, minute=00))
    
    service_duration = (service_stop - service_start).total_seconds() / 60
    
    # depart delay and times last client does not exceed closing hours
    depart_delay = random.randint(2, 6)
    depart_time = service_stop + timedelta(minutes=depart_delay)
    depart_time = min(depart_time, arrival_time.replace(hour=21, minute=00))
    
    # updating the last service stop time
    final_service_stop = max(service_stop, depart_time)
    
    client_data = {
        "name": client_name,
        "arrival": f"{arrival_time.strftime('%H:%M')}h",
        "service_type": service_type,
        "service_start": f"{service_start.strftime('%H:%M')}h",
        "service_stop": f"{service_stop.strftime('%H:%M')}h",
        "service_duration": f"{int(service_duration)}mins",
        "departure": f"{depart_time.strftime('%H:%M')}h",
    }
    
    data.append(client_data)

data.sort(key=lambda x: datetime.strptime(x["arrival"], "%H:%M"))    
with open("Salon Queuing/Data/clients.json", "w") as outfile:
    json.dump(data, outfile, indent=3)

print("Salon client data generated successfully, saved to clients.json!")

with open("Salon Queuing/Data/clients.json", "r") as infile:
    data = json.load(infile)

num_entries = len(data)
print(f"There are {num_entries} customers in it.")