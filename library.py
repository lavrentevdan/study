from books import books_pack
from functions_for_library import get_checked_base_of_books
from functions_for_library import add_book
from functions_for_library import new_book_params_fill
from functions_for_library import search_book
from functions_for_library import print_books
from functions_for_library import choose_books_for_delition
from functions_for_library import deletion

valid_answers = ['1', '2', '3', '4']
cmnd = 0
action = 0
list_of_commands = "Выберите действие: \n1. Показать все книги\n2. Найти книгу\n3. Добавить книгу\n4. Удалить книгу\n5. Выход"
chosing_commands = 'Выберите действие: \n1. Удалить книги\n2. Отмена\n'
delimiter = "-" * 30
checked_base = []
wrong_command_answer = (' \nНесуществующая команда, нажмите Enter, чтобы продолжить...')
no_intersections_answer = ('Нет совпадений')
go_further_answer = ('нажмите Enter, чтобы продолжить...')



while action != 5:
   print(list_of_commands)
   cmnd = input().strip()
   if cmnd in valid_answers:
      action = int(cmnd) 
   elif cmnd == '5':
      action = 5
   else:
      input(wrong_command_answer)
      action = 0

   match action:
      case 1:
         print(delimiter)
         print_books(get_checked_base_of_books(books_pack))
         input(go_further_answer)
      case 2:
         search_string = input("Поиск: ")
         relevant_books = search_book(search_string)
         if relevant_books == []:
            print(no_intersections_answer)
         else:
            print_books(relevant_books)
         input(go_further_answer)
      case 3:
         new_book = new_book_params_fill()
         add_book(new_book)
         input(go_further_answer)
      case 4:
         search_string = input("Какую книгу удаляем: ")
         found_books = search_book(search_string)
         if len(found_books) >= 1:
            print_books(found_books)
            user_choice = choose_books_for_delition()
            if user_choice == 1:
               deletion(found_books)
               print("книги удалены")
            elif user_choice == 2:
               pass
         else:
            print(no_intersections_answer)

         input(go_further_answer)
      case _: pass






