import unittest
from selenium import webdriver


class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element("id", "search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element("name", "q")

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element("class name", "input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element("class name", "button")

    def test_count_of_promo_banner_iamges(self):
        banner_list = self.driver.find_element("class name", "promos")
        banners = banner_list.find_elements("tag name", "img")
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element(
            "xpath",
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img',
        )

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element(
            "css selector", "div.header-minicart span.icon"
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
