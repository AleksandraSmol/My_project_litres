import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


# Класс MainPage представляет главную страницу веб-приложения litres.ru и наследуется от класса Base
class MainPage(Base):

    url = 'https://www.litres.ru/'
    password = 's7H.bsdQ*YW!3Ks'
    user_name = 'irina1petrova@inbox.ru'

    # Класс MainPage содержит метод init, который инициализирует объект класса MainPage  и принимает в качестве
    # параметра объект driver.
    # Функция super вызывает метод init родительского класса Base, чтобы инициализировать
    # driver и использовать его в других методах класса MainPage
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    '''Locators'''
    # Переменные с локаторами на главной странице

    locator_enter = '//a[@href="/pages/login/"]'
    # locator_profile = '//a[@data-testid="header__profile-button"]'
    locator_login_by_mail = '//div[text()="Электронная почта"]'
    locator_catalog = '//button[@data-test-id="header-catalog-button"]'
    locator_category_cooking = '//a[@href="/genre/kulinariya-5275/"]'
    locator_input_email = '//input[@name="email"]'
    locator_next = '//div[text()="Продолжить"]'
    locator_input_pass = '//input[@type="password"]'
    locator_button_to_come_in = '//div[text()="Войти"]'
    locator_close_auth = '//a[@class="AuthorizationPopup-module__closeIcon_1hrrE"]'
    locator_profile_word = '//div[text()="Профиль"]'


    '''Getters'''
    # Получение элемента по локатору

    # Получение кнопки "Вход"
    def get_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_enter)))

    # Получение кнопки "Войти по электронной почте"
    def get_login_by_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_login_by_mail)))

    # Получение поля ввода емэйла
    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_input_email)))

    # Получение поля ввода пароля
    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_input_pass)))

    # Получение кнопки "Продолжить"
    def get_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_next)))

    # Получение кнопки "Войти"
    def get_to_come_in(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_button_to_come_in)))

    # Получение кнопки закрытия попапа авторизации
    def get_close_auth(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_close_auth)))

    # Получение элемента "Профиль"
    def get_profile_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_profile_word)))

    # Получение кнопки "Каталог"
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_catalog)))

    # Получение категории "Кулинария"
    def get_category_cooking(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_category_cooking)))


    '''Actions'''
    # Действия с элементами

    # Клик на кнопку "Вход"
    def click_to_enter(self):
        self.get_enter().click()
        print('Click to enter')

    # Клик на кнопку "Войти по электронной почте"
    def click_to_login_by_mail(self):
        self.get_login_by_mail().click()
        print('Click to login by mail')

    # Ввод емэйла
    def input_email(self, user_name):
        self.get_input_email().send_keys(user_name)
        print('Input user name')

    # Ввод пароля
    def input_password(self, password):
        self.get_input_password().send_keys(password)
        print('Input password')

    # Клик на кнопку "Продолжить"
    def click_to_next(self):
        self.get_next().click()
        print('Click to next')

    # Клик на кнопку "Войти"
    def click_to_come_in(self):
        self.get_to_come_in().click()
        print('Click to come in')

    # Клик на кнопку завершения авторизации
    def click_to_close_auth(self):
        self.get_close_auth().click()
        print('Click to close auth')

    # Клик на кнопку "Каталог"
    def click_to_catalog_button(self):
        self.get_catalog().click()
        print('Click to catalog')

    # Клик на подкатегорию "Кулинария"
    def click_to_category_cooking(self):
        self.get_category_cooking().click()
        print('Click to category')


    '''Methods'''
    # Методы, используемые в тесте

    # Авторизация
    def authorization(self):
        with allure.step('authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_to_enter()
            time.sleep(2)
            self.click_to_login_by_mail()
            time.sleep(2)
            self.input_email(self.user_name)
            self.click_to_next()
            self.input_password(self.password)
            self.click_to_come_in()
            time.sleep(3)
            self.get_screenshot()
            self.click_to_close_auth()
            Logger.add_end_step(url=self.driver.current_url, method='authorization')
            return self

    # Выбор подкатегории книг
    def get_start_it(self):
        with allure.step('get_start_it'):
            Logger.add_start_step(method='get_start_it')
            self.get_current_url()
            self.click_to_catalog_button()
            self.click_to_category_cooking()
            self.get_screenshot()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='get_start_it')
            return self


