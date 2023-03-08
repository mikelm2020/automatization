import unittest

from google_page import GooglePage
from selenium import webdriver


class GoogleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="./usr/bin/chromedriver")

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search("Platzi")

        self.assertEqual("Platzi", google.keyword)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
