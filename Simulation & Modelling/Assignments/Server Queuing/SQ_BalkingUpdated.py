import math
import random
import threading
import time

input_file = open("infile.txt", "r")
output_file = open("outfile.txt", "w")

Queue_Limit = 100
Busy = 1
Idle = 0

next_event_type = num_custs_delayed = num_delays_required = num_events = num_in_queue = server_status = 0

area_num_in_queue = area_sever_status = mean_interarrival = mean_service = simulation_time = time_last_event = total_of_delays = 0.0
time_arrival = [0] * (Queue_Limit+1)
time_next_event = [0] * 3

lunch_12 = False
lunch_1 = False


def initialization():

    global simulation_time, server_status, num_in_queue, time_last_event, num_custs_delayed, total_of_delays, area_sever_status, time_next_event
    server_status = Idle

    time_next_event[1] = simulation_time + expon(mean_interarrival)
    time_next_event[2] = 1.0 * 10**30


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


def update_time_avg_stats():

    global time_last_event, simulation_time, area_num_in_queue, area_sever_status, num_in_queue, server_status

    time_since_last_event = 0.0

    time_since_last_event = simulation_time - time_last_event
    time_last_event = simulation_time
    area_num_in_queue += num_in_queue * time_since_last_event
    area_sever_status += server_status * time_since_last_event


def arrive():

    global server_status, num_in_queue, total_of_delays, num_custs_delayed, simulation_time, mean_interarrival, time_next_event, Queue_Limit, time_arrival, mean_service
    delay = 0.0
    time_next_event[1] = simulation_time + expon(mean_interarrival)

    if (server_status == Busy):
        num_in_queue += 1
        if(num_in_queue > Queue_Limit):
            output_file.write("\nOverflow of the array time_interval at")
            output_file.write("time {0}".format(simulation_time))
            exit(2)
        time_arrival[num_in_queue] = simulation_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = Busy

        time_next_event[2] = simulation_time + expon(mean_service)


def depart():

    global total_of_delays, num_custs_delayed, num_in_queue, server_status, time_next_event, simulation_time, time_arrival, mean_service
    delay = 0.0

    if (num_in_queue == 0):
        server_status = Idle
        time_next_event[2] = 1.0 * 10**30
    else:
        num_in_queue -= 1
        delay = simulation_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = simulation_time + expon(mean_service)

        for i in range(num_in_queue):
            time_arrival[i+1] = time_arrival[i + 2]


def report():

    global total_of_delays, num_custs_delayed, simulation_time, area_num_in_queue, area_sever_status

    output_file.write("\nAverage delay in queue  {0} minutes\n\n".format(
        total_of_delays/num_custs_delayed))
    output_file.write("Average no in queue  {0}\n\n".format(
        area_num_in_queue/simulation_time))
    output_file.write("Server Utilization  {0}\n\n".format(
        area_sever_status/simulation_time))
    output_file.write("Time Simulation ended  {0}".format(simulation_time))


def expon(mean):
    rand = random.uniform(0.1, 1.0)
    return -(float(mean)) * math.log(rand)


def lunch_break():
    global lunch_1, lunch_12

    breaks = random.randint(1, 2)

    if breaks == 1:
        time.sleep(1)
        lunch_12 = True
    else:
        time.sleep(1)
        lunch_1 = True


def main():

    global input_file, output_file, num_events, mean_interarrival, mean_service, num_delays_required, num_custs_delayed
    num_events = 2

    input_parameters = input_file.readline().split()

    mean_interarrival = input_parameters[0]
    mean_service = input_parameters[1]
    num_delays_required = input_parameters[2]

    output_file.write("SINGLE SERVER QUEUING SYSTEM\n\n")
    output_file.write(
        "Mean interarrival time = {0} \n\n".format(mean_interarrival))
    output_file.write("Mean service time = {0} \n\n".format(mean_service))
    output_file.write("Number of Customers = {0} \n".format(num_delays_required))

    initialization()

    while (num_custs_delayed < int(num_delays_required)):
        timing()
        update_time_avg_stats()
        if (next_event_type == 1):
            arrive()
        elif (next_event_type == 2):
            depart()


thread1 = threading.Thread(target=main())
thread2 = threading.Thread(target=lunch_break())

thread1.start()
thread2.start()

report()

input_file.close()
output_file.close()
