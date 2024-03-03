import math
import random
from external_definition import initialize, timing, update_time_avg_stats, next_event_type

def main():
    # open the input and output files
    infile = open("inputfile.txt", "r")
    outfile = open("outputfile.txt", "w")
    
    # specifying the number of events for the timing functions
    num_events = 2
    
        # Read input parameters.
    mean_interarrival, mean_service, num_delays_required = read_input(infile)

    # Write report heading and input parameters.
    write_report_heading(outfile)
    write_input_parameters(outfile, mean_interarrival, mean_service, num_delays_required)

    # Initialize the simulation.
    initialize()

    # Run the simulation while more delays are still needed.
    while num_custs_delayed < num_delays_required:
        # Determine the next event.
        timing()

        # Update time-average statistical accumulators.
        update_time_avg_stats()

        # Invoke the appropriate event function.
        switch(next_event_type)

    # Invoke the report generator and end the simulation.
    report()

    # Close input and output files.
    infile.close()
    outfile.close()

    return 0

def read_input(infile):
    # Read input parameters.
    mean_interarrival, mean_service, num_delays_required = infile.readline().split()
    return float(mean_interarrival), float(mean_service), int(num_delays_required)

def write_report_heading(outfile):
    outfile.write("Single-server queueing system\n\n")

def write_input_parameters(outfile, mean_interarrival, mean_service, num_delays_required):
    outfile.write("Mean interarrival time%11.3f minutes\n\n" % mean_interarrival)
    outfile.write("Mean service time%16.3f minutes\n\n" % mean_service)
    outfile.write("Number of customers%14d\n\n" % num_delays_required)

def switch(next_event_type):
    if next_event_type == 1:
        arrive()
    elif next_event_type == 2:
        depart()
    else:
        print("Invalid event type")

def arrive():
    global num_custs_delayed, num_in_q
    num_custs_delayed += 1
    num_in_q += 1

def depart():
    global num_custs_delayed, num_in_q
    num_custs_delayed -= 1
    num_in_q -= 1

def report():
    pass