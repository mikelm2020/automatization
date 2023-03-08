import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_account_link(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            lambda s: s.find_element(By.ID, "select-language").get_attribute("length")
            == "3"
        )

        account = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "ACCOUNT"))
        )
        account.click()

    def test_create_new_customer(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "ACCOUNT").click()

        my_account = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "My Account"))
        )
        my_account.click()

        create_account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "CREATE AN ACCOUNT"))
        )
        create_account_button.click()

        WebDriverWait(driver, 10).until(
            EC.title_contains("Create New Customer Account")
        )

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
