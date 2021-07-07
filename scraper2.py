import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/path/to/chromedriver')
search = ['mtg']
for result in search:
    driver.get("https://www.amazon.com.mx/")
    e = driver.find_element_by_id('searchfor')
    e.send_keys(book)
    e.send_keys(Keys.ENTER)
