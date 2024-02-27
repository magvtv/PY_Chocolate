import numpy as np

def initialize():
    global sim_time, server_status, num_in_q, time_last_event, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status
    # Initialize the simulation clock
    sim_time = 0.0
    # Initialize the state variables
    server_status = "IDLE"
    num_in_q = 0
    time_last_event = 0.0
    # Initialize the statistical counters
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    # Initialize event list
    time_next_event = [sim_time + expon(mean_interarrival), 1.0e+30]

initialize()