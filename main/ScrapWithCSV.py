import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    topic = soup.find_all('h2')

    # Extract content (p tags)
    topic_content = soup.find_all('p')

    # Prepare the list of data to write to CSV
    data = []

    for i, topic in enumerate(topic):
        if i < len(topic_content):  # Ensure content exists for the topic
            data.append({
                'Topic': topic.text.strip(),
                'Content': topic_content[i].text.strip()
            })
    filename = 'geeksforgeeks_algorithms.csv'
    # Open CSV file for writing
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Topic', 'Content'])
        writer.writeheader()

        # Write each row to CSV
        for row in data:
            writer.writerow(row)

    print(f"Data has been written to {filename}")

else:
    print("Failed to retrieve the page")