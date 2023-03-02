from flask import Blueprint, flash,  url_for, render_template, request
import os
from datetime import datetime
from flask_login import current_user,logout_user, login_required, login_user
from basa import bcrypt, db
from basa.models import User, Order
from basa.order.routes import orders
from basa.user.forms import RegistrationForm, LoginForm
import shutil
from werkzeug.utils import redirect


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.basa'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        full_path = os.path.join(os.getcwd(), 'basa/static', 'profile_pics', user.username)
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        shutil.copy(f'{os.getcwd()}/basa/static/profile_pics/default.jpg', full_path)
        flash('Ваш аккаунт был создан.Вы можете войти', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form, title='Регистрация', legend='Регистрация')


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.basa'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Вы вошли как пользователь {current_user.username}', 'info')
            return redirect(next_page) if next_page else  redirect(url_for('users.account'))
        else:
            flash('Войти не удалось. Проверьте пароль или электронную почту', 'danger')
    return render_template('login.html',form=form, title='Логин', legend='Войти')


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account.html')



@users.route('/user/<string:username>')
@login_required
def user_orders(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    orders = Order.query.filter_by(author=user) \
        .order_by(Order.date_posted.desc()) \
        .paginate(page=page, per_page=3)

    return render_template('user_orders.html', title='Общий блог', orders=orders, user=user)


@users.route('/logout')
def logout():
    current_user.last_seen = datetime.now()
    db.session.commit()
    logout_user()
    return redirect(url_for('main.home'))
