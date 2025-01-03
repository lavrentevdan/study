import pprint
import json
import sqlite3
db_path = r'database.db'
valid_answers = ['1', '2', '3', '4']
cmnd = 0
action = 0
visual_barrier = "-" * 30
continue_message = 'нажмите Enter, чтобы продолжить...'
list_of_commands = "Выберите действие: \n1. Показать все книги\n2. Найти книгу\n3. Добавить книгу\n4. Удалить книгу\n5. Выход"

def print_books(data):
   for i in data:
      print(f'id: {i[0]}')
      print(f'Год издания: {i[1]}')
      print(f'Название: {i[2]}')
      print(f'Автор: {i[3]}')
      if i[4] == 1:
         print('Статус: доступно')
      else:
         print('Статус: недоступно')
      print(visual_barrier)
   return None
def update_data():
   try:
      with sqlite3.connect(db_path) as db:
         cursor = db.cursor()
         query = """SELECT * FROM books"""
         data = cursor.execute(query)
         # data = cursor.fetchall()
         return data
   except FileNotFoundError:
      input('Нет доступа к базе')
def save_data(data):
   try:
      with open('books.json', 'w', encoding='utf-8') as db:
         json.dump(data, db, ensure_ascii=False, indent=4)
   except Exception:
      print('Ошибка')
def demonstration(books_to_demonstrate):
   print(visual_barrier)
   print_books(books_to_demonstrate)
def add_book(book):
    global books_pack
    books_pack.append(book)
def book_filling():

   print("Заполните характеристики новой книги")
   new_books_name = input("Название:").lower()
   new_books_author = input("Автор:").lower()
   while True:
        new_books_year = input("Год выпуска: ")
        if new_books_year.isdigit():
            new_books_year = int(new_books_year)
            break
        else:
            print("Ошибка: Введите числовое значение для года.")

   new_book = [new_books_year, new_books_name, new_books_author]
   return new_book
def book_insertation(new_book):
   try:
      with sqlite3.connect(db_path) as db:
         cursor = db.cursor()
         query = """
         INSERT INTO books(year, name, author, status) VALUES
         (?, ?, ?, 1)
         """
         data = cursor.execute(query, (new_book[0], new_book[1], new_book[2]))
         # data = cursor.fetchall()
         return data
   except FileNotFoundError:
      input('Нет доступа к базе')
def search_book():
   search_key = input('Поиск: ').lower()
   search_pattern = f'%{search_key}%'
   try:
      with sqlite3.connect(db_path) as db:
         cursor = db.cursor()
         query = """
         SELECT * FROM books 
         WHERE year LIKE ? 
         OR author LIKE ? 
         OR name LIKE ?
         """
         cursor.execute(query, (search_pattern, search_pattern, search_pattern))
         data = cursor.fetchall()
         if not data:
            return None
         return data
   except FileNotFoundError:
      input('Нет доступа к базе')
def book_deleting(id):
   try:
      with sqlite3.connect(db_path) as db:
         cursor = db.cursor()
         query = """
         DELETE FROM books
         WHERE id = ?
         """
         cursor.execute(query, (id,))
         # data = cursor.fetchall()
   except FileNotFoundError:
      input('Нет доступа к базе')
   








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
         data = update_data()
         demonstration(data)
         input(continue_message)
      case 2:
         data = search_book()
         if data == None:
            input('ничего не найдено')
         else: 
            demonstration(data)
            input(continue_message)
      case 3:
         new_book = book_filling()
         book_insertation(new_book)
         input(continue_message)
      case 4:
         print("Какую книгу удалить?")
         data = search_book()
         if data != None:
               demonstration(data)
               while True:
                  user_inp = input('введите id книги для удаления: ').strip()
                  try:   
                     delete_key = int(user_inp)
                     break
                  except ValueError:
                     print('введите число из списка')
               book_deleting(delete_key)
               input('книга удалена, нажмите enter, чтобы продолжить...')
         else:
            input('ничего не найдено')
      case _: pass







