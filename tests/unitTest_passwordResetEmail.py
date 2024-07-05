import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        email = "rtomaso@unomaha.edu"
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[contains(., 'Login')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[contains(@href, '/accounts/password_reset/')]").click()
        time.sleep(3)
        elem = driver.find_element(By.ID,"id_email")
        elem.send_keys(email)
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)


        try:
            # verify Password Email has been sent and message shows by looking for part of the message
            content: str = driver.page_source
            content.find('emailed you instructions')
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Email confirmation was not sent and confirmation message cannot be seen.")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
