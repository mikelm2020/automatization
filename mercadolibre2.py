import unittest

from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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

        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[2]/div[1]/div[2]/button[1]")
            )
        )
        cookie_button.click()

        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "as_word"))
        )
        search_field.click()
        search_field.clear()
        search_field.send_keys("playstation 4")
        search_field.submit()

        location = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="root-app"]/div/div[2]/aside/section/div[10]/ul/li[1]/a/span[1]',
                )
            )
        )
        location.click()

        condition = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Nuevo"))
        )
        condition.click()

        order_menu = driver.find_element(
            By.CLASS_NAME, "andes-dropdown__display-values"
        )
        order_menu.click()

        higher_price = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span",
                )
            )
        )
        higher_price.click()

        products = {}

        for i in range(5):
            article_name = driver.find_element(
                By.XPATH,
                f"/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2",
            ).text

            article_price = driver.find_element(
                By.XPATH,
                f"/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]",
            ).text
            products[article_name] = article_price

        print(products)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(output="reports", report_name="mercadolibre"),
    )
