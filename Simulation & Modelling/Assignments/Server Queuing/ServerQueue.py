import math
import random

# initialize constants
QUEUE_LIMIT = 100
BUSY = 1
IDLE = 0

# initialize global variables and arrays for storing the simulation data
next_event_type = num_custs_delayed = num_delays_required = num_events = num_in_queue = server_status = 0
area_num_in_queue = area_server_status = mean_interarrival = mean_service = simulation_time = time_last_event = total_of_delays = 0.0
time_arrival = [0] * (QUEUE_LIMIT+1)
time_next_event = [0] * 3

# function to initialize the simulation - setting the server_status
# calculate the time for the next arrival event
# set the departure time to infinity since it is close to "1.0 * 10**30"
def initialization():
    global simulation_time, server_status, num_in_queue, time_last_event, num_custs_delayed, total_of_delays, area_server_status, time_next_event
    server_status = IDLE
    time_next_event[1] = simulation_time + exponential(mean_interarrival)
    time_next_event[2] = 1.0 * 10**30


# function to determine the next event type based on the minimum time from the event list
# also updates the simulation time to the time of the next event
def timing():
    global simulation_time, next_event_type, num_events
    main_time_next_event = 1.0 * 10**29
    next_event_type = 0
    for i in range(num_events):
        if (time_next_event[i+1] < main_time_next_event):
            main_time_next_event = time_next_event[i+1]
            next_event_type = i+1

    if (next_event_type == 0):
        output_file.write(
            "\nEvent list is empty at time {0}".format(simulation_time))
        exit(1)

    simulation_time = main_time_next_event

# function to update the time average statistics
# calculates the time since the last event and updates the stats such as average number in queue
def update_time_avg_stats():
    global time_last_event, simulation_time, area_num_in_queue, area_server_status, num_in_queue, server_status
    time_since_last_event = 0.0
    time_since_last_event = simulation_time - time_last_event
    time_last_event = simulation_time
    area_num_in_queue += num_in_queue * time_since_last_event
    area_server_status += server_status * time_since_last_event


# function to handle the arrival event
# updates the next arrival time and checks the server_status
# also manages queue overflow and calculates the delays for customers
def arrive():
    global server_status, num_in_queue, total_of_delays, num_custs_delayed, simulation_time, mean_interarrival, time_next_event, QUEUE_LIMIT, time_arrival, mean_service
    delay = 0.0
    time_next_event[1] = simulation_time + exponential(mean_interarrival)

    if (server_status == BUSY):
        num_in_queue += 1
        if(num_in_queue > QUEUE_LIMIT):
            output_file.write("\nOverflow of the array time_interval at")
            output_file.write("time {0}".format(simulation_time))
            exit(2)
        time_arrival[num_in_queue] = simulation_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY

        time_next_event[2] = simulation_time + exponential(mean_service)


# function to handle departure event
# updates the queue status and calculates the delays of the departed customers
def depart():
    global total_of_delays, num_custs_delayed, num_in_queue, server_status, time_next_event, simulation_time, time_arrival, mean_service
    delay = 0.0

    if (num_in_queue == 0):
        server_status = IDLE
        time_next_event[2] = 1.0 * 10**30
    else:
        num_in_queue -= 1
        delay = simulation_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = simulation_time + exponential(mean_service)

        for i in range(num_in_queue):
            time_arrival[i+1] = time_arrival[i + 2]

# function to report the simulation results to outfile
def report():
    global total_of_delays, num_custs_delayed, simulation_time, area_num_in_queue, area_server_status
    output_file.write("\nAverage Queue Delay  {:.3f} minutes\n\n".format((total_of_delays/num_custs_delayed), 3))
    output_file.write("Average Number in Queue  {:.3f}\n\n".format((area_num_in_queue/simulation_time), 3))
    output_file.write("Server Utilization   {:.3f}\n\n".format((area_server_status/simulation_time), 3))
    output_file.write("Time Simulation Ended    {:.3f} minutes".format(simulation_time, 3))

# exponential distribution function
# generates a random number for the exponential distribution calculation
def exponential(mean):
    rand = random.uniform(0.1, 1.0)
    return -(float(mean)) * math.log(rand)





if __name__ == '__main__':
    # open the input and output files within the same directory
    input_file = open('infile.txt', "r")
    output_file = open("outfile.txt", "w")

    # read input parameter in the infile 
    num_events = 2
    input_parameters = input_file.readline().split()
    mean_interarrival = input_parameters[0]
    mean_service = input_parameters[1]
    num_delays_required = input_parameters[2]

    # write the simulation parameters to the outfile
    output_file.write("SINGLE SERVER QUEUING SYSTEM\n\n")
    output_file.write("Mean Interarrival Time   {}00 minutes \n\n".format(mean_interarrival))
    output_file.write("Mean Service Time    {}00 minutes\n\n".format(mean_service))
    output_file.write("Number of Customers  {} \n".format(num_delays_required))

    # call the simulation initialization function
    initialization()

    # run simulation until the required number of customers are served
    while (num_custs_delayed < int(num_delays_required)):
        timing()
        update_time_avg_stats()

        if (next_event_type == 1):
            arrive()
        elif (next_event_type == 2):
            depart()
            
    # call the report function for the above simulation results
    report()

    # close the files
    input_file.close()
    output_file.close()
