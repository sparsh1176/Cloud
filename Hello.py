from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   return 'Hello %s as User' % name

@app.route('/')
def hello():
    return redirect("http://www.google.com", code=302)

if __name__ == '__main__':
   app.run()