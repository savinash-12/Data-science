import requests
import pandas as pd

# 1. Define the API URL
url = 'https://api.covid19api.com/summary' # Example URL

# 2. Make the GET request
response = requests.get(url)

# 3. Check if the request was successful (status code 200)
if response.status_code == 200:
    # 4. Extract the JSON data as a Python dictionary
    data = response.json()

    # 5. Normalize the data into a DataFrame. 
    # Often the relevant data is under a specific key (e.g., 'Countries')
    df = pd.json_normalize(data['Countries'])

    # Print the first few rows of the DataFrame
    print(df.head())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")