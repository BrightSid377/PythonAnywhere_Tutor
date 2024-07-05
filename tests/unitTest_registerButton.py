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
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Sign Up").click()
        time.sleep(5)

        try:
            # verify Sign Up button directs to Register page by locating the username field.
            driver.find_element(By.ID, "id_username")
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Sign Up Button does not lead to registration")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
