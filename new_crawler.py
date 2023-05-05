import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from apartment import Apartment
from time import sleep


def get_df(base_url):
    # Set up empty lists for data
    # TODO: add much more lists of attributes like (pets_allowed, wifi, etc.)
    rates = []
    num_of_guests = []
    num_of_rooms = []
    pets_allowed = []
    wifi = []
    names = []


    # Loop through the first 15 pages of search results
    for i in range(1, 16):
        current_url = base_url + f'&page={i}'

        response = requests.get(current_url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all apartments on the page
        apartments = soup.find_all("div", class_="lwy0wad l1tup9az dir dir-ltr")

        # TODO: implement the price and other values extraction from outside response(?)

        # Loop through each apartment and click on it to get the detailed information
        for index, apartment in enumerate(apartments):
            url = "https://www.airbnb.com" + apartment.find("a")["href"]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            json_data = soup.find('script', id='data-state').text
            json_obj = json.loads(json_data)

            # Creating an Apartment object
            curr_apartment = Apartment(json_obj)

            # Appending the return value of each apartment to relevant list
            num_of_rooms.append(curr_apartment.get_num_of_rooms())
            num_of_guests.append(curr_apartment.get_num_of_guests())
            rates.append(curr_apartment.get_rate())
            wifi.append(curr_apartment.get_wifi())
            pets_allowed.append(curr_apartment.get_pets_allowed())
            names.append(curr_apartment.get_name())

            # Added 2 seconds sleep between each request in order to prevent block by the website
            sleep(2)

            # In order to save the apartments data in folder, uncomment the below rows
            # json_string = json.dumps(json_obj, indent=4)
            # if os.getcwd().find("LA") == -1:
            #     os.chdir('./LA')
            #
            # with open(f"page_{i}_apart_{index}.json", "w") as outfile:
            #     outfile.write(json_string)

    # Create pandas dataframe from data
    data = {
        "Name": names,
        "Rooms": num_of_rooms,
        "Guests": num_of_guests,
        "Pets": pets_allowed,
        "Wifi": wifi
    }
    df = pd.DataFrame(data)
    return df


def main():
    # The list of all df after we extract them from the function
    df_list = []
    for url in urls:
        df_list.append(get_df(url))

    # Appending all df into one big df
    df_concatenated = pd.concat(df_list)

if __name__ == "__main__":
    # Each url is the first page out of 15 pages
    urls = [
        "https://www.airbnb.com/s/Los-Angeles--CA--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2023-04-01&checkout=2023-04-08&source=structured_search_input_header&search_type=search_query"
    ]
    # main()
    get_df(urls[0])