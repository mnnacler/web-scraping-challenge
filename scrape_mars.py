from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests
from flask import Flask, render_template
#import time
#import numpy as np
#import json
#from selenium import webdriver

def scrape():

    #Mars News Titles
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_info = {}

    mars_info["title"] = soup.find('div', class_="content_title").get_text()
    mars_info["description"] = soup.find('div', class_="rollover_description_inner").get_text()


    #Mars Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(url)
    soup2 = BeautifulSoup(response.text, 'html.parser')


    image = soup2.find_all('a', class_='button fancybox')
    link1 = 'https://www.jpl.nasa.gov/'
    
    for results in image:
        link = results['data-fancybox-href']

    mars_info["featured_image_link"] = link1 + link


    #facts
    url='https://space-facts.com/mars/'
    response = requests.get(url)
    #soup3 = BeautifulSoup(response.text, 'html.parser')

    facts = pd.read_html(url)
    marsfacts = facts[0]
    marsTable = marsfacts.to_html()
    marsTable = marsTable.replace("\n","")

    mars_info["facts"] = marsTable


    #hemispheres
    hemisphere_image_urls = []

    #cerberus
    cUrl = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    response = requests.get(cUrl)
    soupC = BeautifulSoup(response.text, 'html.parser')
    cImage = soupC.find_all('div', class_="wide-image-wrapper")

    for image in cImage:
        picC = image.find('li')
        cFullImage = picC.find('a')['href']
    
    cTitle = soupC.find('h2', class_='title').get_text()
    cHem = {"Title": cTitle, "url": cFullImage}

    hemisphere_image_urls.append(cHem)

    #schiaparelli
    sUrl = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    response = requests.get(sUrl)
    soupS = BeautifulSoup(response.text, 'html.parser')
    sImage = soupS.find_all('div', class_="wide-image-wrapper")

    for image in sImage:
        picS = image.find('li')
        sFullImage = picS.find('a')['href']
    
    sTitle = soupS.find('h2', class_='title').get_text()
    sHem = {"Title": sTitle, "url": sFullImage}

    hemisphere_image_urls.append(sHem)

    #syrtis
    syUrl = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    response = requests.get(syUrl)
    soupSY = BeautifulSoup(response.text, 'html.parser')
    syImage = soupSY.find_all('div', class_="wide-image-wrapper")

    for image in syImage:
        picSY = image.find('li')
        syFullImage = picSY.find('a')['href']
    
    syTitle = soupSY.find('h2', class_='title').get_text()
    syHem = {"Title": syTitle, "url": syFullImage}

    hemisphere_image_urls.append(syHem)

    #valles
    vUrl = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    response = requests.get(vUrl)
    soupV = BeautifulSoup(response.text, 'html.parser')
    vImage = soupV.find_all('div', class_="wide-image-wrapper")

    for image in vImage:
        picV = image.find('li')
        vFullImage = picV.find('a')['href']
    
    vTitle = soupV.find('h2', class_='title').get_text()
    vHem = {"Title": vTitle, "url": vFullImage}

    hemisphere_image_urls.append(vHem)

    mars_info["hemisphere_image"] = hemisphere_image_urls

    return mars_info

