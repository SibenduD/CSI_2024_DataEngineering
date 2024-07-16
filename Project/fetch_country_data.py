import requests
import json

# Define countries list
countries = ["india", "us", "uk", "china", "russia"]

# Loop through countries
for country in countries:
  url = f"https://restcountries.com/v3.1/name/{country}"
  response = requests.get(url)

  # Check for successful response
  if response.status_code == 200:
    data = response.json()

    # Save data to JSON file with country name
    with open(f"country_data/{country}.json", "w") as outfile:
      json.dump(data, outfile, indent=4)
  else:
    print(f"Error fetching data for {country}: {response.status_code}")