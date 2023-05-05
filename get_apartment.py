import requests
from bs4 import BeautifulSoup
import json
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        '\nScript for get the json with data about apartment\n'
        'Need to provide the apartment url name and the folder name we want to save the data in'
    )
    parser.add_argument('--url', dest='url', required=True)
    parser.add_argument('--name', dest='name', required=True)

    return parser.parse_args()

def main(url, dir_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    json_data = soup.find('script', id='data-state').text
    json_obj = json.loads(json_data)
    json_string = json.dumps(json_obj, indent=4)

    # while os.path.exists(dir_name):
    #     dir_name += '_latest'

    os.mkdir(dir_name)
    os.chdir(f'./{dir_name}')

    with open('apartment.json', 'w') as file:
        file.write(json_string)

if __name__ == '__main__':
    args = parse_args()
    main(args.url, args.name)