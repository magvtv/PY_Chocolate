def update_time_avg_stats():
    global sim_time, time_last_event, num_in_q, area_num_in_q, area_server_status
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    
    # Update area under number-in-queue function
    area_num_in_q += num_in_q * time_since_last_event
    
    # Update area under server-busy indicator function
    area_server_status += server_status * time_since_last_event

update_time_avg_stats()