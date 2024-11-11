# USER_ID = 2

# name = 'Alex'

# def createUserName(value):
#    if USER_ID == 1:
#       return
#    global name
#    name = value

# createUserName("Danil")
# print(name)

#def sum(a):
#   return a * 2

# import pprint

# users = [{
   #    'name': 'Danil',
   #    'age': 25,
   #    'country': 'Serbia' 
   # },{
   #    'name': 'Alex',
   #    'age': 25,
   #    'country': 'Tailand' 
   # },{
   #    'name': 'Nikita',
   #    'age': 25,
   #    'country': 'Serbia' 
   # },
# ]

#result = list(map(lambda x: x * 2, arr))

# filtered = list(filter(lambda user: user['country'] == 'Serbia', users))



# pprint.pp(filtered)

# 5! = 5 * 4 * 3 * 2 * 1

# def factorial(n):
#    if n == 0:
#       return 1
#    else:
#       return n * factorial(n - 1)

# print(factorial(5))

# myData = {
#    'name': 1,
#    'right': {
#       'name': 2,
#       'right': {
#          'name': 3,
#          'right': None
#       }
#    },
#    'left': {
#       'name': 4,

#    }
# }
# import json
# print(json.dumps(myData))
from books import books_pack
def exhibition():
   print("-" * 30)
   for book, books_number in zip(books_pack, range(1, len(books_pack)+1)):
      if book["status"]:
         
         print(books_number)
         print(f"Название: {book['title']}")
         print(f"Автор: {book['author']}")
         print(f"Год издания: {book['year']}")
         print("-" * 30)
   return ''

def deleting():
   name_of_the_book = input("Введите название книги: ")
   counter = 1
   global books_pack
   user_answer = ''
   for book in books_pack:
      if book.get("title") == name_of_the_book:
         print(F"Вы хотите удалить эту книгу?\n{'-' * 30}")
         print(f"Название: {book['title']}")
         key_name = book['title']
         print(f"Автор: {book['author']}")
         print(f"Год издания: {book['year']}")
         print("-" * 30)
         counter += 2
         break
   if counter == 1:
      print('Такой книги нет в библиотеке')
   else:
      user_answer = input('1 - Да\n2 - Нет\n')
   if user_answer == 1:
      books_pack = [book for book in books_pack if book.get("title") != key_name]
      input("Книга удалена!")
   return ''

deleting()
exhibition()