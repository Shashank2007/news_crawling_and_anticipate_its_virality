# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:35:42 2020

@author: hp
"""

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="http://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("_"*60)