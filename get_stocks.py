import os
import pandas as pd
folder_path = '/home/pharoh/JKUAT/YR 4/S4.1/Knowledge Based Systems/Regression/data'
output_file = 'standard_chartered_stocks.csv'

# Empty data frame that will hold the combined data
combined_data = pd.DataFrame()
print("Started")

for file_name in os.listdir(folder_path):
    # print(file_name)
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        # print(file_path)

        # Read the current csv file
        df = pd.read_csv(file_path)

        # Filter by the specific company
        equity_data = df[df['CODE'] == 'SCBK']

        # Append it to the combined data frame
        combined_data = pd.concat([combined_data, equity_data])

# Save the data frame to an output file
combined_data.to_csv(output_file, index=False)
