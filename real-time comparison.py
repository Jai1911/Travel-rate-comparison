from urllib import response
from bs4 import BeautifulSoup
import requests

origin = input("Enter the place of origin: ")
destination = input("Enter the desired destination: ")


url = "https://www.rome2rio.com/map/"+origin+"/"+destination+"#trips"
page = requests.get(url)
page.raise_for_status()
soup = BeautifulSoup(page.text, 'html.parser')
segments = soup.find_all('div', class_='route__segment')

travel_data = []
for segment in segments:
            mode_name = segment.find('div', class_='route__mode').text.strip()
            cost = segment.find('span', class_='route__price').text.strip()
            time = segment.find('span', class_='route__duration').text.strip()

            print(f"Mode of travel: {mode_name} | Estimated cost: {cost} | Estimated time: {time}")


cost = float(cost.split()[0].replace(',', ''))

travel_info = {
    'mode': mode_name,
    'cost': cost,
    'time': time
}

travel_data.append(travel_info)
sorted_travel_data = sorted(travel_data, key=lambda x: x['cost'])

for info in sorted_travel_data:
    print(f"Mode of travel: {info['mode']} | Estimated cost: {info['cost']} | Estimated time: {info['time']}")





