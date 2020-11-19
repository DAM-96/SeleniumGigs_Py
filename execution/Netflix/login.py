from builder.web_driver.selDrive import SelDrive
from execution.Netflix.contentMapping import *
import unittest

# Test Data initialization
url = ""
browser = ""
testmail = "loginfailuretest@auto.com"
testpwd = ""


# Start Test
class FailedLogin(unittest.TestCase):
    def setUp(self):
        # Set up  the WebDriver
        url = "https://www.netflix.com"
        browser = "EDGE"
        self.fbwd = SelDrive(url, browser)
        self.fbwd.launchSite()

    def test_input_invalid_data_no_mail(self):
        # Data setup
        testmail = ""
        testpwd = "testpwd"
        error_msg_expected_val = "Please enter a valid email or phone number."

        self.fbwd.driver.maximize_window()
        self.fbwd.commons.click("CLASS_NAME","close-button")
        self.fbwd.driver.find_element_by_link_text(signupD["signin_btn"]["value"]).click()
        self.fbwd.driver.implicitly_wait(5)
        self.fbwd.commons.typeTo("ID", signinD["email"]["id"], testmail)
        self.fbwd.commons.typeTo("ID", signinD["password"]["id"], testpwd)
        self.fbwd.commons.click("XPATH",'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
        self.fbwd.driver.implicitly_wait(5)
        login_error_message = self.fbwd.driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div['
                                                                     '3]/div/div/div[1]/form/div[1]/div[2]').text
        self.assertEquals(login_error_message, error_msg_expected_val)

    def test_input_invalid_data_no_pass(self):
        # Data setup
        testmail = "loginfailuretest@auto.com"
        testpwd = ""
        error_msg_expected_val = "Your password must contain between 4 and 60 characters."

        self.fbwd.driver.maximize_window()
        self.fbwd.commons.click("CLASS_NAME", "close-button")
        self.fbwd.driver.find_element_by_link_text(signupD["signin_btn"]["value"]).click()
        self.fbwd.driver.implicitly_wait(5)
        self.fbwd.commons.typeTo("ID", signinD["email"]["id"], testmail)
        self.fbwd.commons.typeTo("ID", signinD["password"]["id"], testpwd)
        self.fbwd.commons.click("XPATH", '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
        self.fbwd.driver.implicitly_wait(5)
        login_error_message = self.fbwd.driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div['
                                                                     '3]/div/div/div[1]/form/div[2]/div[2]').text
        self.assertEquals(login_error_message, error_msg_expected_val)

    def tearDown(self):
        self.fbwd.close()


if __name__ == '__main__':
    unittest.main()
