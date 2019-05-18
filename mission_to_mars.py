# Dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import time

def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    #Empty dictionary to contain the scraped Data
    mars_info = {}
    # URL of page to be scraped
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')
    headlines = soup.find('li', class_='slide')
    # Find headlines
    news_title = headlines.find(class_='content_title').text
    #Find headline paragraph text
    news_p = headlines.find(class_='article_teaser_body').text
    browser.quit()
    #Add to the dictionary
    mars_info["news_title"] = news_title
    mars_info["news_p"] = news_p
    #JPL Image
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    html = browser.html
    soup = bs(html, 'html.parser')
    image_path = soup.find('figure', class_='lede').a['href']
    featured_image_url = "https://www.jpl.nasa.gov/" + image_path
    browser.quit()
    mars_info["featured_image_url"] = featured_image_url
    #Mars Weather
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    weather_tweet = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    browser.quit()
    mars_info["weather_tweet"] = weather_tweet
    #Mars Facts
    factbook_url = 'https://space-facts.com/mars/'
    facts_table = pd.read_html(factbook_url)
    mars_info["facts_table"] = facts_table
    # #Mars Hemispheres
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)
    # usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # browser.visit(usgs_url)
    # html = browser.html
    # soup = bs(html, 'html.parser')
    # hemisphere_image_urls =[]
    # for item in range (4):
    #     time.sleep(5)
    #     images = browser.find_by_tag('h3')
    #     images[item].click()
    #     html = browser.html
    #     soup = bs(html, 'html.parser')
    #     partial = soup.find("img", class_="wide-image")["src"]
    #     img_title = soup.find("h2",class_="title").text
    #     img_url = 'https://astrogeology.usgs.gov'+ partial
    #     dictionary={"title":img_title,"img_url":img_url}
    #     hemisphere_image_urls.append(dictionary)
    #     browser.back()
    # browser.quit()
    # mars_info['hemisphere_image_urls'] = hemisphere_image_urls
    return mars_info
