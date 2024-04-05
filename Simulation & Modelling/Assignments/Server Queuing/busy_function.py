import matplotlib.pyplot as plt

# Arrival and departure times
arrival_times = [0.7, 1.6, 2.0, 2.2, 3.8, 4.0, 5.6, 7.2, 8.3, 8.9]
departure_times = [2.5, 3.1, 3.3, 3.5, 5.2, 9.5]

# Initialize time axis and server status
time_axis = []
server_status = []

# Set initial server status to idle
current_status = 0  # 0 for idle, 1 for busy

# Iterate through time points
for t in range(int(arrival_times[0]), int(departure_times[-1]) + 1):
    time_axis.append(t)
    if t in arrival_times:
        current_status = 1  # Server becomes busy upon arrival
    if t in departure_times:
        current_status = 0  # Server becomes idle upon departure
    server_status.append(current_status)

# Plot the busy function
plt.step(time_axis, server_status, where='post')
plt.xlabel('Time')
plt.ylabel('Server Status')
plt.title('Busy Function of the Single-Server Queueing Model')
plt.ylim(-0.1, 1.1)  # Set y-axis limits
plt.show()
