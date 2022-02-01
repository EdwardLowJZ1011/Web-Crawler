from selenium import webdriver
import numpy as np
import time

driver = webdriver.Chrome()
domain = 'https://www.google.com/search?q='
search = 'Web Scraping'
driver.get(domain+search)
time.sleep(5)

elm = [x.get_attribute('href') for x in driver.find_elements_by_tag_name('a') if x.get_attribute('href') != None]

for e in elm:
    print('Main URL', e)
    driver.get(e)
    time.sleep(5)
    url = np.unique([x.get_attribute('href') for x in driver.find_elements_by_tag_name('a') if x.get_attribute('href') != None and x.get_attribute('href').startswith('https')]).tolist()
    print('Sub URL', url)

driver.quit()
