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
    try:
        driver.find_element_by_link_text(name).click()
        for i in range(1,0, -1):
            time.sleep(0.5)
        url = driver.current_url
    except NoSuchElementException:
        try:
            driver.find_element_by_partial_link_text(name).click()
            for i in range(1,0, -1):
                time.sleep(0.5)
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

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")
films = driver.find_elements_by_class_name('titleColumn')
hej = []
for d in range(len(films)):
    hej.append(films[d].text)
j = 0
i = 0
film = []
n = 10
check = 0
while j < n:
    string = get_string(hej[j])
    while not string[i] == '(':
        film.append(string[i])
        i += 1
    name = ''.join(film)
    while not string[i] == ')':
        film.append(string[i])
        i += 1
    film.append(string[i])
    if not '2020' in ''.join(film):
        print(''.join(film))
        print(find_movie(name))
        check = 1
    film.clear()
    j += 1
    i = 0
    if check == 0:
        n += 1
    check = 0
    
driver.close()   
    
