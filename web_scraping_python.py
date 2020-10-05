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
# fix html for human eyes
html = html.decode('utf-8')
print(html)

# tags for quote
start_tag = '<span class="text" itemprop="text">'
end_tag = '”</span>'

quote_start_index = html.find(start_tag) + len(start_tag)
quote_start_index
quote_end_index = html.find(end_tag) -1
quote_end_index

# find quote
quote = html[quote_start_index:quote_end_index]
quote

# regular expressions
import re
exmple_str="We Are Data Magicians, Data science is magical. Let us show you the trick"
re.findall(r"Data", exmple_str)
re.findall(r"Movie", exmple_str)
exmple_str2="The winners are: winner1, winner2, winner3"
re.findall(r"winner\d", exmple_str2)

# find links example
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

# fix html for human eyes
fixed_html = html_soup.prettify()
html_soup.find_all("img",src = "media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg")
html_soup.find_all("a",href = "catalogue/category/books_1/index.html")

containers = html_soup.find_all("ul", {"class":'nav nav-list'})
type(containers)
containers[0].find_all("a")

# Scrapy
from scrapy import Selector
import requests
url = 'http://books.toscrape.com/'
html = requests.get(url).content

# SELECTOR
sel = Selector(text=html)
type(sel)

images_sel = sel.css('img')
type(images_sel)
images_sel[0].extract()

# spider
import scrapy
from scrapy.crawler import CrawlerProcess
url = 'http://books.toscrape.com/'


# The actual spider that tells which websites to scrape and how
class MySpider(scrapy.Spider):
    
    name = "spider_name"
    
    # Which site or sites we want to scrape and where to send the info from the site to be parsed 
    def start_requests(self):
        urls = [url]
        for i in urls:
            yield scrapy.Request(url = url, callback = self.parse)
    
    # Which data from the html to parse and how
    def parse(self, response):
        
        images = response.css('img').extract()
        
        # save to file
        html_file = "images_file.csv"
        with open(html_file, 'w') as f:
            f.writelines([image +'\n' for image in images])
            f.close()
        
        # if we wanted to parse the next links 
        # in the css command we give the css notation of a link
        # links = response.css('').extract()
        # for link in likns:
            # yield response.follow(url = link, callback = self.parse2)
    # def parse2(self, response):
        # parse next links

# initiate a CrwlerProcess
process = CrawlerProcess()

# tells the process which spider to use
process.crawl(MySpider)

# start the crawling process
process.start()






