import pandas as pd
import json

# Load the CSV file
file_path = 'atms.csv'  # Update this with the actual file path
data = pd.read_csv(file_path)

# Renaming columns to match the desired keys in the JSON output
data.rename(columns={
    'ATM_Terminal_Id': 'ATM_Terminal_Id',
    'IP Address': 'ATM_IP',
    'ATM_Location': 'ATM_Location',
    'Username': 'Username',
    'Password': 'Password',
    'BRANCH_NAME': 'BRANCH_NAME',
    'ATM_TYPE': 'ATM_TYPE',
    'District': 'District',
    'CBS Account': 'CBS_Account',
    'Port': 'Port',
    'Site': 'Site',
    'Status': 'Status'
}, inplace=True)

# Convert the CSV data into the desired JSON structure
json_data = []
for _, row in data.iterrows():
    json_entry = {
        "ATM_Terminal_Id": row["ATM_Terminal_Id"],
        "ATM_IP": row["ATM_IP"],
        "ATM_Location": row["ATM_Location"],
        "Username": row["Username"],
        "Password": row["Password"],
        "BRANCH_NAME": row["BRANCH_NAME"],
        "ATM_TYPE": row["ATM_TYPE"],
        # Adding the extra fields
        "District": row["District"],
        "CBS_Account": row["CBS_Account"],
        "Port": row["Port"],
        "Site": row["Site"],
        "Status": row["Status"]
    }
    json_data.append(json_entry)

# Define the output file path
json_file_path = 'generated_config.json'  # Update this with the desired output path

# Write the JSON output to the file
with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON file has been saved to: {json_file_path}")
