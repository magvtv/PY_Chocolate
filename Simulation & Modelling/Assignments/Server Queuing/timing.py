def timing():
    global next_event_type, sim_time
    min_time_next_event = 1.0e+29
    next_event_type = 0
    # Determine the event type of the next event to occur
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i
    
    # Check if the event list is empty
    if next_event_type == 0:
        # The event list is empty, stop the simulation
        print(f"\nEvent list empty at time {sim_time}")
        exit(1)
    
    # Advance the simulation clock
    sim_time = min_time_next_event

timing()