import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


titles = ["date", "mean_temp"]
data = pd.read_csv("/home/pharoh/Desktop/LEARN/PY/Data/ldn_weather.csv", usecols = titles) 
ldn_data = pd.DataFrame(data)
values = ldn_data.tail(16)

x = (values["date"] - 20201200)
y = values["mean_temp"]

#find line of best fit
a, b = np.polyfit(x, y, 1)
plt.title("London Temperatures", fontweight="bold")

#add points to plot
plt.scatter(x, y)
plt.xlabel("Date 2020", fontweight="semibold")
plt.ylabel("Temperature", fontweight="semibold")
line_eq = ((a * x) + b)

#add line of best fit to plot
plt.plot(x, line_eq, ':k')
plt.show()

#lowest temperature from ldn_data
lowest_temp = min(y)
print("Lowest Temp: " + str(lowest_temp) + "°C")
