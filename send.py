from selenium.webdriver.common.keys import Keys
from configuration import config, contacts
import helper.helper as helper


def send():
    driver = helper.setup()
    for contact in contacts.contacts:
        header, hadith, title, content = helper.get_hadith()
        helper.click(driver, config.new_chat)
        helper.send(driver, config.search, contact)
        helper.click(driver, config.first_contact)
        helper.send(driver, config.message, config.greeting)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, header)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, hadith)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, title)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, "--")
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, content)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, Keys.ALT, Keys.ENTER)
        helper.send(driver, config.message, config.footer)
        helper.send(driver, config.message, Keys.ENTER)


if __name__ == "__main__":
    send()
