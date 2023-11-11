import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


# Класс ProductPage представляет страницу карточки первой книги веб-приложения litres.ru и наследуется от класса Base
class ProductPage(Base):

    # Класс ProductPage содержит метод init, который инициализирует объект класса ProductPage и принимает в качестве
    # параметра объект driver.
    # Функция super вызывает метод init родительского класса Base, чтобы инициализировать
    # driver и использовать его в других методах класса ProductPage
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    '''Variables'''
    # Переменные с названиями товаров

    book_title = 'Большая поваренная книга Гарри Поттера. От праздничных пиров Хогвартса до камерных посиделок в «Норе»'


    '''Locators'''
    # Переменные с локаторами в карточке второй книги

    locator_book_title = '//h1[@itemprop="name"]'
    locator_book_price = '//span[@class="simple-price"]'
    locator_button_put_to_favorites = '//button[@class="art-button art-buttons__favorite"]'
    locator_button_put_to_cart = '//button[@class="art-button art-buttons__basket"]'
    locator_reviews = '//li[@data-goal="Tab_otzivi"]'
    locator_reviews_filter = '//div[@class="Sorting-module__commentsSorting"]'
    locator_radiobutton_pop = '//button[text()="Сначала популярные"]'
    locator_radiobutton_new = '//button[text()="Сначала новые"]'
    locator_promo_popup = '//div[@id="promo-books-popup"]/a[@class="close"]'
    locator_button_favorites = '//a[@href="/pages/new_liked/"]'
    locator_button_cart = '//div[@data-test-id="tab-basket"]'


    '''Getters'''
    # Получение элемента по локатору

    # Получение названия первой книги
    def get_book_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_book_title)))

    # Получение цены первой книги
    def get_book_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_book_price)))

    # Получение кнопки "Положить в корзину"
    def get_button_put_to_favorites(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_button_put_to_favorites)))

    # Получение кнопки "Отзывы"
    def get_reviews(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_reviews)))

    # Получение элемента сортировки отзывов
    def get_reviews_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_reviews_filter)))

    # Получение радиобаттона "Новые отзывы"
    def get_radiobutton_new(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_radiobutton_new)))

    # Получение кнопки "Положить в корзину"
    def get_button_put_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_button_put_to_cart)))

    # Получение промо-попапа
    def get_promo_popup(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_promo_popup)))

    # Получение кнопки "Отложенное"
    def get_button_favorites(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_button_favorites)))

    # Получение текста названия первой книги
    def get_text_book_title(self, word):
        return self.get_book_title().text

    # Получение кнопки "Корзина"
    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_button_cart)))


    '''Actions'''
    # Действия с элементами

    # Клик на кнопку "Положить в Отложенное"
    def click_to_button_put_to_favorites(self):
        self.get_button_put_to_favorites().click()
        print('Click to button put to favorites')

    # Клик на кнопку "Отзывы"
    def click_to_reviews(self):
        self.get_reviews().click()
        print('Click to reviews')

    # Клик на кнопку сортировки отзывов
    def click_to_reviews_filter(self):
        self.get_reviews_filter().click()
        print('Click to reviews filter')

    # Клик на радиобаттон "Новые отзывы"
    def click_to_radiobutton_new(self):
        self.get_radiobutton_new().click()
        print('Click to radiobutton new')

    # Клик на кнопку "Положить в корзину"
    def click_to_button_put_to_cart(self):
        self.get_button_put_to_cart().click()
        print('Click to button put to cart')

    # Клик на закрытие промо-попапа
    def click_to_close_promo_popup(self):
        self.get_promo_popup().click()
        print('Click to close promo popup')

    # Клик на кнопку "Отложенное"
    def click_to_button_favorites(self):
        self.get_button_favorites().click()
        print('Click to button favorites')

    # Клик на кнопку "Положить в корзину"
    def click_to_button_cart(self):
        self.get_button_cart().click()
        print('Click to read button return')


    '''Methods'''
    # Методы, используемые в тесте

    # Получение url страницы
    def receive_data(self):
        with allure.step('receive_data'):
            Logger.add_start_step(method='receive_data')
            self.get_current_url()
            time.sleep(3)
            Logger.add_end_step(url=self.driver.current_url, method='receive_data')
            return self

    # Работа с первой книгой
    def working_with_the_cooking_book(self):
        with allure.step('working_with_the_cooking_book'):
            Logger.add_start_step(method='working_with_the_cooking_book')
            self.click_to_button_put_to_favorites()
            self.click_to_close_promo_popup()
            self.driver.execute_script('window.scrollTo(0,500)')
            self.click_to_reviews()
            time.sleep(1)
            self.click_to_reviews_filter()
            time.sleep(1)
            self.click_to_radiobutton_new()
            time.sleep(1)
            self.get_screenshot()
            time.sleep(2)
            self.click_to_reviews_filter()
            self.driver.execute_script('window.scrollTo(0,-500)')
            self.click_to_button_put_to_cart()
            self.click_to_button_favorites()
            Logger.add_end_step(url=self.driver.current_url, method='working_with_the_cooking_book')
            return self









