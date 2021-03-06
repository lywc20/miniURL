from flask import Flask, render_template, request, Blueprint, g, redirect
from .extensions import mongo
from .api import key_generator
from .models import URL_Form
main = Blueprint('main',__name__)
import sys

keyGeneratorObject = key_generator.KeyGenerator(mongo)

@main.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        url = URL_Form(request.form)
        if not url.validate():
            g.errors = url.errors
            return render_template('index.html')
        else:
            short_url = keyGeneratorObject.generateKey()
            keyGeneratorObject.bindUrl(short_url,url.url.data)
            g.url = url.url.data
            g.short_url = short_url
            return render_template('index.html')
    else:
        return render_template('index.html')

# Redirects users to mapped url
@main.route('/<string:short_url>/',methods=['GET'])
def redirect_to_mapped_site(short_url):
    if request.method == 'GET':
        res = keyGeneratorObject.findUrl(short_url)
        if res:
            return redirect(res['url'])
        else:
            return render_template('404.html'),404


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
