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

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

in_genre = input(str('Genre: '))

if not in_genre.istitle():
    in_genre = in_genre.capitalize()

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
driver.find_element_by_link_text(in_genre).click()
films = driver.find_elements_by_class_name('lister-item-header')
for i in range(1,0, -1):
    time.sleep(0.5)
hej = []
for d in range(len(films)):
    hej.append(films[d].text)
j = 0
i = 0
film = []
n = 10
while j < n:
    for i in range(1,0, -1):
        time.sleep(0.2)
    string = get_string(hej[j])
    while not (string[i]).isalpha():
        i += 1
    while not string[i] == '(':
        film.append(string[i])
        i += 1
    name = ''.join(film)
    while not string[i] == ')':
        film.append(string[i])
        i += 1
    film.append(string[i])
    print(''.join(film))
    print(find_movie(name))
    film.clear()
    j += 1
    i = 0

driver.close()   
    
