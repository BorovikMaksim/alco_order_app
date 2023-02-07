from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from basa.models import User
from flask import flash


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя',validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Емайл', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердить пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user =User.query.filter_by(username=username.data)
        if user:
            flash('Это имя уже занято.Выберете другое','danger')
            raise ValidationError('That username is taken. Please choose a different one')

class LoginForm(FlaskForm):
    email = StringField('Емайл', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')





