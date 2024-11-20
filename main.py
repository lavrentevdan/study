from modules.functions import my_func
from datetime import datetime as dt

import requests

def main_modules():
    r = requests.get('https://catfact.ninja/fact')
    print(r.json())


def division(a, b):
    return round(a / int(b), 2)


def main_except():
    try:
        print(division(10, 0))
    except (ZeroDivisionError, ValueError):
        print('Одна из 2х ошибок')
    except ZeroDivisionError as e:
        print('На ноль деллить нельзя')
    except ValueError as e:
        print('Дурак, только числа!')
    except:
        print('Неизвестная ошибка')
    else:
        print('Если нет ошибки')
    finally:
        print('Закончили проверку')

    print('Работаем дальше')



class OnlyOneException(Exception):
    pass

def do_thing(param):
    if param != 1:
        raise OnlyOneException

def main():
    try:
        do_thing(2)
    except OnlyOneException:
        print('Только единицы!')

if __name__ == '__main__':
   main()