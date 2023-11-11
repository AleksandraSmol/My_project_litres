import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


# Класс ProductNewPage представляет страницу карточки второй книги веб-приложения litres.ru и наследуется от класса Base
class ProductNewPage(Base):

    # Класс ProductNewPage содержит метод init, который инициализирует объект класса ProductNewPage и принимает в качестве
    # параметра объект driver.
    # Функция super вызывает метод init родительского класса Base, чтобы инициализировать
    # driver и использовать его в других методах класса ProductNewPage
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    '''Variables'''
    # Переменные с названиями товаров

    book_title = 'Шоколад'


    '''Locators'''
    # Переменные с локаторами в карточке второй книги

    locator_new_book_title = '//a[@class="Cart-module__bookCard__link_2vZQZ" and text()="Шоколад"]'
    locator_new_book_price = '(//strong[@class="Cart-module__bookCard__price__final_3ZZQv"])[1]'
    locator_button_cart = '//div[@data-test-id="tab-basket"]'
    locator_new_put_to_cart = '//button[@class="art-button art-buttons__basket" and @data-name="Шоколад"]'


    '''Getters'''
    # Получение элемента по локатору

    # Получение кнопки "Положить в корзину"
    def get_new_put_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_new_put_to_cart)))

    # Получение названия второй книги
    def get_new_book_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_new_book_title)))

    # Получение цены второй книги
    def get_new_book_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_new_book_price)))

    # Получение кнопки "Корзина"
    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_button_cart)))

    # Получение текста названия второй книги
    def get_text_new_book_title(self, word):
        return self.get_new_book_title().text


    '''Actions'''
    # Действия с элементами

    # Клик на кнопку "Положить в корзину"
    def click_to_new_put_to_cart(self):
        self.get_new_put_to_cart().click()
        print('Click to button put to cart')

    # Клик на кнопку "Корзина"
    def click_to_button_cart(self):
        self.get_button_cart().click()
        print('Click to button favorites')


    '''Methods'''
    # Методы, используемые в тесте

    # Рабоота со второй книгой
    def working_with_the_new_book(self):
        with allure.step('working_with_the_new_book'):
            Logger.add_start_step(method='working_with_the_new_book')
            self.get_current_url()
            self.click_to_new_put_to_cart()
            self.click_to_button_cart()
            Logger.add_end_step(url=self.driver.current_url, method='working_with_the_new_book')
            return self






