import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(60)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element("name", "q")
        search_field.clear()

        search_field.send_keys("tee")
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element("name", "q")

        search_field.send_keys("salt shaker")
        search_field.submit()

        products = driver.find_elements(
            "xpath",
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a',
        )
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
