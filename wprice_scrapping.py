#!/usr/bin/env python

import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time
import datetime


def get_html(url):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    try:
        driver.get(url)
        time.sleep(3)

        with open('./price_page.html', 'w') as file:
            file.write(driver.page_source)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def find_price(file_path):
    with open(file_path) as file:
        src = file.read()

    soup = bs(src, 'lxml')
    price_div = soup.find('div', class_='product-buy__price')
    return price_div.text


def main():
    URL = 'https://www.dns-shop.ru/product/4940593d45ad3332/nausniki-tws-samsung-buds-pro-cernyj/'
    FILE_PATH = './price_page.html'
    get_html(URL)
    price = f'Цена наушников на {datetime.date.today()} составляет {find_price(FILE_PATH)}'
    print(price)


if __name__ == "__main__":
    main()
