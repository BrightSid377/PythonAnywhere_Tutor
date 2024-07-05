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
        user = "testuser"
        pwd = "test123"
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)

        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)


        try:
            # verify Log in was successful by locating Log Out button
            driver.find_element(By.XPATH, '//button[text()="Log out"]')
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Log In was not successful")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
