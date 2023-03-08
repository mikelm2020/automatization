import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LanguageOptions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_select_language(self):
        exp_options = ["English", "French", "German"]
        act_options = []
        select_language = Select(self.driver.find_element(By.ID, "select-language"))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        self.assertEqual(exp_options, act_options)

        self.assertEqual("English", select_language.first_selected_option.text)

        select_language.select_by_visible_text("German")

        self.assertTrue("store=german" in self.driver.current_url)

        select_language = Select(self.driver.find_element(By.ID, "select-language"))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
