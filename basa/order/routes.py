from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import current_user, login_required

from basa import db
from basa.order.forms import OrderForm
from basa.models import Order
from basa.order.utils import save_picture_post

orders = Blueprint('orders',__name__)

@orders.route('/order/new', methods=['GET','POST'])
@login_required
def new_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = Order(title=form.title.data, content=form.content.data, image_post=form.picture.data, author=current_user)
        picture_file = save_picture_post(form.picture.data)
        order.image_post = picture_file
        db.session.add(order)
        db.session.commit()
        flash('Заявка была добавлена!', 'success')
        return  redirect(url_for('main.blog'))
    image_file = url_for('static',
                         filename=f'profile_pics/' + current_user.username + '/post_images/' + current_user.image_file)
    return render_template('create_order.html', title='Новый Заказ',
                           form=form, legend='Новый Заказ', image_file=image_file)





@orders.route('/order/<int:order_id>')
@login_required
def order(order_id):
    order = Order.query.get_or_404(order_id)
    image_file = url_for('static',
                         filename=f'profile_pics/' + order.author.username + '/post_images/' + order.image_post)
    return render_template('order.html', title=order.title, order=order, image_file=image_file)