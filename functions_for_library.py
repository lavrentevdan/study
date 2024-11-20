from books import books_pack

valid_answers = ['1', '2', '3', '4']
cmnd = 0
action = 0
list_of_commands = "Выберите действие: \n1. Показать все книги\n2. Найти книгу\n3. Добавить книгу\n4. Удалить книгу\n5. Выход"
chosing_commands = 'Выберите действие: \n1. Удалить книги\n2. Отмена\n'
delimiter = "-" * 30
checked_base = []



def get_checked_base_of_books(raw_base):
   checked_base = []
   for book in raw_base:
      if book["status"]:
         checked_base.append(book)
   return checked_base
def add_book(book):
    global books_pack
    books_pack.append(book)
def new_book_params_fill():
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
   return new_book
def search_book(search_string):
   books_found = []
   search_string.lower()
   for book in books_pack:
      if search_string in book.get("author").lower() or \
         search_string in book.get("title").lower() or \
         search_string in str(book.get("year")).lower():
         books_found.append(book)
   return books_found
def print_books(books):
   for i, book in enumerate(books):
      print(i+1)
      print(f"Название: {book['title']}")
      print(f"Автор: {book['author']}")
      print(f"Год издания: {book['year']}")
      print(delimiter)
def print_single_book(single_book):
   for key, value in single_book():
      print(f"{key}: {value}")
def choose_books_for_delition():
   while True:
      user_answer = input(chosing_commands).strip()
      if user_answer == '1':
         return 1
      elif user_answer == '2':
         return 2
      else: input('нет такой команды, нажмите Enter, чтобы продолжить...')
def deletion(books_to_remove):
   global books_pack
   for book in books_to_remove:
      if book in books_pack:
         books_pack.remove(book)
   