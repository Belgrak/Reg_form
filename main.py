from flask import Flask, render_template
from data import db_session
from re_form import RegisterForm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if form.validate_on_submit() and form.password.data == form.rep_password.data:
        user = User()
        user.name = form.name.data
        user.surname = form.surname.data
        user.email = form.login.data
        user.hashed_password = hash(form.password.data)
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        return 'Вы успешно зарегистрированы'
    return render_template('index.html', title='Регистрация', form=form)


if __name__ == '__main__':
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    app.run()
