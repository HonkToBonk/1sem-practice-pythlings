import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

def find_movie(name):
    driver.get("https://www.amazon.com/Amazon-Video/b?ie=UTF8&node=2858778011")
    elem = driver.find_element_by_id("twotabsearchtextbox")
    elem.clear()
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)
    for i in range(1,0, -1):
        time.sleep(0.2)
    try:
        driver.find_element_by_link_text(name).click()
        url = driver.current_url
    except NoSuchElementException:
        try:
            driver.find_element_by_partial_link_text(name).click()
            for i in range(1,0, -1):
                time.sleep(0.2)
            url = driver.current_url
        except NoSuchElementException:
            url = driver.current_url
    return url

def get_string(element):
    string = ''.join(element)
    return string

in_year = input(str('Year: '))

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.films101.com/years.htm")
driver.find_element_by_link_text(in_year).click()
films = driver.find_elements_by_class_name('zt1')
years = driver.find_elements_by_class_name('zy1')
for i in range(1,0, -1):
    time.sleep(0.5)
hej = []
year = []
for d in range(len(films)):
    hej.append(films[d].text)
for d in range(len(years)):
    year.append(years[d].text)
j = 0
i = 0
film = []
n = 10
while j < n:
    for i in range(1,0, -1):
        time.sleep(0.2)
    string = get_string(hej[j])
    print(string + ' ' + year[j])
    print(find_movie(string))
    film.clear()
    j += 1
    i = 0

driver.close()   
    
