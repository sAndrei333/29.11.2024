import sqlite3

from flask import Flask, render_template, flash, request

app = Flask(__name__)
con = sqlite3.connect("data.db")
@app.route('/register/', methods=['POST','GET'])
def register():
    return render_template('register.html')
@app.route('/save_register/')
def save_register():

    if request.method == "POST":

        id = request.form['id']
        last_name = request.form['last_name']
        name = request.form['name']
        patronymic = request.form['patronymic']
        gender = request.form['gender']
        email= request.form['email']
        user_name = request.form['login']
        password = request.form['password']
        con.cursor.execute('INSERT INTO data.db (id, last_name, name, patronymic, gender, email, login, password) VALUES({id, last_name, name, patronymic, user_name, password})')
        con.commit()

        return  f' Вы ввели id {id} фамилию {last_name} имя {name} отчество {patronymic} пол {gender} email {email} логин {user_name} и пароль {password}'
    return 'Вы уже зарегестрировались'
app.run(debug=True)