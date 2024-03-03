import os
from math import pi

def main():
    # Open input and output files
    infile_path = "mm1.in"
    outfile_path = "mm1.out"
    infile = open(infile_path, "r")
    outfile = open(outfile_path, "w")
    
    # Specify the number of events for the timing function
    num_events = int(infile.readline().strip())
    
    # Read input parameters
    mean_interarrival, mean_service, num_delays_required = map(float, infile.readline().split())
    
    # Write report header and input parameters
    outfile.write("Single-server queueing system\n\n")
    outfile.write(f"Mean interarrival time: {mean_interarrival:.3f} minutes\n\n")
    outfile.write(f"Mean service time:      {mean_service:.3f} minutes\n\n")
    outfile.write(f"Number of customers:   {num_delays_required}\n\n")
    
    # Initialize the simulation
    initialize()
    
    # Run the simulation while more delays are still needed
    while num_custs_delayed < num_delays_required:
        
        # Determine the next event
        timing()
            
        # Update time-average statistical accumulators
        update_time_avg_stats()
            
        # Invoke the appropriate event function
        match infile.read()[0]:
            case '1':
                arrive()
                break
            case '2':
                depart()
                break
            default:
                raise ValueError("Unexpected event.")

    # Invoke the report generator and end the simulation
    report()
    infile.close()
    outfile.close()

def arrival_rate(lambda_, tau):
    return lambda_ / tau

def mean_wait_time(mu, sigma):
    return mu**2 + (sigma**2)/(2*mu**2)

def mean_response_time(mu, sigma):
    return mean_wait_time(mu, sigma) + 1/mu

def initialize():
    global num_custs_delayed
    num_custs_delayed = 0

def timing():
    pass

def arrive():
    global num_custs_delayed
    num_custs_delayed += 1

def depart():
    pass

def update_time_avg_stats():
    pass

def report():
    pass