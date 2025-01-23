from flask import render_template, redirect, url_for, request
from . import db
from .models import Message
from .forms import MessageForm
from flask import current_app as app

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        new_message = Message(text=form.text.data)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('index'))
    
    messages = Message.query.all()
    return render_template('index.html', form=form, messages=messages)

@app.route('/delete/<int:id>')
def delete_message(id):
    message = Message.query.get(id)
    if message:
        db.session.delete(message)
        db.session.commit()
    return redirect(url_for('index'))
