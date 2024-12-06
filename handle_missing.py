import os
import pandas as pd
import numpy as np
from datetime import time

# Read the CSV file
df = pd.read_csv('Classification/data/traffic_data.csv')

# Function to generate random time
def random_time():
	return time(hour=np.random.randint(0, 24), minute=np.random.randint(0, 60)).strftime('%H:%M')

# Function to generate random weather condition
def random_weather():
	conditions = ['Sunny', 'Rainy', 'Cloudy', 'Foggy', 'Windy']
	return np.random.choice(conditions)

# Function to generate random number of deaths
def random_deaths():
	return np.random.randint(0, 10)  # Adjust the range as needed

# Handle missing values in 'Time of the Accidents'
df['Time of the Accidents'] = df['Time of the Accidents'].fillna(df['Time of the Accidents'].apply(lambda x: random_time() if pd.isna(x) else x))

# Handle missing values in 'Weather conditions'
df['Weather conditions'] = df['Weather conditions'].fillna(df['Weather conditions'].apply(lambda x: random_weather() if pd.isna(x) else x))

# Handle missing values in 'Total people confirmed dead'
df['Total people confirmed dead'] = df['Total people confirmed dead'].fillna(df['Total people confirmed dead'].apply(lambda x: random_deaths() if pd.isna(x) else x))

# Save the updated DataFrame to a new CSV file
df.to_csv('Classification/data/traffic_data_updated.csv', index=False)

print("Updated CSV file has been created: traffic_data_updated.csv")