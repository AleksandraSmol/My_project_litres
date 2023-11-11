import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


# Класс ReadPage представляет страницу чтения фрагмента первой книги веб-приложения litres.ru и наследуется от класса Base
class ReadPage(Base):

    # Класс ReadPage содержит метод init, который инициализирует объект класса ReadPage и принимает в качестве
    # параметра объект driver.
    # Функция super вызывает метод init родительского класса Base, чтобы инициализировать
    # driver и использовать его в других методах класса ReadPage
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    '''Variables'''
    # Переменные с названиями товаров

    book_title = 'Большая поваренная книга Гарри Поттера. От праздничных пиров Хогвартса до камерных посиделок в «Норе»'


    '''Locators'''
    # Переменные с локаторами на странице чтения фрагмента

    locator_read_button_smaller = '//button[@class="scale-button smaller-scale-button"]'
    locator_read_button_larger = '//button[@class="scale-button larger-scale-button"]'
    locator_read_button_return = '//a[@class="art-page-link"]'


    '''Getters'''
    # Получение элемента по локатору

    # Получение кнопки "Мельче"
    def get_read_button_smaller(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_read_button_smaller)))

    # Получение кнопки "Крупнее"
    def get_read_button_larger(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_read_button_larger)))

    # Получение кнопки возврата в карточку первого товара
    def get_read_button_return(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_read_button_return)))


    '''Actions'''
    # Действия с элементами

    # Клик на кнопку "Мельче"
    def click_to_read_button_smaller(self):
        self.get_read_button_smaller().click()
        print('Click to read button smaller')

    # Клик на кнопку "Крупнее"
    def click_to_read_button_larger(self):
        self.get_read_button_larger().click()
        print('Click to read button larger')

    # Клик на кнопку возврата в карточку первой книги
    def click_to_read_button_return(self):
        self.get_read_button_return().click()
        print('Click to read button return')


    '''Methods'''
    # Методы, используемые в тесте

    # Получение url страницы
    def receive_data_read(self):
        with allure.step('receive_data_read'):
            Logger.add_start_step(method='receive_data_read')
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method='receive_data_read')

    # Работа с фрагментом книги
    def reading_a_fragment_of_a_book(self):
        with allure.step('reading_a_fragment_of_a_book'):
            Logger.add_start_step(method='reading_a_fragment_of_a_book')
            self.get_screenshot()
            self.click_to_read_button_smaller()
            self.click_to_read_button_larger()
            self.click_to_read_button_return()
            Logger.add_end_step(url=self.driver.current_url, method='reading_a_fragment_of_a_book')
            return self







