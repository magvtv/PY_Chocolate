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
for i in range(20):
    client_name = random.choice(client_names)
    # generate random arrival time
    arrival_time = datetime.now() + timedelta(minutes = random.randint(0, 19))
    
    # generate random service start and stop time within 8 - 128 minutes
    service_start = arrival_time + timedelta(minutes=random.randint(4, 29))
    
    # generate random service start and stop time within 8 - 128 minutes
    service_stop = service_start + timedelta(minutes=random.randint(14, 59))
    
    service_types = [
        'Hair styling',
        'Trimming',
        'Hair Color',
        'Deep Conditioning Treatment',
        'Keratin Hair Treatment'
    ]

    service_type = random.choice(service_types)
    
    # generate random service start and stop time within 8 - 128 minutes
    depart_time = service_stop + timedelta(minutes=random.randint(2, 5))
    
    client_data = {
        "name": client_name,
        "arrival time": arrival_time.strftime('%H:%M'),
        "service type": service_type,
        "service start time": service_start.strftime('%H:%M'),
        "service  stop time": service_stop.strftime('%H:%M'),
        "depart time": depart_time.strftime('%H:%M'),
    }
    
    data.append(client_data)
    
with open("Salon Queueing/salon_clients.json", "w") as outfile:
    json.dump(data, outfile, indent=3)

print("Salon client data generated successfully, saved to salon_clients.json!")

with open("Salon Queueing/salon_clients.json", "r") as infile:
    data = json.load(infile)

num_entries = len(data)
print(f"There are {num_entries} customers in it.")