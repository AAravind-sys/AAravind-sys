import pandas as pd
import matplotlib.pyplot as plt
import os

# Assuming you have a list of filenames (fns) and CSVs (csvs) already defined

dic_csv = {}
for i in range(len(fns)):
    dic_csv[fns[i]] = pd.read_csv(csvs[i])

# Set time index
for key, df in dic_csv.items():
    df['Time'] = pd.to_datetime(df['Time'])
    df.set_index(['Time'], inplace=True)

# Create a folder to store the plots
output_folder = 'plots'
os.makedirs(output_folder, exist_ok=True)

# Data frame slice range
start_time = pd.to_datetime('00:35:00.000')
end_time = pd.to_datetime('00:37:00.000')
time_interval = pd.Timedelta(minutes=2)

# Create new dictionary to store the sliced data frames
slice_dic = {}

# Calculate the end times for each interval
current_time = start_time
while current_time <= end_time:
    next_time = current_time + time_interval
    for key, df in dic_csv.items():
        # Slice the DataFrame based on the specified time range
        sliced_df = df.between_time(current_time.time(), next_time.time())
        
        # Store the sliced DataFrame in the new dictionary
        slice_dic[key] = sliced_df
        
        # Create a subplot and save the plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(sliced_df.index, sliced_df['P1-Water Discharge Pressure'])
        ax.plot(sliced_df.index, sliced_df['P1-Air-Supply-pressure'])
        ax.plot(sliced_df.index, sliced_df['P1-CPM'])
        ax.set_ylim(0, 118)
        ax.set_title(key)
        
        # Save the plot with a filename indicating the time interval
        filename = os.path.join('D:\\1.2022\\AODD Different test cases\\Aprildata', f'{key}_{current_time.strftime("%H-%M-%S")}_to_{next_time.strftime("%H-%M-%S")}.png')
        plt.savefig(filename)
        plt.close()
    
    current_time = next_time

