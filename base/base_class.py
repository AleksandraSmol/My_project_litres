import datetime
import re


class Base():

    # В классе Base хранится wevdriver
    def __init__(self, driver):
        self.driver = driver


    '''Метод получения текущего url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')


    '''Метод проверки по слову'''

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')
        print(value_word)
        # return self


    '''Метод получения скриншотов'''

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y.%m.%d_%H:%M:%S')
        name_screenshot = f'./screenshots/screenshot {now_date}.png'
        self.driver.save_screenshot(name_screenshot)


    '''Метод проверки по url'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')


    '''Метод очистки цены от знаков валюты'''
    # В методе используется регулярное выражение re.sub()

    def clean_price(self, price):
        price_with_sign = price
        price_without_currency = re.sub(r'\D', '', price_with_sign)
        return int(price_without_currency)