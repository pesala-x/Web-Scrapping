from bs4 import BeautifulSoup
import requests

pageToScrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(pageToScrape.text, "html.parser")

quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

"""
# this is simple code 
for quote in quotes:
    print(quote.text)
for author in authors:
    print(author.text)
"""
for quote, author in zip(quotes, authors):
    print(quote.text + " --> " + author.text)
