# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:26:45 2020

@author: Ariel
"""

# retrieve the HTML data from the domain name

# urllib
from urllib.request import urlopen
page = urlopen('http://quotes.toscrape.com/random')
page
html = page.read()
html

# requests
import requests
url = 'http://quotes.toscrape.com/random'
html = requests.get(url).content
html

# Parse the data in the desired format
# Simple methods 

# String methods
html = html.decode('utf-8')
print(html)

start_tag = '<span class="text" itemprop="text">'
end_tag = '”</span>'

quote_start_index = html.find(start_tag) + len(start_tag)
quote_start_index
quote_end_index = html.find(end_tag) -1
quote_end_index

quote = html[quote_start_index:quote_end_index]
quote

# regular expressions
import re
exmple_str="We Are Data Magicians, Data science is magical. Let us show you the trick"
re.findall(r"Data", exmple_str)
re.findall(r"Movie", exmple_str)
exmple_str2="The winners are: winner1, winner2, winner3"
re.findall(r"winner\d", exmple_str2)

regex = r"http\S+"
re.findall(regex,html)

regex2 = r'http[\'"s]?://([^\'" >]+)'
re.findall(regex2,html)

# HTML Parser
# Beautiful Soup
from bs4 import BeautifulSoup as Soup
import requests
url = 'http://books.toscrape.com/'
html = requests.get(url).content
html_soup = Soup(html,"html.parser")
type(html_soup)


# basic call tags
html_soup.title
html_soup.article.div.a

# get text
text = html_soup.get_text()
text = text.replace('\n', '')
text

# find_all, image example
list_img = html_soup.find_all("img")
list_img[0]
image = list_img[0]
type(image)
image.name
image['alt']

html_soup.find_all("img",src = "media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg")
html_soup.find_all("a",href = "catalogue/category/books_1/index.html")

containers = html_soup.find_all("ul", {"class":'nav nav-list'})
type(containers)
containers[0].find_all("a")

# Scrapy
# from scrapy import Selector
# sel = Selector(text=html)

# save to csv
filename = "web_scraping_result.csv"
f = open(filename,"W")
headers = "header1, header2, header3\n"
f.write(headers)