from flask import Flask, render_template, request, Blueprint, g
from .extensions import mongo
from .api import key_generator

main = Blueprint('main',__name__)

@main.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        short_url = key_generator.generateKey()
        url = request.form['url']
        key_generator.bindUrl(short_url,url)
        g.url = url
        g.short_url = short_url
        return render_template('index.html')
    else:
        return render_template('index.html')

@main.route('/success/<string:short_url>')
def success(url):
    return "The url is " + url

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        password = request.form['password']
        email = request.form['email']
        newAccount = account(user,password,email)
    else:
        return render_template('register.html')




if __name__ == '__main__':
    main.run(debug=True)
