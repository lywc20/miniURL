from flask import Flask, render_template, request, Blueprint

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

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
