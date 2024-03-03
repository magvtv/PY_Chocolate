from external_definition import time_next_event, mean_interarrival, expon, IDLE

def initialize():
    global sim_time, server_status, num_in_queue, time_last_event, num_customers_delayed, total_delays, area_num_in_queue, area_server_status

    # Initialize the simulation clock.
    sim_time = 0.0

    # Initialize the state variables.
    server_status = IDLE
    num_in_queue = 0
    time_last_event = 0.0

    # Initialize the statistical counters.
    num_customers_delayed = 0
    total_delays = 0.0
    area_num_in_queue = 0.0
    area_server_status = 0.0

    # Initialize event list.
    # Since no customers are present, the departure (service completion) event is eliminated from consideration.
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30
