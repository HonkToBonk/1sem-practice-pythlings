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

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.randomlists.com/random-movies")
name = driver.find_element_by_class_name('rand_medium').text
print(name)
driver.get("https://www.amazon.com/Amazon-Video/b?ie=UTF8&node=2858778011")
elem = driver.find_element_by_id("twotabsearchtextbox")
elem.clear()
elem.send_keys(name)
elem.send_keys(Keys.RETURN)
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
print(url)
driver.close()
