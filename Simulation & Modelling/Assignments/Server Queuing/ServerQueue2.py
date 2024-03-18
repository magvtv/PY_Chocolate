import math
import random

# Constants
Queue_Limit = 100
Busy = 1
Idle = 0

# Initialize global variables
next_event_type = num_custs_delayed = num_delays_required = num_events = num_in_queue = server_status = 0
area_num_in_queue = area_sever_status = mean_interarrival = mean_service = simulation_time = time_last_event = total_of_delays = 0.0
time_arrival = [0] * (Queue_Limit + 1)
time_next_event = [0] * 3

# Function to initialize simulation
def initialization():
    global simulation_time, server_status, num_in_queue, time_last_event, num_custs_delayed, total_of_delays, area_sever_status, time_next_event
    server_status = Idle
    time_next_event[1] = simulation_time + expon(mean_interarrival)
    time_next_event[2] = float('inf')  # Infinite time for departure event initially

# Function to determine next event
def timing():
    global simulation_time, next_event_type, num_events
    next_event_type = time_next_event.index(min(time_next_event))
    simulation_time = time_next_event[next_event_type]

# Function to update time average statistics
def update_time_avg_stats():
    global time_last_event, simulation_time, area_num_in_queue, area_sever_status, num_in_queue, server_status
    time_since_last_event = simulation_time - time_last_event
    time_last_event = simulation_time
    area_num_in_queue += num_in_queue * time_since_last_event
    area_sever_status += server_status * time_since_last_event

# Function to handle arrival event
def arrive():
    global server_status, num_in_queue, total_of_delays, num_custs_delayed, simulation_time, mean_interarrival, time_next_event, Queue_Limit, time_arrival, mean_service
    delay = 0.0
    time_next_event[1] = simulation_time + expon(mean_interarrival)
    if server_status == Busy:
        num_in_queue += 1
        if num_in_queue > Queue_Limit:
            print("Overflow of the array time_interval at time", simulation_time)
            exit(2)
        time_arrival[num_in_queue] = simulation_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = Busy
        time_next_event[2] = simulation_time + expon(mean_service)

# Function to handle departure event
def depart():
    global total_of_delays, num_custs_delayed, num_in_queue, server_status, time_next_event, simulation_time, time_arrival, mean_service
    delay = 0.0
    if num_in_queue == 0:
        server_status = Idle
        time_next_event[2] = float('inf')  # No customers in queue, set departure time to infinity
    else:
        num_in_queue -= 1
        delay = simulation_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = simulation_time + expon(mean_service)
        time_arrival = time_arrival[1:]

# Function to report simulation results
def report():
    global total_of_delays, num_custs_delayed, simulation_time, area_num_in_queue, area_sever_status
    print("\nAverage Queue Delay = {:.3f} minutes".format(total_of_delays / num_custs_delayed))
    print("Average Number of Customers in Queue = {:.3f}".format(area_num_in_queue / simulation_time))
    print("Server Utilization = {:.3f}".format(area_sever_status / simulation_time))
    print("End Time of the Simulation = {:.3f} minutes".format(simulation_time))

# Exponential distribution function
def expon(mean):
    return -float(mean) * math.log(random.uniform(0.1, 1.0))

if __name__ == '__main__':
    # Open input and output files
    input_file = open("infile.txt", "r")
    output_file = open("outfile.txt", "w")

    # Read input parameters from file
    num_events = 2
    input_parameters = input_file.readline().split()
    mean_interarrival, mean_service, num_delays_required = map(float, input_parameters)

    # Write simulation parameters to output file
    output_file.write("SINGLE SERVER QUEUING SYSTEM\n\n")
    output_file.write("Mean Interarrival Time = {:.3f} minutes\n\n".format(mean_interarrival))
    output_file.write("Mean Service Time = {:.3f} minutes\n\n".format(mean_service))
    output_file.write("Total Customers = {}\n".format(num_delays_required))

    # Initialize simulation
    initialization()

    # Run simulation until required number of customers are served
    while num_custs_delayed < num_delays_required:
        timing()
        update_time_avg_stats()
        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()

    # Report simulation results
    report()

    # Close input and output files
    input_file.close()
    output_file.close()
