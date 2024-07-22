from flask import Flask, render_template


app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
  return f'User {username}'

@app.route('/')
def hello_world():
  return 'Hello, World!<br><a href="/about">About</a>'

@app.route('/about')
def about():
  return '<h1>DOM</h1><a href="/">Main</a>'

if __name__ == '__main__':
  app.run(debug=True)