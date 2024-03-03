from external_definition import time_arrival, time_next_event, mean_interarrival, expon, Q_LIMIT, mean_service
from timing import sim_time
def arrive():
    global num_in_q, server_status, num_customers_delayed, total_of_delays
    delay = 0.0
    # Schedule next arrival
    time_next_event[1] = sim_time + expon(mean_interarrival)
    
    # Check if the server is busy
    if server_status == "BUSY":
        # Server is busy, increment number of customers in queue
        num_in_q += 1
        
        # Check for overflow condition
        if num_in_q > Q_LIMIT:
            # Queue has overflowed, stop the simulation
            print(f"\nOverflow of the array time_arrival at time {sim_time}")
            exit(2)
        
        # Store the time of arrival of the customer at the end of time_arrival
        time_arrival[num_in_q] = sim_time
    else:
        # Server is idle, arriving customer has zero delay
        total_of_delays += delay
        
        # Increment number of customers delayed and make server busy
        num_customers_delayed += 1
        server_status = "BUSY"
        
        # Schedule a departure (service completion)
        time_next_event[2] = sim_time + expon(mean_service)

arrive()