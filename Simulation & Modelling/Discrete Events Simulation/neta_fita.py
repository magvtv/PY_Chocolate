import random

class Event:
    def __init__(self, time, event_type):
        self.time = time
        self.event_type = event_type
    
# function to generate random events
def generate_random_events(num_events):
    events = []
    for _ in range(num_events):
        time = random.uniform(1, 100)       # random time (1 - 100) time units
        event_type = random.choice(['Arrival', 'Departure'])
        events.append(Event(time, event_type))
    return events
    
    
# next event time advance (NETA) approach 
def simulate_neta(events):
    simulation_time = 0
    for event in events:
        print(f"Current Simulation Time: {simulation_time:.2f}")
        print(f"Processing Event: {event.event_type}, Time: {event.time:.2f}")
        simulation_time = event.time
            
# fixed increment time advance (FITA) approach
def simulate_fita(events):
    simulation_time = 0
    time_increment = 5      # fixed time increments of 5 minutes
    # simulate for 100 time units
    while simulation_time < 100:
        print(f"\nCurrent Simulation Time: {simulation_time:.2f}")
        events_increment = [e for e in events if simulation_time <= e.time < (simulation_time + time_increment)]
        for event in events_increment:
            print(f"Processing Event: {event.event_type}, Time: {event.time:.2f}")
        
        # advance simulation time by the time increment 
        simulation_time += time_increment


def main():
    # generate random events
    events = generate_random_events(10)
    print("NETA Simulation")
    simulate_neta(events)
    
    print("\nFITA Simulation")
    simulate_fita(events)
    
if __name__ == '__main__':
    main()
    
    
                