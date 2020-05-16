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
    for i in range(1,0, -1):
            time.sleep(0.5)
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

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

in_actor = input(str('Actor: '))

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.imdb.com/?ref_=nv_home")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys(in_actor)
elem.send_keys(Keys.RETURN)
for i in range(1,0, -1):                                                #pause & wait to load
            time.sleep(0.5)
driver.find_element_by_link_text('Name').click()                       #make sure it's a movie
for i in range(1,0, -1):
            time.sleep(0.5)
driver.find_element_by_partial_link_text(in_actor).click()
films = driver.find_elements_by_class_name('knownfor-ellipsis')
i = 0
movie_list = []
while i < 10:
    movie_list.append(''.join(films[i].text))
    movie_list.append(''.join(films[i+2].text))
    i += 3

i = 0
while i < 7:
    print(movie_list[i] + movie_list[i + 1])
    print(find_movie(movie_list[i]))
    i += 2
driver.close()
