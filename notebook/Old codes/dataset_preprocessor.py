import os
import pandas as pd

# Get a list of all files in the folder
folder = 'datasets/'
files = [f for f in os.listdir(folder) if f.endswith('.csv')]

# Read all the files into a list of dataframes
df_list = [pd.read_csv(folder + f) for f in files]

# Concatenate all the dataframes into a single dataframe
merged_df = pd.concat(df_list, ignore_index=True)

# Drop duplicates based on a column
# merged_df = merged_df.drop_duplicates(subset='')

# Save the resulting dataframe to a new file
merged_df.to_csv('datasets/merged_dataset.csv', index=False)
