import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from SearchByName import *

def by_year(year):
    if int(year) < 1895:
        return '-1'
    else:
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")

        try:
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("https://www.kinopoisk.ru/lists/navigator/" + year + '-' + year +"/?quick_filters=films&tab=all")
            for i in range(1,0, -1):
                        time.sleep(0.5)
            get_films = driver.find_elements_by_class_name("selection-film-item-meta__name")
            i = 0
            films = []
            while i < 20:
                films.append(get_films[i].text)
                i += 1
            driver.close()
            n = 5
            i = 0
            while i < n and n < 20:
                if by_name(films[i]) == '-1':
                    n += 1
                i += 1
        except NoSuchElementException:
                    return "-1"
    
