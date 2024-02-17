import requests
import json
     
API = "https://chatgpt-api.shn.hk/v1/"
response = requests.get(API)


if response.status_code == 200:
    data = response.json()
    

    filename = "younas.json"
    
    # Write the JSON data to a file
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Data saved to {filename}")
else:
    print("Failed to fetch data. Status code:", response.status_code)