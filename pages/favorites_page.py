import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


# Класс FavoritesPage представляет страницу Отложенное веб-приложения litres.ru и наследуется от класса Base
class FavoritesPage(Base):

    # Класс FavoritesPage содержит метод init, который инициализирует объект класса FavoritesPage  и принимает в качестве
    # параметра объект driver.
    # Функция super вызывает метод init родительского класса Base, чтобы инициализировать
    # driver и использовать его в других методах класса FavoritesPage
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    '''Variables'''
    # Переменные с названиями товаров

    book_title = 'Большая поваренная книга Гарри Поттера. От праздничных пиров Хогвартса до камерных посиделок в «Норе»'


    '''Locators'''
    # Переменные с локаторами на странице Отложенное

    locator_book_fav_title = ('//div[@class="liked-art__name"]/a['
                              '@href="/book/tatyana-alekseeva-32/bolshaya-povarennaya-kniga-garri-pottera-ot'
                              '-prazdnich-69751531/"]')
    locator_book_fav_price = '//span[@class="simple-price"]'
    locator_fav_dropdown_dots = '//a[@class="dropdown-opener dropdown-dots"]'
    locator_fav_dropdown_read = '//a[@class="art-button art-buttons__read"]'
    locator_read_button_smaller = '//button[@class="scale-button smaller-scale-button"]'
    locator_read_button_larger = '//button[@class="scale-button larger-scale-button"]'
    locator_read_button_return = '//a[@class="art-page-link"]'
    locator_button_cart = '//div[@data-test-id="tab-basket"]'
    

    '''Getters'''
    # Получение элемента по локатору

    # Получение названия первой книги в Отложенном
    def get_book_fav_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_book_fav_title)))

    # Получение цены первой книги в Отложенном
    def get_book_fav_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_book_fav_price)))

    # Получение кнопки выпадающего меню
    def get_dropdown_dots(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_fav_dropdown_dots)))

    # Получение кнопки "Читать фрагмент"
    def get_dropdown_read(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_fav_dropdown_read)))

    # Получение текста названия первой книги в Отложенном
    def get_text_book_fav_title(self, word):
        return self.get_book_fav_title().text

    # Получение текста цены первой книги в Отложенном
    def get_text_book_fav_price(self, word):
        return self.get_book_fav_price().text


    '''Actions'''
    # Действия с элементами

    # Клик на выпадающее меню рядом с книгой
    def click_to_dropdown_dots(self):
        self.get_dropdown_dots().click()
        print('Click to dropdown dots')

    # Клик в выпадающем меню на кнопку "Читать фрагмент"
    def click_to_dropdown_read(self):
        self.get_dropdown_read().click()
        print('Click to dropdown read')


    '''Methods'''
    # Методы, используемые в тесте

    # Получение url страницы
    def receive_data_fav(self):
        with allure.step('receive_data_fav'):
            Logger.add_start_step(method='receive_data_fav')
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method='receive_data_fav')
            return self

    # Работа с первой книгой в Отложенном
    def working_with_book_in_the_favorites(self):
        with allure.step('working_with_book_in_the_favorites'):
            Logger.add_start_step(method='working_with_book_in_the_favorites')
            self.click_to_dropdown_dots()
            self.get_screenshot()
            self.click_to_dropdown_read()
            Logger.add_end_step(url=self.driver.current_url, method='working_with_book_in_the_favorites')
            return self




