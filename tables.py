import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

COLUMN_NUMBER = 5
ROW_NUMBER = 4

class Tables(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./usr/bin/chromedriver")
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

    def test_sort_tables(self):
        driver = self.driver

        table_data = [[] for i in range(COLUMN_NUMBER)]
        print(table_data)

        for i in range(COLUMN_NUMBER):
            header = driver.find_element(
                By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span'
            )
            table_data[i].append(header.text)

            for j in range(ROW_NUMBER):
                row_data = driver.find_element(
                    By.XPATH, f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]'
                )
                table_data[i].append(row_data.text)

        print(table_data)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
