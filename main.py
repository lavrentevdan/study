# string = 'Alex'
# number = 123
# float_ = 12.4
# bool_ = True

# list_ = []
# list2_ = list()
# tuple_ = (1, )
# tuple2 = tuple()
# dict_ = {
#     'key': {}
# }
# dict2 = dict()

# aaa = ['123', 12, 12, '123']
# set_ = set(aaa)
# set_.add('lesson')
# print(set_)

# frset_ = frozenset(aaa)


# DICT
car = {
    'color': 'blue',
    'people': 5,
    'wheels': [
        {
            'radius': 16,
            'year': 2024
        },
        {
            'radius': 16,
            'year': 2022
        }
    ],
    'doors': {
        'left': 1,
    }
}

# print(car[True])


# Арифметика в python

# + - * / // % **

# string = 5 ** 2

# print(string)



# Условные конструкции
# == | != | < | > | <= | >= | and | or | ^


# print('Check car color')
# if car['people']:
#     print('My capor is red')
# elif car['people'] != 5:
#     print('Nice size')
# else:
#     print('Missed color')
    
# term = input("Input car type: ")

# match term:
#     case 'polo':
#          print('Love')
#     case 'tuareg':
#          print('shit')
#     case 'cayen':
#          print('porsh')
#     case _:
#         print('car')


# Цыклы

# cars = ['porsh', 'bmw', 'kia']

# for car in cars:
#     print(f'My best car is { car }')
#     if (car == 'bmw'):
#         break

# count = 0
# while count <= 5:
#     print(count)
#     count += 1

# Задача
# 1. Калькулятор cmd
# 2* Графический интерфейс

def foo():
    print(123)


print('0 - Выход\n1 - ...')
answer = None
while answer != 0:
    answer = int(input("Команда: "))