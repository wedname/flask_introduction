"""
import sqlite3


connection = sqlite3.connect('flask.db')
cursor = connection.cursor()

cursor.execute("/""                CREATE TABLE IF NOT EXISTS users (
                    id integer not null primary key,
                    name text,
                    email text not null unique,
                    password text not null
                )
                ""/")

# cursor.execute(""/"
#                 INSERT INTO users (name, email, password)
#                 values ('Petro', 'admin1@admin.com', 'admin1')
#                 ""/")
# connection.commit()
cursor.execute('SELECT * FROM users')
users = cursor.fetchone()
print(users)
"""
import sqlite3
"""
Внимание!! Выбор типов данных и модификаторов для них (null, unique и т.д.) остается за вами
Задание 1: Создать таблицу articles с полями title, text, author, id
Задание 2: Написать функцию для добавления статей и добавить в табличку пару статей
Задание 3: Написать функцию для получения статьи по ид
Задание 4: Написать функцию для получения всех статей с возможностью сортировать и фильтровать данные по всем колонкам
Задание 5: Написать функцию для обновления статьи по ид

Задание 6: Создать таблицу users с полями id, username, email, password
Задание 7: Написать функцию для добавления пользователей и добавить в табличку пару пользователей
Задание 8: Написать функцию для получения пользователя по ид
Задание 9: Написать функцию для получения всех пользователей с возможностью сортировать и фильтровать данные по всем 
колонкам
Задание 10: Написать функцию для обновления пользователей по ид
"""

connection = sqlite3.connect('flask.db')

cursor = connection.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY NOT NULL,
  	                author TEXT NOT NULL,
  	                text TEXT NOT NULL,
  	                title TEXT NOT NULL
                )
                """)

cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY NOT NULL,
  	                email TEXT NOT NULL unique,
  	                password TEXT NOT NULL,
  	                username TEXT NOT NULL
                )
                """)


class DB:

    def __init__(self):
        pass

    def add(self, **kwargs):
        pass

    def search_id(self, search):
        pass

    def sorting(self, **kwargs):
        pass

    def edit(self, **kwargs):
        pass


class Articles(DB):

    def __init__(self):
        super(DB, self).__init__()

    def add(self, author: str, text: str, title: str):
        try:
            cursor.execute(f"""
                            INSERT INTO articles (author, text, title)
                            values ('{author}', '{text}', '{title}')
                            """)
        except ValueError as e:
            print(e)
            return False
        connection.commit()
        return True

    def search_id(self, search):
        try:
            cursor.execute(f"""
                            SELECT * FROM articles WHERE id = {search}
                            """)
        except ValueError as e:
            print(e)
            return False
        articles = cursor.fetchone()
        print(articles)
        return True

    def sorting(self, request: str):
        # requests = request.split()
        cursor.execute(f"""
                            SELECT * FROM articles ORDER BY {request}
                        """)
        articles = cursor.fetchall()
        print(articles)

    def edit(self, edit_user_id, column, value):
        cursor.execute(f"""
                                    UPDATE articles SET {column} = '{value}' WHERE ID = {edit_user_id}
                                """)


class Users(DB):

    def __init__(self):
        super(DB, self).__init__()

    def add(self, email: str, username: str, password: str):
        try:
            cursor.execute(f"""
                            INSERT INTO users (username, email, password)
                            values ('{username}', '{email}', '{password}')
                            """)
        except ValueError as e:
            print(e)
            return False
        connection.commit()
        return True

    def search_id(self, search):
        try:
            cursor.execute(f"""
                            SELECT * FROM users WHERE id = {search}
                            """)
        except ValueError as e:
            print(e)
            return False
        users = cursor.fetchone()
        print(users)
        return True

    def sorting(self, request: str):
        # requests = request.split()
        cursor.execute(f"""
                            SELECT * FROM users ORDER BY {request}
                        """)
        users = cursor.fetchall()
        print(users)

    def edit(self, edit_user_id, column, value):
        cursor.execute(f"""
                                    UPDATE users SET {column} = '{value}' WHERE ID = {edit_user_id}
                                """)


control_db_articles = Articles()
# control_db_articles.add('wedname', 'some text 1', 'title 1')
# control_db_articles.add('wedname', 'some text 2', 'title 2')
# control_db_articles.add('wedname', 'some text 3', 'title 3')
control_db_articles.sorting("id")
control_db_articles.edit(3, 'author', 'admin')
control_db_articles.sorting("id")

control_db_users = Users()
control_db_users.sorting("id")
control_db_users.edit(3, 'email', 'admin3@admin.com')
control_db_users.sorting("id")




