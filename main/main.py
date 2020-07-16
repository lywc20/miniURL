from flask import Flask, render_template, request, Blueprint, g, redirect
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

# Redirects users to mapped url
@main.route('/<string:short_url>/',methods=['GET'])
def redirect_to_mapped_site(short_url):
    if request.method == 'GET':
        res = key_generator.findUrl(short_url)
        return redirect('https:' + res['url'])

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
