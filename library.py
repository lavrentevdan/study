from books import books_pack
import pprint
valid_answers = ['1', '2', '3', '4']
cmnd = 0
action = 0
list_of_commands = "Выберите действие: \n1. Показать все книги\n2. Найти книгу по автору\n3. Найти книгу по названию\n4. Добавить книгу\n5. Выход"

def exhibition():
   print("-" * 30)
   for book, books_number in zip(books_pack, range(1, len(books_pack)+1)):
      if book["status"]:
         
         print(books_number)
         print_book(book)
   return ''
def add_book(book):
    global books_pack
    books_pack.append(book)
def book_append():
   print("Заполните характеристики новой книги")
   new_books_name = input("Название:")
   new_books_author = input("Автор:")
   while True:
        new_books_year = input("Год выпуска: ")
        if new_books_year.isdigit():
            new_books_year = int(new_books_year)
            break
        else:
            print("Ошибка: Введите числовое значение для года.")
   new_book = {
      "title": new_books_name,
      "author": new_books_author,
      "year": new_books_year,
      "status": True
      }
   add_book(new_book)
   return ''
def search_book_by_author():
   key = input("Поиск: ").lower()
   books_found = []
   for book in books_pack:
      if key in book.get("author").lower() or \
         key in book.get("title").lower() or \
         key in str(book.get("year")).lower():
         books_found.append(book)
   return books_found
def search_book_by_title():
   key_title = input("Введите название книги: ")
   counter = 1
   for book, books_number in zip(books_pack, range(1, len(books_pack)+1)):
      if book.get("title") == key_title:
         print(counter)
         print(f"Название: {book['title']}")
         print(f"Автор: {book['author']}")
         print(f"Год издания: {book['year']}")
         print("-" * 30)
         counter += 1
   if counter == 1:
      print("\nКниг с указанным названием нет в библиотеке\n")
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

def print_books(books):
   for i, book in enumerate(books):
      print(i+1)
      print(f"Название: {book['title']}")
      print(f"Автор: {book['author']}")
      print(f"Год издания: {book['year']}")
      print("-" * 30)

while action != 5:
   print(list_of_commands)
   cmnd = input().strip()
   if cmnd in valid_answers:
      action = int(cmnd) 
   elif cmnd == '5':
      action = 5
   else:
      input(' \nНесуществующая команда, нажмите Enter, чтобы продолжить...')
      action = 0

   match action:
      case 1:
         print(exhibition())
         print('нажмите Enter, чтобы продолжить...')
         input()
      case 2:
         relevant_books = search_book_by_author()
         print_books(relevant_books)
         print('нажмите Enter, чтобы продолжить...')
         input()
      case 3:
         search_book_by_title()
         print('нажмите Enter, чтобы продолжить...')
         input()
      case 4:
         book_append()
         print('нажмите Enter, чтобы продолжить...')
         input()
      case _: pass








# def exhibition():
#    for book, books_number in zip(books_pack, range(1, len(books_pack)+1)):
#       if book["status"]:
#          print(books_number)
#          print(f"Название: {book['title']}")
#          print(f"Автор: {book['author']}")
#          print(f"Год издания: {book['year']}")
#          print("-" * 30)
#    return ''
# def add_book(book):
#     global books_pack
#     books_pack.append(book)
# def book_append():
#    print("Заполните характеристики новой книги")
#    new_books_name = input("Название:")
#    new_books_author = input("Автор:")
#    while True:
#         new_books_year = input("Год выпуска: ")
#         if new_books_year.isdigit():
#             new_books_year = int(new_books_year)
#             break
#         else:
#             print("Ошибка: Введите числовое значение для года.")
#    new_book = {
#       "title": new_books_name,
#       "author": new_books_author,
#       "year": new_books_year,
#       "status": True
#       }
#    add_book(new_book)
#    return ''
# def search_book_by_author():
#    key_author = input("Введите автора: ")
#    counter = 1
#    for book, books_number in zip(books_pack, range(1, len(books_pack)+1)):
#       if book.get("author") == key_author:
#          print(counter)
#          print(f"Название: {book['title']}")
#          print(f"Автор: {book['author']}")
#          print(f"Год издания: {book['year']}")
#          print("-" * 30)
#          counter += 1
#    if counter == 1:
#       print("Указаного автора нет в библиотеке\n")
#    input("\nДля продолжения нажмите Enter...")
#    return ''
# def search_book_by_title():
#    key_title = input("Введите название книги: ")
#    counter = 1
#    for book, books_number in zip(books_pack, range(1, len(books_pack)+1)):
#       if book.get("title") == key_title:
#          print(counter)
#          print(f"Название: {book['title']}")
#          print(f"Автор: {book['author']}")
#          print(f"Год издания: {book['year']}")
#          print("-" * 30)
#          counter += 1
#    if counter == 1:
#       print("\nКниг с указанным названием нет в библиотеке\n")
#    input("Для продолжения нажмите Enter...")
#    return ''
# def deleting():
#    name_of_the_book = input("Введите название книги: ")
#    counter = 1
#    global books_pack
#    user_answer = ''
#    for book in books_pack:
#       if book.get("title") == name_of_the_book:
#          print(F"Вы хотите удалить эту книгу?\n{'-' * 30}")
#          print(f"Название: {book['title']}")
#          key_name = book['title']
#          print(f"Автор: {book['author']}")
#          print(f"Год издания: {book['year']}")
#          print("-" * 30)
#          counter += 2
#          break
#    if counter == 1:
#       print('Такой книги нет в библиотеке')
#    else:
#       user_answer = input('1 - Да\n2 - Нет\n')
#    if user_answer == 1:
#       books_pack = [book for book in books_pack if book.get("title") != key_name]
#       input("Книга удалена!")
#    return ''


# print(deleting())

# print(search_book_by_title())

# print(exhibition())


# def status_change():

# 1.	Функция для добавления книги: done
# 2.	Функция для удаления книги:
# 3.	Функция для поиска книг по автору: done
# 4.	Функция для поиска книги по названию: done
# 5.	Функция для изменения статуса книги:
# 6.	Функция для отображения всех книг: done
# 7.	Функция для запуска программы:

# print(book_append())