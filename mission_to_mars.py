# Dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import time
import requests

def scrape():
    try:
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
        time.sleep(5)
        html_image = browser.html
        soup = bs(html_image, 'html.parser')
        image_path = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
        featured_image_url = 'https://www.jpl.nasa.gov' + image_path
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
        scrape_table = pd.read_html(factbook_url)
        scrape_table[0]
        mars_facts_df = scrape_table[0]
        mars_facts_df.rename(columns={0: 'Fact', 1: "Value"}, inplace=True)
        mars_facts_df.set_index('Fact')
        facts_table = mars_facts_df.to_html(index=False)
        facts_table.replace('\n', '')
        mars_info["facts_table"] = facts_table
        #Mars Hemispheres
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(usgs_url)
        html = browser.html
        soup = bs(html, 'html.parser')
        hemispheres = soup.find_all('div', class_='item')
        hemisphere_img_urls =[]
        for result in hemispheres:
            try:
                img_title = result.find('h3').text
                partial = result.find('a', class_='itemLink product-item')['href']
                img_url = 'https://astrogeology.usgs.gov'+ partial
                hemisfind = requests.get(img_url)
                soup = bs(hemisfind.text, 'html.parser')

                try:
                    hemis_dl = soup.find('div', class_='downloads')
                    hemis_href = hemis_dl.find('a')['href']
                    hemisphere_img_urls.append({'title': img_title, 'img_url': hemis_href})

                except Exception as f:
                    print('f: ', f)

            except Exception as e:
                print('e: ', e)

        mars_info['hemisphere_img_urls'] = hemisphere_img_urls
        return mars_info

    finally:
        browser.quit()
