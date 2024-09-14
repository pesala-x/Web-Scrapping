from bs4 import BeautifulSoup
import requests
import csv

pageToScrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(pageToScrape.text, "html.parser")

quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

"""
# this is simple code for get authors and quotes
for quote in quotes:
    print(quote.text)
for author in authors:
    print(author.text)
"""
"""
for quote, author in zip(quotes, authors):
    print(quote.text + " --> " + author.text)
"""

for quote, author in zip(quotes, authors):
    print(quote.text + " --> " + author.text)
    writer.writerow([quote.text, author.text])
    # file.close()
