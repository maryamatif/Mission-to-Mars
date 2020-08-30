#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[5]:


# Path to chromedriver
get_ipython().system('which chromedriver')


# In[6]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)


# In[7]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[8]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[9]:


slide_elem.find("div", class_='content_title')


# In[10]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[11]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[12]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[13]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[14]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[15]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[16]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[17]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[18]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[19]:


df.to_html()


# In[20]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[21]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')
slide_elem


# In[22]:


slide_elem.find("div", class_='content_title')


# In[23]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[24]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[25]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[26]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[27]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[28]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[29]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[30]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ### Mars Facts

# In[31]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[32]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[33]:


df.to_html()


# ### Mars Weather

# In[34]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[35]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[36]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[37]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[38]:


html = browser.html
test_soup = soup(html, 'html.parser')


# In[39]:


results = test_soup.find_all("div", class_='item')
results


# In[53]:


# Loop through returned results

hemisphere_image_urls = [];

for result in results:
    # Error handling
    try:
        # Identify and return title of listing
        title = result.find('h3').text
        # Identify and return link to listing
        link = result.a['href']     
    # Print results only if title, price, and link are available
        if (title and link):
            print('-------------')
            print('title is ', title)
            first_image = f"https://astrogeology.usgs.gov{link}"
            browser.visit(first_image)
            html = browser.html
            new_soup = soup(html, 'html.parser')
            fancies = new_soup.find_all("div", class_='downloads')
            for fancy in fancies:
                hemispheres = {};
                link = fancy.a['href']
                hemispheres.update({'img_url':str(link)})
                hemispheres.update({'title':str(title)})
                hemisphere_image_urls.append(hemispheres)
                print('link',please)
                

    except AttributeError as e:
        print(e)


# In[58]:


# Loop through returned results

hemisphere_image_urls = [];

for result in results:
    # Error handling
    try:
        # Identify and return title of listing
        title = result.find('h3').text
        # Identify and return link to listing
        link = result.a['href']
        first_image = f"https://astrogeology.usgs.gov{link}"
        browser.visit(first_image)
        html = browser.html
        new_soup = soup(html, 'html.parser')
        fancies = new_soup.find_all("div", class_='downloads')
        for fancy in fancies:
                hemispheres = {};
                url_link = fancy.a['href']
                hemispheres.update({'img_url':str(url_link)})
                hemispheres.update({'title':str(title)})
                hemisphere_image_urls.append(hemispheres)

        # Print results only if title, price, and link are available
        if (title and link):
            print('-------------')
            print('title is ', title)
            print('url_link', url_link)
                

    except AttributeError as e:
        print(e)


       


# In[59]:


hemisphere_image_urls


# In[61]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




