from selenium import webdriver
import os
from os.path import dirname, join
from termcolor import colored

# Browser webdriver and working directory setup
driverDir = join(join(dirname(dirname(os.getcwd())), "controller"), "drivers")


def setDriver(browser):
    try:
        if browser == "CHROME":
            driver = webdriver.Chrome(join(driverDir, "chromedriver.exe"))
        elif browser == "EDGE":
            driver = webdriver.Edge(join(driverDir, "msedgedriver.exe"))
        elif browser == "FIREFOX":
            driver = webdriver.Firefox(join(driverDir, "geckodriver.exe"))
        else:
            print(colored(
                "WARNING --- The browser name wasn't resolved properly: Google Chrome has been set up as the default "
                "browser.",
                "yellow"))
            driver = webdriver.Chrome(join(driverDir, "chromedriver.exe"))
    except:
        print(colored(
            "ERROR --- There was an issue while setting up the browser and webdriver, please confirm that the browser "
            "you're trying to run the tests on is actually installed on this device and that the webdriver saved "
            "under the \"drivers\" directory is for the same version of the browser you currently have installed.",
            "red"
        ))
        exit(1)
    else:
        print(colored(
            "The WebDriver was been correctly set up for the " + browser + " browser.",
            "blue"
        ))
        return driver
