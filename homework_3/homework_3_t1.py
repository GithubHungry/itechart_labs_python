# Создать класс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.

# 1.Определить в классе следующие конструкторы: с параметрами и без параметров
# 2.Компоненты-функции для просмотра и установки полей данных: setТип(), getТип()
#   (помним про инкапсуляцию проверку корректности задания параметров).
# 3.Написать демонстрационную программу, в которой создаются и разрушаются объекты (от 3 до 5 шт.)
#   и указатели на объекты пользовательского класса и каждый вызов конструктора сопровождается выдачей
#   соответствующего сообщения.
# 4.Использовать метод __setattr__().
# 5.Создать список объектов. Вывести:
#       a.список книг заданного автора;
#       b.список книг, выпущенных после заданного года.
import datetime


class Book:
    """Class about book."""

    __count = 0

    # def __init__(self):
    #   """Пример Конструктора без параметров."""
    #
    #
    #         В Python создать несколько методов __init__() в классе можно, однако "рабочим" останется только последний.
    #         Он переопределит ранее определенные. Поэтому в Python в классах используется только один конструктор,
    #         а изменчивость количества передаваемых аргументов настраивается через назначение значений по-умолчанию.

    def __init__(self, id_book: int, title: str, authors: str, publishing_house: str, year: int, pages_number: int,
                 price: float, binding: str) -> None:
        """Конструктор с параметрами."""
        self.__id_book = id_book
        self.__title = title
        self.__authors = authors
        self.__publishing_house = publishing_house
        self.__year = year
        self.__pages_number = pages_number
        self.__price = price
        self.__binding = binding
        Book.__count += 1
        print("Создан экземпляр класса, показание счетчика экземпляров:", Book.__count)

    def __setattr__(self, key, value):
        """Redefinition __setattr__."""
        if key == '_Book__id_book' and isinstance(value, int):
            self.__dict__[key] = value
        # print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__title' and isinstance(value, str):
            self.__dict__[key] = value
        # print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__authors' and isinstance(value, str):
            self.__dict__[key] = value
        # print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__publishing_house' and isinstance(value, str):
            self.__dict__[key] = value
        # print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__year' and isinstance(value, int):
            self.__dict__[key] = value
        # print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__pages_number' and isinstance(value, int):
            self.__dict__[key] = value
        # print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__price':
            self.__dict__[key] = value
        # print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__binding' and isinstance(value, str):
            self.__dict__[key] = value
        # print("Вы установили для поля {0}, значение {1}".format(key, value))
        else:
            raise AttributeError

    def get_id_book(self) -> int:
        """Getter for id_book field."""
        return self.__id_book

    def get_title(self) -> str:
        """Getter for title field."""
        return self.__title

    def get_authors(self) -> str:
        """Getter for authors field."""
        return self.__authors

    def get_year(self) -> int:
        """Getter for year field."""
        return self.__year

    def set_author(self, value: str) -> None:
        """Setter for authors field."""
        if isinstance(value, str):
            print("Устанавливаю полю authors значение:", value)
            self.__authors = value
        else:
            raise ValueError("Некорректное значение для поля authors.")

    def set_pages_number(self, value: int) -> None:
        """Setter for pages_number field."""
        if isinstance(value, int) and value > 0:
            print("Устанавливаю полю authors значение:", value)
            self.__pages_number = value
        else:
            raise ValueError("Некорректное значение для поля pages_number.")

    def set_year(self, value: int) -> None:
        """Setter for year field."""
        if isinstance(value, int) and value <= datetime.datetime.now().year:
            print("Устанавливаю полю year значение:", value)
            self.__year = value
        else:
            raise ValueError

    @property
    def full_info(self):
        """Return full info about book as attr(only for reading)."""
        return '{}, {}, {}, {}, {}, {}, {}, {}.'.format(self.__id_book, self.__title, self.__authors,
                                                        self.__publishing_house, self.__year, self.__pages_number,
                                                        self.__price, self.__binding)

    def __str__(self):
        """String representation of object."""
        return self.__title

    def __repr__(self):
        """Representation"""
        return self.__title

    def __del__(self) -> None:
        """Object destruction."""
        Book.__count -= 1
        print("Удален экземпляр класса, показание счетчика экземпляров:", Book.__count)

    @staticmethod
    def return_counter() -> int:
        """Getter for counter field."""
        return Book.__count


def show_constructor_and_destructor_work():
    """Написать демонстрационную программу, в которой создаются и разрушаются объекты (от 3 до 5 шт.)
    и указатели на объекты пользовательского класса и каждый вызов конструктора сопровождается выдачей"""
    b1_demonstration = Book(6, 'Война и мир', 'Лев Толстой', 'АВЕРСЭВ', 1867, 1000, 621, 'Твердая')
    b2_demonstration = Book(7, 'Мастер и Маргарита', 'Михаил Булгаков', 'АВЕРСЭВ', 1937, 654, 500, 'Мягкая')
    b3_demonstration = Book(8, 'Евгений Онегин', 'Александр Пушкин', 'АВЕРСЭВ', 1831, 189, 870, 'Твердая')
    print(Book.return_counter())
    del b1_demonstration
    print(Book.return_counter())
    del b2_demonstration
    print(Book.return_counter())
    del b3_demonstration
    print(Book.return_counter())


def book_list_with_author(list_of_books: list, author: str) -> list:
    """Returns list of books, where author == author."""
    result_list = []
    for book in list_of_books:
        if book.get_authors() == author:
            result_list.append(book)
    if result_list:
        return result_list
    else:
        print('Нет книг этого автора!')


def book_list_after_year(list_of_books: list, year: int) -> list:
    """Returns list of books, where all books created after year."""
    result_list = []
    for book in list_of_books:
        if book.get_year() > year:
            result_list.append(book)
    if result_list:
        return result_list
    else:
        print('Нет книг этого автора!')


#   Демонстрация работы конструктора и деструктора
# show_constructor_and_destructor_work()

# Проверочные данные для функций
# b1 = Book(0, 'Война и мир', 'Лев Толстой', 'АВЕРСЭВ', 1867, 1000, 621, 'Твердая')
# b2 = Book(1, 'Мастер и Маргарита', 'Михаил Булгаков', 'АВЕРСЭВ', 1937, 654, 500, 'Мягкая')
# b3 = Book(2, 'Евгений Онегин', 'Александр Пушкин', 'АВЕРСЭВ', 1831, 189, 870, 'Твердая')
# b4 = Book(3, 'Преступление и наказание', 'Фёдор Достоевский', 'АВЕРСЭВ', 560, 980, 621.21, 'Твердая')
# b5 = Book(4, 'Маленький принц', 'Антуан де Сент-Экзюпери', 'АВЕРСЭВ', 1942, 60, 466, 'Мягкая')
# b6 = Book(5, '1984', 'Джордж Оруэлл', 'АВЕРСЭВ', 1948, 350, 250, 'Твердая')
# b7 = Book(5, 'О дивный новый мир', 'Олдос Хаксли', 'АВЕРСЭВ', 1931, 368, 234.30, 'Твердая')
# books_list = [b1, b2, b3, b4, b5, b6, b7]

#   Список книг по автору
# print(book_list_with_author(books_list, 'Александр Пушкин'))

#   Список книг выпущенных после заданного года
# print(book_list_after_year(books_list, 1900))
