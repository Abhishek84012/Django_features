from urllib.request import Request

import lxml
from bs4 import BeautifulSoup


# BeautifulSoup
# lxml
# html5lib
# requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

# avo div k jeno class footer hoy(first div)    
match = soup.find('div',class_='footer')["src"]
match.h2.a.text

match = soup.find_all('div',class_='footer')

soup.find('article')
