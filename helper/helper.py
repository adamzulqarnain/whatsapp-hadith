from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
import config
import requests
import json


def get_hadith():
    response = requests.get(config.api, headers=config.headers)
    response_dict = json.loads(response.text)
    return response_dict


def click(driver, elem):
    time.sleep(0.5)
    delay = 5
    WebDriverWait(driver, delay).until(expected_conditions.element_to_be_clickable((By.XPATH, elem)))
    driver.find_element_by_xpath(elem).click()


def send(driver, elem, *key):
    driver.find_element_by_xpath(elem).send_keys(key)
