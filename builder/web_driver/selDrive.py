from builder.web_driver import wdInit
from selenium import webdriver


class CommonFunctions:
    def __init__(self, driver):
        self.driver = driver

    def click(self, selectortype, selectorvalue):
        if selectortype == "ID":
            self.driver.find_element_by_id(selectorvalue).click()
        elif selectortype == "NAME":
            self.driver.find_element_by_name(selectorvalue).click()
        elif selectortype == "CLASS_NAME":
            self.driver.find_element_by_class_name(selectorvalue).click()
        elif selectortype == "XPATH":
            self.driver.find_element_by_xpath(selectorvalue).click()

    def typeTo(self, selectortype, selectorvalue, inputvalue):
        if selectortype == "ID":
            self.driver.find_element_by_id(selectorvalue).send_keys(inputvalue)
        elif selectortype == "NAME":
            self.driver.find_element_by_name(selectorvalue).send_keys(inputvalue)
        elif selectortype == "CLASS_NAME":
            self.driver.find_element_by_class_name(selectorvalue).send_keys(inputvalue)
        elif selectortype == "XPATH":
            self.driver.find_element_by_xpath(selectorvalue).send_keys(inputvalue)


class SelDrive:
    def __init__(self, url, browser="EDGE"):
        self.url = url
        self.browser = browser
        self.driver = wdInit.setDriver(browser)
        self.commons = CommonFunctions(self.driver)
        if self.browser == "CHROME":
            self.options = webdriver.ChromeOptions()
        elif self.browser == "EDGE":
            self.options = webdriver.IeOptions()
        elif self.browser == "FIREFOX":
            self.options = webdriver.FirefoxOptions()

    def launchSite(self, launchpref="reg"):
        if launchpref == "max":
            pass
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()
