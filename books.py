import sqlite3

db_path = r'database.db'
new_book = [1999, 'ария', 'Перельман']
with sqlite3.connect(db_path) as db:
    cursor = db.cursor()
    query = """
    INSERT INTO books(year, name, author, status) VALUES
    (?, ?, ?, 1)
    """
    cursor.execute(query, (new_book[0], new_book[1], new_book[2]))
    print('success')




# CREATE TABLE IF NOT EXISTS books(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     year INTEGER,
#     name TEXT NOT NULL,
#     author TEXT NOT NULL,
#     status INTEGER
#     )


# INSERT INTO books (year, name, author, status) VALUES
#     (1867, "Война и Мир", "Толстой", 1),
#     (1866, "Преступление и наказание", "Достоевский", 1),
#     (1821, "Идиот", "Достоевский", 1),
#     (1862, "Отцы и дети", "Тургенев", 0)




# books_pack = [
#     {
#         "title": "Война и Мир",
#         "author": "Толстой",
#         "year": 1867,
#         "status": True
#     },
#     {
#         "title": "Преступление и наказание",
#         "author": "Достоевский",
#         "year": 1866,
#         "status": True
#     },
#     {
#         "title": "Идиот",
#         "author": "Достоевский",
#         "year": 1821,
#         "status": True
#     },
#     {
#         "title": "Преступление",
#         "author": "Достоевский",
#         "year": 1866,
#         "status": True
#     },
#     {
#         "title": "Наказание",
#         "author": "Достоевский",
#         "year": 1866,
#         "status": True
#     }
# ]

