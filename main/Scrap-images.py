import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Create a directory to save downloaded images
if not os.path.exists('images'):
    os.makedirs('images')

# Find all image tags
images = soup.find_all('img')

# Loop through the images and download them
for img in images:
    img_url = img.get('src')
    if not img_url:
        continue

    # Handle relative URLs
    img_url = urljoin(url, img_url)

    # Send request to the image URL
    img_response = requests.get(img_url)

    # Get the image file name
    img_name = os.path.basename(img_url)

    # Save the image
    with open(f'images/{img_name}', 'wb') as f:
        f.write(img_response.content)

    print(f"Downloaded{img_name}")