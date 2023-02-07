from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html', title='Главная')


@main.route('/basa')
def basa():
    return render_template('index.html', title='База')


@main.route('/vodka')
def vodka():
    return render_template('vodka.html')


@main.route('/whiskey')
def whiskey():
    return render_template('whiskey.html')


@main.route('/rom')
def rom():
    return render_template('rom.html')

@main.route('/wine')
def wine():
    return render_template('wine.html')

@main.route('/sparkling_wine')
def sparkling_wine():
    return render_template('sparkling_wine.html')


@main.route('/gin')
def gin():
    return render_template('gin.html')


@main.route('/brandy_and_cognac')
def brandy_and_cognac():
    return render_template('brandy_and_cognac.html')


@main.route('/liqueurs')
def liqueurs():
    return render_template('liqueurs.html')


@main.route('/beer')
def beer():
    return render_template('beer.html')


@main.route('/other_drinks')
def other_drinks():
    return render_template('other_drinks.html')






