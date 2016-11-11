from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


@app.route('/list-test', methods=['GET', 'POST'])
def list_test():
    return render_template('list-test.html', messagelist=['Adam', 'Bob', 'Cube', 'Dick', 'Ella'])


if __name__ == '__main__':
    app.run()
