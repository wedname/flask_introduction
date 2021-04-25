from flask import render_template, request, redirect, session, abort
import random
import string

from app.users.models import User, Users


class UserController:

    def get_one_user(self, id: int):
        return next(iter(filter(lambda x: x.id == id, self.users.items)))

    def __init__(self, app):
        self.app = app
        self.users = Users('database/users.json', User)

        @app.route('/register', methods=['GET'])
        def register_view():
            return render_template('register.html')

        @app.route('/logout', methods=['GET'])
        def logout_user():
            if 'email' in session:
                session.pop('email')
            return redirect('/')

        @app.route('/register/create', methods=['POST'])
        def register_new_user():
            if not self.register_validate(request.form):
                print('Валидация не пройдена')
                return redirect('/register')
            user_id = self.users.get_last_id() + 1
            is_created = self.users.push(
                User(
                    id=user_id,
                    **request.form
                ),
                lambda i: not len([x for x in i if request.form.get('email') == x.email]) > 0
            )
            if not is_created:
                print('Такой юзер уже есть')
                return redirect('/register')
            self.users.save()
            session['id'] = user_id
            session['email'] = request.form.get('email')
            session['role'] = request.form.get('role')
            return redirect('/')

        @app.route('/register/create', methods=['POST'])
        def register_new_user():
            if not self.register_validate(request.form):
                print('Валидация не пройдена')
                return redirect('/register')
            user_id = self.users.get_last_id() + 1
            is_created = self.users.push(
                User(
                    id=user_id,
                    **request.form
                ),
                lambda i: not len([x for x in i if request.form.get('email') == x.email]) > 0
            )
            if not is_created:
                print('Такой юзер уже есть')
                return redirect('/register')
            self.users.save()
            session['id'] = user_id
            session['email'] = request.form.get('email')
            session['role'] = request.form.get('role')
            return redirect('/')

        @app.route('/create/user', methods=['GET', 'POST'])
        def create_user():
            if session['role'] != '2':
                abort(403)
            if request.method == 'GET':
                return render_template('user_form.html')
            elif request.method == 'POST':
                try:
                    if 'avatar' in request.files:
                        image = request.files['avatar']
                        random_name = ''.join([random.choice(string.digits + string.ascii_letters) for x in range(10)])
                        img_path = f'static/images/{random_name}.jpg'
                        image.save(img_path)
                    else:
                        img_path = 'static/images/default_avatar.jpg'
                    user = {
                        'id': self.users.get_last_id(),
                        'username': request.form['username'],
                        'email': request.form['email'],
                        'phone': request.form['phone'],
                        'password': request.form['password'],
                        'avatar': img_path
                    }
                    self.users.push(User(**user))
                    return redirect('/')
                except Exception as e:
                    print(e)
                    abort(500)
            else:
                return 'METHOD NOT ALLOWED'

        @app.route('/users', methods=['GET'])
        def get_users():
            return render_template('users.html', users=self.users.items)

        @app.route('/user/<int:id>', methods=['GET'])
        def get_user(id):
            user = self.get_one_user(id)
            if user is None:
                abort(404)
            return render_template('user.html', user=user)

        @app.route('/delete/user/<int:id>', methods=['GET'])
        def delete_user(id):
            self.users.remove(id)
            return 'success'

    def register_validate(self, form):
        if not all([form.get('email'), form.get('password'), form.get('confirm_password')]):
            return False
        elif form.get('password') != form.get('confirm_password'):
            return False
        return True
