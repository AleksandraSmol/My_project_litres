import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


# Класс SearchPage представляет страницу с найденными по запросу книгами веб-приложения litres.ru и наследуется от класса Base
class SearchPage(Base):

    # Класс SearchPage содержит метод init, который инициализирует объект класса SearchPage и принимает в качестве
    # параметра объект driver.
    # Функция super вызывает метод init родительского класса Base, чтобы инициализировать
    # driver и использовать его в других методах класса SearchPage
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    '''Variables'''
    # Переменные с названиями товаров

    book_title = 'Шоколад'
    input_title = 'до камерных посиделок'


    '''Locators'''
    # Переменные с локаторами на странице найденных книг

    locator_new_book = '(//p[@class="ArtInfo-modules__title_MkOVH" and text()="Шоколад"])[1]'
    locator_first_book = '//a[@data-test-id="art__title--desktop"]'
    locator_search = '//input[@data-test-id="header__search-input--desktop"]'
    locator_result_search = '//h1[@data-test-id="search-title__wrapper"]'
    locator_button_search = '//button[@data-test-id="header__search-button--desktop"]'
    locator_checkbox_format_text = '//label[text()="Текст"]'
    locator_checkbox_lang_rus = '//label[text()="Русский"]'
    locator_toggle_4_5 = '//div[text()="Высокая оценка"]/..//div[@class="Switcher__toggle_YvG-f"]'
    locator_book = ('//a[@href="/book/tatyana-alekseeva-32/bolshaya-povarennaya-kniga-garri-pottera-ot-prazdnich'
                    '-69751531/"][@data-test-id="art__title--desktop"]')


    '''Getters'''
    # Получение элемента по локатору

    # Получение результата поиска
    def get_result_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_result_search)))

    # Получение второй книги
    def get_new_book(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_new_book)))

    # Получение чекбокса формата
    def get_checkbox_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_checkbox_format_text)))

    # Получение чекбокса языка
    def get_checkbox_lang_rus(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_checkbox_lang_rus)))

    # Получения тогла
    def get_toggle_4_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_toggle_4_5)))

    # Получение первой книги
    def get_book(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_book)))

    # Получение поля ввода
    def get_input_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_search)))

    # Получение кнопки "Найти"
    def get_button_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_button_search)))

    # Получение названия первой книги
    def get_title_first_book(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator_first_book)))

    # Получение текста названия второй книги
    def get_text_new_book(self):
        return self.get_new_book().text


    '''Actions'''
    # Действия с элементами

    # Клик на вторую книгу
    def click_to_new_book(self):
        self.get_new_book().click()
        print('Click to new book')

    # Клик на чекбокс формата
    def click_to_checkbox_text(self):
        self.get_checkbox_text().click()
        print('Click to checkbox text')

    # Клик на чекбокс языка
    def click_to_checkbox_rus(self):
        self.get_checkbox_lang_rus().click()
        print('Click to checkbox rus')

    # Клик на тогл
    def click_to_toggle_4_5(self):
        self.get_toggle_4_5().click()
        print('Click to toggle 4_5')

    # Клик на первую книгу
    def click_to_book(self):
        self.get_book().click()
        print('Click to book')

    # Клик на поле ввода
    def click_to_input_search(self):
        self.get_input_search().click()
        print('Click to book')

    # Клик на кнопку "Найти"
    def click_to_button_search(self):
        self.get_button_search().click()
        print('Click to book')

    # Ввод названия второй книги
    def input_search_name(self, book_title):
        self.get_input_search().send_keys(book_title)
        print('Input user name')


    '''Methods'''
    # Методы, используемые в тесте


    # Выбор второй книги
    def select_new_product(self):
        with allure.step('select_new_product'):
            Logger.add_start_step(method='select_new_product')
            self.get_current_url()
            self.click_to_new_book()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_new_product')
            return self

    # Выбор первой книги
    def search_product_book(self):
        with allure.step('search_product_book'):
            Logger.add_start_step(method='search_product_book')
            self.click_to_input_search()
            self.input_search_name(self.input_title)
            self.click_to_button_search()
            Logger.add_end_step(url=self.driver.current_url, method='search_product_book')
            return self

    # Выбор фильтров
    def select_filters(self):
        with allure.step('select_filters'):
            Logger.add_start_step(method='select_filters')
            self.click_to_checkbox_text()
            self.click_to_checkbox_rus()
            self.click_to_toggle_4_5()
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_filters')
            return self

    # Выбор первой книги
    def select_product(self):
        with allure.step('select_product'):
            Logger.add_start_step(method='select_product')
            self.get_current_url()
            self.click_to_book()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_product')
            return self



