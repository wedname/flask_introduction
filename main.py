from flask import Flask, render_template, redirect, session

from app.users.controller import UserController
from app.articles.controller import ArticleController

app = Flask(__name__)

app.secret_key = 'asdasdasdasd'


@app.route('/')
def main_page():
    if 'email' not in session:
        return redirect('/register')
    return render_template('index.html', title='ItStep Blog', articles=article.articles.items)


if __name__ == '__main__':
    user = UserController(app)
    article = ArticleController(app)
    app.run(host='localhost', port=5000)


"""
Задание #1:
Добавить возможность редактировать пользователя.
Задание #2:
Добавить возможность удалять статьи
Задание #3:
Добавить в статью поле 'rating' - int.
На странице статьи, нужно добавить форму с инпутом, чтобы пользователь мог оценить статью.
Когда пользователь вводит оценку и отправляет форму, нужно к полю rating добавить оценку пользователя и поделить на 2
Задание #4:
Запретить пользователю с ролью 'Гость' оценивать статьи
"""
