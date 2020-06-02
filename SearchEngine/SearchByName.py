import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

def by_name(in_name):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.kinopoisk.ru/")
    elem = driver.find_element_by_name("kp_query")
    elem.clear()
    elem.send_keys(in_name)
    elem.send_keys(Keys.RETURN) 
    for i in range(1,0, -1):
                time.sleep(0.5)
    try:
        driver.find_element_by_partial_link_text(in_name).click()
        for i in range(1,0, -1):
            time.sleep(0.5)
        name = driver.find_element_by_tag_name("h1").text
        print(name)
        get_data = driver.find_elements_by_tag_name("tr")
        print(''.join(get_data[0].text))
        get_stars = driver.find_elements_by_tag_name("li")
        print(get_stars[4].text)
        print(get_stars[5].text)
        print(get_stars[6].text)
        driver.find_element_by_id("online-view-options-watch-button").click()
        for i in range(1,0, -1):
                    time.sleep(0.5)
        url = driver.current_url
        driver.close()
        print(url)
    except NoSuchElementException:
        driver.close()
        return '-1'
