# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 23:38:09 2022

@author: Thakral's
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url ='https://www.ebay.com/sch/i.html?_from=R40&_nkw=canon&_sacat=0&rt=nc&LH_PrefLoc=98'

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    return soup

def parse(soup):
    productslist = []
    results = soup.find_all('div', class_='s-item__info clearfix')
    for item in results:
        
        
        products = {
            
        'title': item.find('h3' , class_='s-item__title').text,
        'soldprice': item.find('span' , class_='s-item__price').text.replace('$','').replace(',','').strip()
        
            
        }
        
        productslist.append(products)
    return productslist
    

def output(productslist):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv('output.csv' , index=False)
    print('Saved to Csv')
    return 


soup = get_data(url)
productslist = parse(soup)
output(productslist)
