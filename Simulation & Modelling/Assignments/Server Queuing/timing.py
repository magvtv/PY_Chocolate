def timing():
    global next_event_type, time_next_event, min_time_next_event, num_events

    # Initialize the minimum time next event.
    min_time_next_event = 1.0e+29

    # Initialize the event type.
    next_event_type = 0

    # Determine the event type of the next event to occur.
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i

    # Check to see whether the event list is empty.
    if next_event_type == 0:
        # The event list is empty, so stop the simulation.
        print(f"Event list empty at time {sim_time}")
        exit(1)

    # The event list is not empty, so advance the simulation clock.
    sim_time = min_time_next_event
