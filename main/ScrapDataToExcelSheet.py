import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'https://www.geeksforgeeks.org/fundamentals-of-algorithms/'

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract Table of Contents
toc_div = soup.find('div', {'id': 'table_of_content'})
toc_items = toc_div.find_all('li')

toc_data = []
for item in toc_items:
    link = item.find('a')
    title = link.get_text()
    href = link.get('href')
    toc_data.append([title, href])

# Extract Sections
section_data = []
sections = soup.find_all('h2')
for section in sections:
    section_title = section.get_text()
    section_id = section.get('id')
    section_content = ""
    content = section.find_next_sibling()
    while content and content.name not in ['h2', 'h3']:
        if content.name == 'p':
            section_content += content.get_text() + "\n"
        elif content.name == 'ul':
            for li in content.find_all('li'):
                section_content += "- " + li.get_text() + "\n"
        content = content.find_next_sibling()
    section_data.append([section_title, section_id, section_content.strip()])

# Convert data into pandas DataFrames
toc_df = pd.DataFrame(toc_data, columns=['Title', 'URL'])
sections_df = pd.DataFrame(section_data, columns=['Title', 'ID', 'Content'])

# Save DataFrames to Excel
with pd.ExcelWriter('scraped_data.xlsx') as writer:
    toc_df.to_excel(writer, sheet_name='Table of Contents', index=False)
    sections_df.to_excel(writer, sheet_name='Sections', index=False)

print("Scraped data successfully saved to Excel!")

#  # Save DataFrames to Excel with a different file name
# with pd.ExcelWriter('scraped_data_v2.xlsx') as writer:
#     toc_df.to_excel(writer, sheet_name='Table of Contents', index=False)
#     sections_df.to_excel(writer, sheet_name='Sections', index=False)
