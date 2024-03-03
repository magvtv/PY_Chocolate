def update_time_avg_stats():
    global time_last_event, sim_time, area_num_in_queue, area_server_status, num_in_queue, server_status

    # Compute time since the last event and update the last-event-time marker.
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    # Update area under the number-in-queue function.
    area_num_in_queue += num_in_queue * time_since_last_event

    # Update area under the server-busy indicator function.
    area_server_status += server_status * time_since_last_event
