import math
import random

# initializing the variables of queue length, server state
Q_LIMIT = 100
BUSY = 1
IDLE = 0

# initialize other variables
next_event_type = 0
num_customers_delayed = 0
num_delays_required = 0
num_in_queue = 0
server_status = IDLE

# initialize time variable
area_num_in_queue = 0.0
area_server_status = 0.0
mean_interarrival = 0.0
mean_service = 0.0
sim_time = 0.0
time_arrival = [0] * (Q_LIMIT + 1)
time_last_event = 0.0
time_next_event = [0] * 3
total_delays = 0.0

# initialize file pointers
infile = None
outfile = None


def initialize():
    global next_event_type, num_customers_delayed, num_delays_required, num_events, num_in_queue, server_status
    next_event_type = 0
    num_customers_delayed = 0
    num_delays_required = 0
    num_events = 0
    num_in_queue = 0
    server_status = IDLE

def timing():
    global next_event_type, num_customers_delayed, num_delays_required, num_events, num_in_queue, server_status
    pass

def arrive():
    global next_event_type, num_customers_delayed, num_delays_required, num_events, num_in_queue, server_status
    pass

def depart():
    global next_event_type, num_customers_delayed, num_delays_required, num_events, num_in_queue, server_status
    pass


def report():
    global next_event_type, num_customers_delayed, num_delays_required, num_events, num_in_queue, server_status
    pass

def update_time_avg_stats():
    global area_num_in_queue, area_server_status, mean_interarrival, mean_service, sim_time, time_arrival, time_last_event, time_next_event, total_delays
    pass

def expon(mean):
    pass