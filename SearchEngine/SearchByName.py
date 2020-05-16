import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

in_name = input(str("Name: "))

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.imdb.com/?ref_=nv_home")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys(in_name)
elem.send_keys(Keys.RETURN)
for i in range(1,0, -1):                                                #pause & wait to load
            time.sleep(0.5)
driver.find_element_by_link_text('Movie').click()                       #make sure it's a movie
for i in range(1,0, -1):
            time.sleep(0.5)
driver.find_element_by_partial_link_text(in_name).click()
for i in range(1,0, -1):
            time.sleep(0.5)
name = driver.find_element_by_tag_name("h1").text                                                                 #name and year
get_stars = driver.find_elements_by_class_name('credit_summary_item')
i = 0
stars = []
while not((get_stars[2].text)[i] == '|'): 
    stars.append((get_stars[2].text)[i])
    i += 1
just_name = []
i = 0
while not (name[i] == '('):
    just_name.append(name[i])
    i += 1
driver.get("https://www.amazon.com/Amazon-Video/b?ie=UTF8&node=2858778011")
elem = driver.find_element_by_id("twotabsearchtextbox")
elem.clear()
elem.send_keys(''.join(just_name))
for i in range(1,0, -1):
            time.sleep(0.5)
elem.send_keys(Keys.RETURN)
for i in range(1,0, -1):
    time.sleep(0.5)
try:
    driver.find_element_by_link_text(''.join(just_name)).click()
    url = driver.current_url
except NoSuchElementException:
    try:
        driver.find_element_by_partial_link_text(''.join(just_name)).click()
        for i in range(1,0, -1):
            time.sleep(0.2)
        url = driver.current_url
    except NoSuchElementException:
        url = driver.current_url
driver.close()
print(name)
print(''.join(stars))  
print(url)
