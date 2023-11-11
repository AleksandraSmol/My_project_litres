import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


# Класс CartPage представляет страницу Корзина веб-приложения litres.ru и наследуется от класса Base
class CartPage(Base):

    # Класс CartPage содержит метод init, который инициализирует объект класса CartPage  и принимает в качестве
    # параметра объект driver.
    # Функция super вызывает метод init родительского класса Base, чтобы инициализировать
    # driver и использовать его в других методах класса CartPage
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    '''Variables'''
    # Переменные с названиями товаров

    book_title = 'Большая поваренная книга Гарри Поттера. От праздничных пиров Хогвартса до камерных посиделок в «Норе»'
    search_name = 'Шоколад Джоан Харрис'


    '''Locators'''
    # Переменные с локаторами на странице Корзина

    locator_book_cart_title = '//a[@href="/book/tatyana-alekseeva-32/bolshaya-povarennaya-kniga-garri-pottera-ot-prazdnich-69751531/"][contains(text(), "повар")]'
    locator_book_cart_price = '(//strong[@class="Cart-module__bookCard__price__final_3ZZQv"])[2]'
    locator_new_book_cart_title = '//a[@href="/book/dzhoann-harris/shokolad-121580/"][contains(text(), "Шоколад")]'
    locator_new_book_cart_price = '(//strong[@class="Cart-module__bookCard__price__final_3ZZQv"])[1]'
    locator_info_total = ('//div[@class="CheckoutBox-module__costs__info_3IkF9 '
                          'CheckoutBox-module__costs__info_total_15QTT"]')
    locator_total_price = ('//div[@class="CheckoutBox-module__costs__price_1HeDU '
                           'CheckoutBox-module__costs__info_total_15QTT"]')
    locator_button_purchase = '//div[@class="Button-module__buttonContent_28JI7"]'
    locator_search = '//input[@data-test-id="header__search-input--desktop"]'
    locator_button_search = '//button[@data-test-id="header__search-button--desktop"]'
    locator_in_fav = '//div[text()="В отложенном"]'
    locator_delete = '//div[@class="FunctionalButton-module__funcButtonContent__child_3mjgy" and text()="Удалить"]'
    locator_delete_2 = '//div[@class="Button-module__textContainer_1I67-" and text()="Удалить"]'
    locator_empty_cart = '//h2[@class="EmptyState-module__empty__title_22qdT"]'


    '''Getters'''
    # Получение элемента по локатору

    # Получение кнопки удаления книги из отложенного
    def get_in_fav(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_in_fav)))

    # Получение кнопки удаления книги из корзины
    def get_del(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_delete)))

    # Получение кнопки подтверждения удаления книги из корзины
    def get_del_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_delete_2)))

    # Получение поля поиска
    def get_input_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_search)))

    # Получение кнопки "Найти"
    def get_button_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_button_search)))

    # Получение названия первой книги в корзине
    def get_book_cart_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_book_cart_title)))

    # Получение цены первой книги в корзине
    def get_book_cart_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_book_cart_price)))

    # Получение слова "Итого"
    def get_info_total(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_info_total)))

    # Получение итоговой цены книг
    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_total_price)))

    # Получение кнопки "Перейти к покупке"
    def get_button_purchase(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_button_purchase)))

    # Получение названия второй книги в корзине
    def get_new_book_cart_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_new_book_cart_title)))

    # Получение цены второй книги в корзине
    def get_new_book_cart_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_new_book_cart_price)))

    # Текст названия второй книги в корзине
    def get_text_new_book_cart_title(self, word):
        return self.get_new_book_cart_title().text

    # Текст цены второй книги в корзине
    def get_text_new_book_cart_price(self, word):
        return self.get_new_book_cart_price().text

    # Текст названия первой книги в корзине
    def get_text_book_cart_title(self,word):
        return self.get_book_cart_title().text

    # Текст цены первой книги в корзине
    def get_text_book_cart_price(self, word):
        return self.get_book_cart_price().text

    # Элемент "Корзина пуста"
    def get_empty_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_empty_cart)))


    '''Actions'''
    # Действия с элементами

    # Клик на поле поиска
    def click_to_input_search(self):
        self.get_input_search().click()
        print('Click to input search')

    # Клик на кнопку "Найти"
    def click_to_button_search(self):
        self.get_button_search().click()
        print('Click to button search')

    # Вставка названия первой книги
    def input_search_name(self, book_title):
        self.get_input_search().send_keys(book_title)
        print('Input search name')

    # Клик на кнопку "Перейти к покупке"
    def click_to_button_purchase(self):
        self.get_button_purchase().click()
        print('Click to button purchase')

    # Клик на удалить из Отложенного
    def click_to_in_fav(self):
        self.get_in_fav().click()
        print('Click to delete "in favorites"')

    # Клик на Удалить
    def click_to_del(self):
        self.get_del().click()
        print('Click to Delete')

    # Клик на подтвердить удаление
    def click_to_del_2(self):
        self.get_del_2().click()
        print('Click to Delete too')


    '''Methods'''
    # Методы, используемые в тесте

    # Получение url страницы
    def receive_data_cart(self):
        with allure.step('receive_data_cart'):
            Logger.add_start_step(method='receive_data_cart')
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method='receive_data_cart')
            return self

    # Поиск второй книги
    def search_product_book(self):
        with allure.step('search_product_book'):
            Logger.add_start_step(method='search_product_book')
            self.click_to_input_search()
            self.input_search_name(self.search_name)
            self.click_to_button_search()
            Logger.add_end_step(url=self.driver.current_url, method='search_product_book')
            return self

    # Работа с двумя книгами в корзине
    def working_with_books_in_the_cart(self):
        with allure.step('working_with_books_in_the_cart'):
            Logger.add_start_step(method='working_with_books_in_the_cart')
            self.get_current_url()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='working_with_books_in_the_cart')
            return self

    # Оплата
    def purchase(self):
        with allure.step('purchase'):
            Logger.add_start_step(method='purchase')
            self.click_to_button_purchase()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='purchase')
            return self

    # Очистка корзины
    def clean_all(self):
        with allure.step('clean_all'):
            Logger.add_start_step(method='clean_all')
            self.driver.refresh()
            self.click_to_in_fav()
            self.click_to_del()
            self.click_to_del_2()
            time.sleep(5)
            self.click_to_del()
            self.click_to_del_2()
            Logger.add_end_step(url=self.driver.current_url, method='clean_all')
            return self








