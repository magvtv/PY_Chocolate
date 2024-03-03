def report():
    global total_delays, num_customers_delayed, area_num_in_queue, area_server_status, sim_time
    # Compute and write estimates of desired measures of performance
    average_delay_in_queue = total_delays / num_customers_delayed
    print("\n\nAverage delay in queue:", round(average_delay_in_queue, 3), "minutes\n\n")
    average_number_in_queue = area_num_in_queue / sim_time
    print("Average number in queue:", round(average_number_in_queue, 3), "\n\n")
    server_utilization = area_server_status / sim_time
    print("Server utilization:", round(server_utilization * 100, 3), "%\n\n")
    print("Time simulation ended:", round(sim_time, 3), "minutes")

report()