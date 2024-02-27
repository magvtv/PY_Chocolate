def depart():
    global num_in_q, server_status, num_custs_delayed, total_of_delays
    delay = 0.0
    
    # Check if the queue is empty
    if num_in_q == 0:
        # Queue is empty, make the server idle and eliminate departure event
        server_status = "IDLE"
        time_next_event[2] = 1.0e+30
    else:
        # Queue is nonempty, decrement number of customers in queue
        num_in_q -= 1
        
        # Compute delay of customer beginning service and update total delay accumulator
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        
        # Increment number of customers delayed and schedule departure
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)
        
        # Move each customer in queue up one place
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1]

depart()