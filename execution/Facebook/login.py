from builder.web_driver.selDrive import SelDrive
from execution.Facebook.contentMapping import loginD
import unittest

# Test Data
url = "https://www.facebook.com"
browser = "EDGE"
testmail = "loginfailuretest@any.com"
testpwd = "testpwd"


# Start Test
class FailedLogin(unittest.TestCase):
    def setUp(self):
        # Set up  the WebDriver
        self.fbwd = SelDrive(url, browser)
        self.fbwd.launchSite()

    def test_input_invalid_data(self):
        # Data setup
        error_msg_expected_val = "The email you’ve entered doesn’t match any account. Sign up for an account."

        self.fbwd.commons.typeTo("ID", loginD["email"]["id"], testmail)
        self.fbwd.commons.typeTo("ID", loginD["password"]["id"], testpwd)
        self.fbwd.commons.click("NAME", loginD["login_btn"]["name"])
        self.fbwd.driver.implicitly_wait(5)
        login_error_message = self.fbwd.driver.find_element_by_xpath('//*[@id="email_container"]/div[2]').text
        self.assertEquals(login_error_message, error_msg_expected_val)

    def tearDown(self):
        self.fbwd.close()


if __name__ == '__main__':
    unittest.main()
