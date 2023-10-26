from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__) 

boostrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
    return 'This is a new task!'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'It is time for you to go.'
    return s1 + s2

#hello_flask.py
@app.route('/nicva')
def t_test():
    return render_template('template.html')

