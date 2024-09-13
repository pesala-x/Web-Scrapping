import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # find the all content in the given tag
    tags = soup.find(id="table_of_content")
    for tag in tags:
        print(tag.text.strip())
else:
    print("Error fetching the webpage")
