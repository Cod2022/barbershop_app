from flask import Flask, request, render_template, url_for, redirect
from models import Client, db
from message_to_bot import send_message, get_from_env

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barbershop_database.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Database created')


@app.get('/')
def index_get():
    return render_template('index.html')

@app.get('/submission')
def submission_get():
    return render_template('submission.html')


@app.post('/')
def index_submit():
    name = request.form.get('name')
    tel = request.form.get('tel') 
    message = f"Новая запись: {name}, {tel}"
    send_message(get_from_env('CHAT_ID'), message)
    client = Client(name=name, phone_number=tel)
    db.session.add(client)
    db.session.commit()
    return redirect(url_for('submission_get'))


if __name__ == '__main__':
    app.run(debug=False)