# работа с файлами

# f = open('file.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()


# with open('file.txt', 'r', encoding='utf-8') as file:
#    .readlines()
#    .read()
#    for line in file:
#       print(line)
import json
import pprint

data = {
   'author': {
      'name': 'Alex',
      'surname': 'Pushkin',
      'hobbies': ['ski', 'pianino']
   }
}

new_data = None

# with open('file2.json', 'w', encoding='utf-8') as f:
#    f.write(json.dumps(data))

# with open('file2.json', 'r', encoding='utf-8') as f:
#    new_data = json.loads(f.read())

# pprint.pprint(new_data)

import time
 
# class Timer:
#     def __enter__(self):
#         self.start = time.time()
 
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end = time.time()
#         print(f'Время выполнения: {self.end - self.start:.2f} секунд')


# with Timer():
#     # код, время выполнения которого нужно измерить
#     time.sleep(3)


# with (open('file2.json', 'r', encoding='utf-8') as data,
#       open('file.txt', 'a', encoding='utf-8') as text):
   
#    data = json.loads(data.read())
#    print(data)

#    text.write('\nХобби автора: ')
#    for hobby in data['author']['hobbies']:
#       text.write(hobby + ' ')


data = None

my_files = ['file.txt', 'file_top.txt', 'image3.txt']

for file in my_files:
   try:
      with open(file, 'r', encoding='UTF-8') as f:
         print(f.read())
   except FileNotFoundError:
      print('файл не найден')