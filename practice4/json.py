import json

# Load the JSON data from the file
with open('sample-data.json') as f:
    data = json.load(f)

# Print the headers
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("="*90)

# Iterate through the data and print in the specified format
for item in data:
    dn = item.get('DN', 'N/A')
    description = item.get('Description', 'N/A')
    speed = item.get('Speed', 'N/A')
    mtu = item.get('MTU', 'N/A')

    # Print the values in the desired table format
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")