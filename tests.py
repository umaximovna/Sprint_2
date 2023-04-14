from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # проверка проставления книге рейтинга меньше 1
    def test_set_book_rating_set_rating_less_than_one_rating_not_change(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1, 'Assigned a rating value less than 1, must be between 1 and 10'

    # проверка проставления книге рейтинга больше 10
    def test_set_book_rating_set_rating_more_than_ten_rating_not_change(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1, 'Assigned a rating value more than 10, must be between 1 and 10'

    # проверка получения рейтинга несуществующей книги
    def test_get_book_rating_get_not_found_book_rating_none(self):
        collector = BooksCollector()
        collector.add_new_book('Человек, который смеётся')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == None

    # проверка получения списка книг с определенным рейтингом
    def test_get_books_with_specific_rating_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Человек, который смеётся')
        collector.set_book_rating('Человек, который смеётся', 8)
        collector.add_new_book('Поющие в терновнике')
        collector.set_book_rating('Поющие в терновнике', 8)
        collector.add_new_book('Американская трагедия')
        collector.set_book_rating('Американская трагедия', 9)
        result = collector.get_books_with_specific_rating(8)
        assert len(result) == 2 and ['Человек, который смеётся', 'Поющие в терновнике'] == result

    # проверка получения словаря books_rating
    def test_get_books_rating_get_dict_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Человек, который смеётся')
        collector.set_book_rating('Человек, который смеётся', 8)
        collector.add_new_book('Поющие в терновнике')
        collector.set_book_rating('Поющие в терновнике', 7)
        # получить список ключей и значений из словаря, сравнить с заданными
        assert collector.get_books_rating() == {'Человек, который смеётся': 8, 'Поющие в терновнике': 7}

    # проверка добавления книги, существующей в словаре books_rating, в Избранное
    def test_add_book_in_favorites_add_exist_in_book_rating_list_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Человек, который смеётся')
        collector.add_book_in_favorites('Человек, который смеётся')
        assert collector.get_list_of_favorites_books() == ['Человек, который смеётся']

    # проверка добавления книги, отсутствующей в словаре books_rating, в Избранное
    def test_add_book_in_favorites_add_not_found_in_book_rating_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Человек, который смеётся')
        collector.add_book_in_favorites('Обыкновенная история')
        assert collector.get_list_of_favorites_books() == [], 'Book that is not in the [books_rating] dict must not added to favorites'

    # проверка удаления существующей в Избранном книги из Избранного
    def test_delete_book_from_favorites_delete_exist_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Сестра Керри')
        collector.add_book_in_favorites('Сестра Керри')
        collector.delete_book_from_favorites('Сестра Керри')
        assert collector.get_list_of_favorites_books() == []

    # проверка получения списка избранных книг
    def test_get_list_of_favorites_books_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Финансист')
        collector.add_book_in_favorites('Финансист')
        collector.add_new_book('Титан')
        collector.add_book_in_favorites('Титан')
        assert collector.get_list_of_favorites_books() == ['Финансист', 'Титан']
