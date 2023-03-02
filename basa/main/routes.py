from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user

from basa.models import Order

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html', title='Главная')


@main.route('/blog', methods=['POST', 'GET'])
@login_required
def blog():
    order = Order.query.get(current_user.id)
    if order:
        page = request.args.get('page', 1, type=int)
        orders = Order.query.order_by(Order.date_posted.desc()) \
            .paginate(page=page, per_page=2)
        image_file = url_for('static', filename=f'profile_pics/{current_user.username}/{order.image_post}')

        return render_template('blog.html', title='Блог', orders=orders, image_file=image_file)

    else:
        return render_template('blog.html',title='Блог', nithing='Заказов пока нет')

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
