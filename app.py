from flask import Flask, render_template, send_from_directory, request, redirect
from flask_mail import Mail, Message
import os
from database import *
from secret import *

app = Flask(__name__)

VIDEO_FOLDER = os.path.join(os.getcwd(), 'video')


app.config['MAIL_SERVER'] = 'smtp.ukr.net'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = email
app.config['MAIL_DEFAULT_SENDER'] = email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/video/<filename>')
def video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/TO')
def serv_TO():
    return render_template('serv_TO.html')

@app.route('/spare_parts')
def serv_spare_parts():
    return render_template('serv_spare_parts.html')

@app.route('/suspension')
def serv_suspension():
    return render_template('serv_suspension.html')

@app.route('/brakes')
def serv_brakes():
    return render_template('serv_brakes.html')

@app.route('/computer_diagnostics')
def serv_computer_diagnostics():
    return render_template('serv_computer_diagnostics.html')


@app.route('/checking_before_buying')
def serv_checking_before_buying():
    return render_template('serv_checking_before_buying.html')




@app.route('/comments')
def comments():
    comments = view_comments()
    return render_template('comments.html', comments=comments)

@app.route('/add_comment_form')
def add_comment_form():
    return render_template('add_comment.html')

@app.route('/<int:id>/')
def comment(id):
    comment = view_comment(id)
    return render_template('comment_inside.html', comment=comment)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    name = request.form['name']
    brand = request.form['brand_']
    comment = request.form['comment']
    good = request.form['good']
    bad = request.form['bad']
    evaluation = request.form['rating']
    add_comments(name, brand, comment, good, bad, evaluation)
    return redirect('/')






@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    brand = request.form['brand']
    year = request.form['year']
    problem = request.form['problem']
    phone = request.form['phone']
    telegram = request.form['telegram']
    call_back = request.form['call_back']
    send_email_user(name, brand, year, problem, phone, telegram, call_back)
    return redirect('/')

def send_email_user(name, brand, year, problem, phone, telegram, call_back):
    msg = Message(f'Новий запис: {name}. Машина: {brand}, {year}',
                  recipients=[email1])
    msg.body = f"""
    Ім'я: {name}
    Марка: {brand}
    Модель та рік: {year}
    Проблема: {problem}
    Телефон: {phone}
    Телеграм: {telegram}
    Зателефонувати?: {call_back}
    """
    mail.send(msg)




@app.route('/order_parts')
def order_parts():
    return render_template('order_parts.html')

@app.route('/submit_parts', methods=['POST'])
def submit_parts():
    name = request.form['name']
    brand = request.form['brand']
    year = request.form['year']
    vin = request.form['vin']
    parts = request.form['parts']
    phone = request.form['phone']
    telegram = request.form['telegram']
    call_back = request.form['call_back']
    send_email_parts(name, brand, year, vin, parts, phone, telegram, call_back)
    return redirect('/')

def send_email_parts(name, brand, year, vin, parts, phone, telegram, call_back):
    msg = Message(f'Запчастини: {name}. Машина: {brand}, {year}',
                  recipients=[email1])
    msg.body = f"""
    Ім'я: {name}
    Марка: {brand}
    Модель та рік: {year}
    VIN: {vin}
    Перелік запчастин: {parts}
    Телефон: {phone}
    Телеграм: {telegram}
    Зателефонувати?: {call_back}
    """
    mail.send(msg)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')