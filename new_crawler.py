import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# Set up empty lists for data
prices = []
rooms = []
rates = []
num_of_guests = []
num_of_rooms = []

# Loop through the first 5 pages of search results
for i in range(1, 6):
    # url = f"https://www.airbnb.com/s/Los-Angeles--CA--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2023-04-01&checkout=2023-04-08&source=structured_search_input_header&search_type=search_query&page={i}"
    url = "https://www.airbnb.com/s/Los-Angeles--CA--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2023-04-01&checkout=2023-04-08&source=structured_search_input_header&search_type=search_query&page=15"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # with open("outside_file.html", "w") as file:
    #     file.write(str(soup.prettify()))


    # Find all listings on the page
    listings = soup.find_all("div", class_="lwy0wad l1tup9az dir dir-ltr")
    # print(f"Page number {i}, Num of appartments: {len(listings)}")
    
    # TODO: implement the price and other values extraction


    # Loop through each listing and click on it to get the detailed information
    for listing in listings:
        url = "https://www.airbnb.com" + listing.find("a")["href"]
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # with open("inside_file.html", "w") as file:
        #     file.write(str(soup.prettify()))
        #
        # exit(0)
    
        # Extract price, number of rooms, and rate from the detailed information page
        # price = soup.find("span", class_="_tyxjp1").text
        # room = soup.find("div", class_="_kqh46o").text.split(" · ")[0]
        # rate = soup.find("span", class_="_18khxk1").text

        # Testing if works... not part of the script, have to add it afterwards
        # TODO: we recieve the data as json and need to extract the desired features.
        #  1.Make sure to determine the features - as many as possible
        #  2.Rewrite the script for other apartment and make sure all features we agreed on
        #    are in the there as well
        #  3.Extract all agreed features for each apartment
        #  4.Create df from the feature lists we made
        json_data = soup.find('script', id='data-state').text
        json_obj = json.loads(json_data)
        json_string = json.dumps(json_obj, indent=4)
        # Rename the json file name to prevent writing on existing one
        with open("output.json", "w") as outfile:
            outfile.write(json_string)
        exit(0)

        # Append the data to the lists
        # prices.append(price)
        # rooms.append(room)
        # rates.append(rate)

print(prices)
exit(0)
# Create pandas dataframe from data
data = {"Price": prices, "Rooms": rooms, "Rate": rates}
df = pd.DataFrame(data)

# Print dataframe
print(df)
