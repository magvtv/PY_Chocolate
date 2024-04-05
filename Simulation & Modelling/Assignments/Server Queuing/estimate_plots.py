"""
- this code runs on trinket (online python interpreter)
"""

import matplotlib.pyplot as plt
import numpy as np


arrivals = [0.7, 1.6, 2.0, 2.2, 3.8, 4.0, 5.6, 7.2, 8.3, 8.9]
departures = [2.5, 3.1, 3.3, 3.5, 5.2, 9.5]

time_points = sorted(set(arrivals + departures))
queue_length = np.zeros(len(time_points))

total_observation_time = time_points[-1]  # Total observation time

# Calculate queue length over time
for i, t in enumerate(time_points):
    arrivals_count = sum(1 for a in arrivals if a <= t)
    departures_count = sum(1 for d in departures if d <= t)
    queue_length[i] = arrivals_count - departures_count

plt.plot(time_points, queue_length)
plt.xlabel('Time')
plt.ylabel('Queue Length')
plt.title('Time Path of Queue Length')
plt.grid(True)
plt.show()

# Estimate of the time average number in queue
average_num_in_queue = np.trapz(queue_length, time_points) / total_observation_time
print(f"Estimate of the Time Average Number in Queue: {average_num_in_queue:.2f}")

# Estimate of the server utilization
server_busy_time = sum(time_points[i] - time_points[i-1] for i in range(1, len(time_points)) if queue_length[i] > 0)
server_utilization = server_busy_time / total_observation_time
print(f"Estimate of the Server Utilization: {server_utilization:.2f}")