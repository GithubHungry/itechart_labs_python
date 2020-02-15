########## 1 TASK ##########

# Реализуйте функцию постановки слова «рубль» в подходящее число и падеж в зависимости от введенного целого числа
# (ввели «0» – функция возвращает «рублей», ввели «1» – «рубль», ввели «2» – «рубля» и т. д.).

def ruble_substitution(rub: int) -> str:
    """Ruble substitution function."""
    if type(rub) != int:
        rub = int(rub)
    if rub % 10 == 0 or 5 <= rub % 10 <= 9 or 11 <= rub % 100 <= 14:
        return 'рублей'
    elif 2 <= rub % 10 <= 4:
        return 'рубля'
    elif rub % 10 == 1:
        return 'рубль'


########## 2 TASK ##########

# Реализуйте функцию постановки слова «копейка» в подходящее число и падеж в зависимости от введенного целого числа
# (ввели «0» – функция возвращает «копеек», ввели «1» – «копейка», ввели «2» – «копейки» и т. д.).

def coin_substitution(coin: int) -> str:
    """Coin substitution function."""
    if type(coin) != int:
        coin = int(coin)
    if coin % 10 == 0 or 5 <= coin % 10 <= 9 or 11 <= coin % 100 <= 14:
        return 'копеек'
    elif 2 <= coin % 10 <= 4:
        return 'копейки'
    elif coin % 10 == 1:
        return 'копейка'


########## 3 TASK ##########

# Реализуйте функцию вывода введенного числа прописью в мужском роде
# (ввели «0» – функция возвращает «ноль», ввели «1» – «одна», ввели «2» – «две» и т. д. до «999»).

def number_2_words_rubles(num: int) -> str:
    """Convert number into words(0-999)."""
    one_s = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
             'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
             'девятнадцать']
    ten_s = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    if type(num) != int:
        num = int(num)
    if num > 999:
        return 'Неправильные входные данные.'
    if not num:
        return 'ноль'
    if num // 100 != 0 and num % 100 != 0:
        result_string = '{0}'.format(hundreds[num // 100 - 1]) + ' '
    elif num // 100 != 0:
        return hundreds[num // 100 - 1]
    else:
        result_string = ''
    if num % 100 <= 19:
        result_string += one_s[num % 100 - 1]
    else:
        result_string = result_string + ten_s[num % 100 // 10 - 2] + ' ' + one_s[num % 10 - 1]
    return result_string


########## 4 TASK ##########

# Реализуйте функцию вывода введенного числа прописью в женском роде (ввели «0» – функция возвращает «ноль»,
# ввели «1» – «одна», ввели «2» – «две» и т. д. до «999»).

def number_2_words_coins(num: int) -> str:
    """Convert number into words(0-999)."""
    one_s = ['одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
             'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
             'девятнадцать']
    ten_s = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    if type(num) != int:
        num = int(num)
    if num > 999:
        return 'Неправильные входные данные.'
    if not num:
        return 'ноль'
    if num // 100 != 0 and num % 100 != 0:
        result_string = '{0}'.format(hundreds[num // 100 - 1]) + ' '
    elif num // 100 != 0:
        return hundreds[num // 100 - 1]
    else:
        result_string = ''
    if num % 100 <= 19:
        result_string += one_s[num % 100 - 1]
    else:
        result_string = result_string + ten_s[num % 100 // 10 - 2] + ' ' + one_s[num % 10 - 1]
    return result_string


########## 5 TASK ##########

# Используя предыдущие функции, реализуйте еще одну функцию, которая будет выводить введенную сумму денег
# с плавающей точкой прописью (ввели «0,70» – функция возвращает «ноль рублей семьдесят копеек»).

def money_function(money: str) -> str:
    """Convert number into words+ruble(coin)."""
    money_list = [int(num) for num in money.replace('.', ',').split(',') if num.isdigit()]
    if len(money_list) == 2:
        if money_list[1] <= 99:
            result_string = '{0} {1}, {2} {3}.'.format(number_2_words_rubles(money_list[0]),
                                                        ruble_substitution(money_list[0]),
                                                        number_2_words_coins(money_list[1]),
                                                        coin_substitution(money_list[1]))
    elif len(money_list) == 1:
        result_string = '{0} {1}.'.format(number_2_words_rubles(money_list[0]),
                                          ruble_substitution(money_list[0]))
    else:
        result_string = 'Введите корректное число.'
    return result_string


print(money_function(input('Введите количество денег:')))
