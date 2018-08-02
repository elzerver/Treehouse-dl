import sys
from bs4 import BeautifulSoup

html = open("/home/aldo/Documentos/projects/Treehouse-dl/themes.html", "r")
print(html.read())

# Creating the beautifulsoup object
data = html.text(html)

# create the html scraper object
soup = BeautifulSoup(data, 'html.parser')