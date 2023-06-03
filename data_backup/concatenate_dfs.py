import pandas as pd

# List of file names
file_names = [f'data_output{i}.csv' for i in range(1,12)]

# Initialize an empty list to store individual DataFrames
dfs = []

# Loop through each file name and read the CSV file into a DataFrame
for file_name in file_names:
    df = pd.read_csv(file_name)
    dfs.append(df)

# Concatenate the DataFrames into one large DataFrame
concatenated_df = pd.concat(dfs, ignore_index=True)

concatenated_df = concatenated_df.iloc[:, 1:]
concatenated_df.reset_index(drop=True)

# Print the concatenated DataFrame
concatenated_df.to_csv('data_output.csv')
