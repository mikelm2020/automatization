import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(60)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_laguage_option(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == "__main__":
    unittest.main(verbosity=2)
