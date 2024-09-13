import requests
from bs4 import BeautifulSoup
import csv
import time

def slicetext(text, start, end):
    try:
        return text.split(start)[1].split(end)[0]
    except IndexError:
        return ""

csv_file_path = 'patpat.csv'

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Land Size', 'Location', 'Total Price', 'Monthly Payment'])

for i in range(100):
    url = f'https://www.patpat.lk/property?page={i}&city=&sub_category=&sub_category_name=&category=property&search_txt=&sort_by='

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        cards = soup.find_all(class_='result-item')

        for card in cards:
            title = card.find(class_='result-title').text.strip()
            size = card.select_one('p.clearfix')
            location = slicetext(str(size), "<span class=\"d-block w-50 float-left\">\n<span class=\"hidden-on-mobile\">", "</span>").replace(".", "")
            sizee = slicetext(str(size), "d-block w-50 float-left\">", "</span>").replace(" ", "").replace("\n", " ").replace("<spanclass=\"hidden-on-mobile\">, ", " ")
            total = slicetext(str(card), "Total Price", "</p>")
            total = slicetext(total, "<span class=\"money\">", "</span>")
            mon = slicetext(str(card), "Monthly Payment", "</p>")
            mon = slicetext(mon, "<span class=\"money\">", "</span>")

            print("Title : ", title)
            print("Location : ", location)
            print("Size : ", sizee)
            print("Total : Rs.", total)
            print("Monthly : Rs.", mon)
            print("*" * 10)

            arr = [title, sizee, location, total, mon]
            with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(arr)
    else:
        print("Error to Get File")

    time.sleep(1)