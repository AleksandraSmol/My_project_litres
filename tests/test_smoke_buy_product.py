import time
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.search_page import SearchPage
from base.base_class import Base
from pages.product_page import ProductPage
from pages.favorites_page import FavoritesPage
from pages.cart_page import CartPage
from pages.product_new_page import ProductNewPage
from pages.read_page import ReadPage

# Смоук-тест сайта litres.ru
@allure.description('Test buy books')
def test_buy_books(set_up):
    driver = webdriver.Chrome()


    '''Авторизация'''

    mp = MainPage(driver)
    mp.authorization()

    # Проверка успешности авторизации по слову "Профиль"
    profile_word = mp.get_profile_word()
    base = Base(driver)
    base.assert_word(profile_word, 'Профиль')


    '''Выбор категории и подкатегории книги'''

    mp.get_start_it()

    # Проверка успешности выбора подкатегории
    expected_url_mp = 'https://www.litres.ru/genre/kulinariya-5275/'
    base.assert_url(expected_url_mp)


    '''Поиск первой книги'''

    sp = SearchPage(driver)
    sp.search_product_book()

    # Проверка поиска первой книги
    search_word = sp.get_result_search()
    base.assert_word(search_word, 'Результаты поиска «до камерных посиделок»')

    time.sleep(5)

    # Фильтрация результата поиска
    sp.select_filters()

    # Проверка найденной книги по словосочетанию
    preview_word = sp.get_title_first_book()
    book_title_in_preview = preview_word.text[:-3]    # Убираем в сокращенном названии 3 последних знака (...), которых нет в полном названии
    base.assert_word(preview_word, 'Большая поваренная книга Гарри Поттера. От...')


    '''Выбор первой книги'''

    sp.select_product()

    # Проверка выбранной книги по его url
    expected_url_sp = 'https://www.litres.ru/book/tatyana-alekseeva-32/bolshaya-povarennaya-kniga-garri-pottera-ot-prazdnich-69751531/'
    base.assert_url(expected_url_sp)


    '''Проверка названия первой книги на разных страницах'''

    pp = ProductPage(driver)
    pp.receive_data()

    # Переменные названия первой книги и ее цены для дальнейшей проверки их на странице Favorites
    book_title_for_favorites = pp.get_book_title().text
    book_price_for_favorites = pp.get_book_price().text
    print(book_price_for_favorites)

    # Сравнение названия первой книги в превью (страница SearchPage) с полным названием в карточке первой книги на странице
    # ProductPage.
    # Проверка, что сокращенное название из превью входит в полное название, для этого необходимо удалить 3 последних
    # знака сокращенного названия (...).
    # Передача названия первой книги из SearchPage в метод для получения названия первой книги на странице ProductPage
    book_text_title_in_card = pp.get_text_book_title(book_title_in_preview)
    print(f'text word 1 is {book_title_in_preview}')
    print(f'text word 2 is {book_text_title_in_card}')
    assert book_title_in_preview in book_text_title_in_card
    print(f'Book title in preview {book_title_in_preview} included in the title {book_text_title_in_card}')


    '''Работа с карточкой первой книги'''
    #

    pp.working_with_the_cooking_book()


    '''Отложенное'''

    fp = FavoritesPage(driver)
    fp.receive_data_fav()

    # Проверка переход в избранное по url
    expected_url_fp = 'https://www.litres.ru/pages/new_liked/'
    base.assert_url(expected_url_fp)

    # Сравнение названия первой книги и его цены в карточке первой книги (страница ProductPage) с названием и ценой первой книги в
    # Отложенном на странице FavoritesPage.
    # Передача названия первой книги из ProductPage в метод для получения названия первой книги на странице FavoritesPage
    book_text_title_fav = fp.get_text_book_fav_title(book_title_for_favorites)
    book_text_price_fav = fp.get_text_book_fav_price(book_price_for_favorites)
    # Проверка названия первой книги
    assert book_text_title_fav == book_title_for_favorites
    print(f'The title of the book in favorites {book_text_title_fav} matches the title of the book in the product card {book_title_for_favorites}')
    # Проверка цены первой книги
    assert book_text_price_fav == book_price_for_favorites
    print(f'The price of the book in favorites {book_text_price_fav} matches the price of the book in the product card {book_price_for_favorites}')

    # Открытие выпадающего меню и переход к чтению фрагмента первой книги
    fp.working_with_book_in_the_favorites()


    '''Чтение фрагмента первой книги'''

    rp = ReadPage(driver)
    rp.receive_data_read()

    # Проверка страницы чтения фрагмента первой книги по слову "Крупнее"
    read_word = rp.get_read_button_larger()
    base.assert_word(read_word, 'Крупнее')
    print('The read word is "Крупнее"')

    # Работа с фрагментом первой книги, возврат в карточку первой книги
    rp.reading_a_fragment_of_a_book()

    # Проверка по url
    base.assert_url(expected_url_sp)

    # Переход в корзину из карточки первой книги
    pp.click_to_button_cart()


    '''Корзина'''

    cp = CartPage(driver)
    cp.receive_data_cart()

    # Проверка нахождения в корзине по url
    expected_url_cp = 'https://www.litres.ru/pages/new_basket/'
    base.assert_url(expected_url_cp)


    '''Поиск второй книги'''

    cp.search_product_book()


    '''Выбор второй книги'''

    new_search_word = sp.get_text_new_book()

    sp.select_new_product()


    '''Работа со второй книгой'''

    pnp = ProductNewPage(driver)
    pnp.working_with_the_new_book()

    # Сравнение названия второй книги и ее цены в карточке второй книги (страница ProductNewPage) с названием и ценой второй книги в
    # превью (страница SearchPage).
    # Передача названия второй книги из SearchPage в метод для получения названия второй книги на странице ProductNewPage
    book_title_for_cart = pnp.get_new_book_title().text
    print(book_title_for_cart)
    book_price_for_cart = pnp.get_new_book_price().text
    print(book_price_for_cart)
    book_title_pnp = pnp.get_text_new_book_title(new_search_word)
    assert book_title_pnp == new_search_word
    print(
        f'The title of the book in product new page {book_title_pnp} matches the title of the book in the new search book {new_search_word}')


    '''Корзина с двумя книгами'''

    cp.working_with_books_in_the_cart()


    '''Проверка названия и цены обеих книг'''

    # Переменные названия второй книги и ее цены для проверки их в Корзине
    word_title_cart_new = cp.get_text_new_book_cart_title(book_title_for_cart)
    word_price_cart_new = cp.get_text_new_book_cart_price(book_price_for_cart)

    # Сравнение названия второй книги в корзине со второй книгой на странице ProductNewPage
    assert word_title_cart_new == book_title_for_cart
    print('Name "Шоколад" has been checked in the cart')
    # Сравнение цены второй книги в корзине со второй книгой на странице ProductNewPage
    assert word_price_cart_new == book_price_for_cart
    print('Price "Шоколад" has been checked in the cart')

    # Переменные названия первой книги и ее цены для проверки их в Корзине
    word_title_cart = cp.get_text_book_cart_title(book_title_for_favorites)
    word_price_cart = cp.get_text_book_cart_price(book_price_for_favorites)

    # Сравнение названия первой книги в корзине с первой книгой на странице ProductPage
    assert word_title_cart == book_title_for_favorites
    print('Name "Большая поваренная книга Гарри..." has been checked in the cart')
    # Сравнение названия первой книги в корзине с первой книгой на странице ProductPage
    assert word_price_cart == book_price_for_favorites
    print('Price "Большая поваренная книга Гарри..." has been checked in the cart')


    '''Проверка суммы к оплате'''

    # Очистка цен от знака валюты с помощью метода из класса Base
    price_1 = word_price_cart
    clean_price_1 = base.clean_price(price_1)
    price_2 = word_price_cart_new
    clean_price_2 = base.clean_price(price_2)

    # Сложение цен двух книг
    total_book = clean_price_1 + clean_price_2

    # Проверка сложенных цен с суммой к оплате
    price_all = cp.get_total_price().text
    clean_price_all = base.clean_price(price_all)
    assert total_book == clean_price_all
    print('Total book = price all')


    '''Переход к оплате и очистка корзины'''

    cp.purchase().clean_all()

    # Проверка очистки корзины по слову 'Корзина пуста'
    empty_word = cp.get_empty_cart()
    base.assert_word(empty_word, 'Корзина пуста')
    print('Cart is empty')

