import pandas as pd
import json

# Load the CSV file
file_path = 'atms.csv' 
data = pd.read_csv(file_path)

# Renaming columns to match the desired keys in the JSON output
data.rename(columns={
    'ATM_Terminal_Id': 'ATM_Terminal_Id',
    'IP Address': 'ATM_IP',
    'ATM_Location': 'ATM_Location',
    'Username': 'Username',
    'Password': 'Password',
    'BRANCH_NAME': 'BRANCH_NAME',
    'ATM_TYPE': 'ATM_TYPE'
}, inplace=True)

# Selecting the relevant columns
json_data = data[['ATM_Terminal_Id', 'ATM_IP', 'ATM_Location', 'Username', 'Password', 'BRANCH_NAME', 'ATM_TYPE']]

# Converting the DataFrame to a list of dictionaries (JSON structure)
json_output = json_data.to_dict(orient='records')

# Define the output file path
json_file_path = 'path_to_output_json_file.json'  

# Write the JSON output to the file
with open(json_file_path, 'w') as json_file:
    json.dump(json_output, json_file, indent=4)

print(f"JSON file has been saved to: {json_file_path}")
