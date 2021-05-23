from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import config
import re
import helper.helper as helper


def send():
    response_dict = helper.get_hadith()
    send_body = re.sub('<[^<]+?>', '', response_dict["hadith"][0]["body"])

    send_hadith_header = "*Collection*: {}, *Book*: {}, *Hadith Number*: {}, " \
                         "*Chapter Number*: {}".format(response_dict["collection"], response_dict["bookNumber"],
                                                       response_dict["hadithNumber"],
                                                       response_dict["hadith"][0]["chapterNumber"])
    send_hadith_title = "*Chapter Title*: {}".format(response_dict["hadith"][0]["chapterTitle"])
    send_hadith_content = "\"{}\"".format(send_body)

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", config.port)
    driver = webdriver.Chrome(config.chrome_driver, options=chrome_options)
    driver.get(config.web)

    # WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, config.new_chat)))

    for contact in config.contacts:
        helper.click(driver, config.new_chat)
        helper.send(driver, config.search, contact)
        helper.click(driver, config.first_contact)
        helper.send(driver, config.message, config.greeting)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, send_hadith_header)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, send_hadith_title)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, send_hadith_content)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, config.footer)
        helper.send(driver, config.message, Keys.ENTER)


if __name__ == "__main__":
    send()
