import unittest
from time import sleep

from selenium import webdriver

# from HtmlTestRunner import Ht
from selenium.webdriver.common.by import By


class TestingMercadoLibre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./usr/bin/chromedriver")
        driver = self.driver
        driver.get("https://www.mercadolibre.com")
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element(By.ID, "CO")
        country.click()

        cookie_button = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[1]/div[2]/button[1]"
        )
        cookie_button.click()
        sleep(3)

        search_field = driver.find_element(By.NAME, "as_word")
        search_field.click()
        search_field.clear()
        search_field.send_keys("playstation 4")
        search_field.submit()
        sleep(3)

        location = driver.find_element(
            By.XPATH,
            '//*[@id="root-app"]/div/div[2]/aside/section/div[10]/ul/li[1]/a/span[1]',
        )
        location.click()
        sleep(3)

        condition = driver.find_element(By.PARTIAL_LINK_TEXT, "Nuevo")
        condition.click()
        sleep(3)

        order_menu = driver.find_element(
            By.CLASS_NAME, "andes-dropdown__display-values"
        )
        order_menu.click()
        higher_price = driver.find_element(
            By.CSS_SELECTOR,
            "#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span",
        )
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element(
                By.XPATH,
                f"/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2",
            ).text
            articles.append(article_name)
            article_price = driver.find_element(
                By.XPATH,
                f"/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]",
            ).text
            prices.append(article_price)

        print(articles, prices)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
