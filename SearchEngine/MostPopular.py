import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from SearchByName import *

def top_five():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://www.kinopoisk.ru/lists/top250/")
        name = driver.find_elements_by_class_name("selection-film-item-meta__name")
        i = 0
        n = 5
        while i < n:
            if by_name(name[i].text) == '-1':
                n += 1
            i += 1      
        driver.close()
    except NoSuchElementException:
            driver.close()
            print("Sorry.")
    
