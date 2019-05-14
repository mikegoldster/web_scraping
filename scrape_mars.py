from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

# URL of page to be scraped
news_url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
response = requests.get(news_url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')

# Find and print headlines
news_title = soup.find('div', class_='content_title')
print(news_title.text)


#Find and print headline paragraph text
news_p = soup.find('div', class_='article_teaser_body')
print(news_p.text)

#JPL Mars Space Images - Featured Image
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA16613-1920x1200.jpg'

#Mars Weather
mars_weather = 'InSight sol 156 (2019-05-05) low -99.2ºC (-146.6ºF) high -18.1ºC (-0.6ºF) winds from the SW at 4.7 m/s (10.5 mph) gusting to 13.8 m/s (30.8 mph) pressure at 7.40 hPa'


#Mars Facts
factbook_url = 'https://space-facts.com/mars/'
facts_table = pd.read_html(factbook_url)
facts_table

#Mars Hemispheres
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]

mars_info = {
    "News_title": news_title,
    "News_p": news_p,
    "Featured Image": featured_image_url,
    "Weather": mars_weather,
    "Mars_descr": facts_table,
    "Hemis_dict": hemisphere_image_urls,
    "Date_time": date
}

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_info

    print("Executing scrape_mars function")
