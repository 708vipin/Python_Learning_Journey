#To install Beautifulsoup run the command in terminal
#To install lxml parser
#html5lib is also a popular parser, but here we are going to use lxml
#To install requests
#You don't have to be extremely familiar with HTML to scrape 

from bs4 import BeautifulSoup
import requests

source = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(source, "lxml")

article_title = soup.find_all(class_="titleline")

for title in article_title:
    print(title.prettify())

