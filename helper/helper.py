from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import config
import requests
import json
import re
import time


def setup():
    """
    Setup selenium driver, open chrome browser and navigate to whatsapp for web
    :return: driver obj
    """
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", config.port)
    driver = webdriver.Chrome(config.chrome_driver, options=chrome_options)
    driver.get(config.web)
    return driver


def get_hadith():
    """
    Requests random hadith via REST from www.sunnah.com API
    :return: header, title, content of hadith
    """
    response = requests.get(config.api, headers=config.headers)
    response_dict = json.loads(response.text)
    send_body = re.sub('<[^<]+?>', '', response_dict["hadith"][0]["body"])

    header = "*Collection*: {}, *Book*: {}, *Hadith Number*: {}, *Chapter Number*: {}"\
        .format(response_dict["collection"], response_dict["bookNumber"], response_dict["hadithNumber"],
                response_dict["hadith"][0]["chapterNumber"])
    title = "*Chapter Title*: {}".format(response_dict["hadith"][0]["chapterTitle"])
    content = "\"{}\"".format(send_body)
    return header, title, content


def click(driver, elem):
    """
    Waits for element to be clickable then clicks it on page
    :param driver: driver obj
    :param elem: element on page
    :return: None
    """
    time.sleep(0.5)  # needed to wait for elem to completely load
    delay = 10
    WebDriverWait(driver, delay).until(expected_conditions.element_to_be_clickable((By.XPATH, elem)))
    driver.find_element_by_xpath(elem).click()


def send(driver, elem, *key):
    """
    Sends key(s) to element on page
    :param driver: driver obj
    :param elem: element on page
    :param key: key(s) to be sent to element
    :return: None
    """
    driver.find_element_by_xpath(elem).send_keys(key)
