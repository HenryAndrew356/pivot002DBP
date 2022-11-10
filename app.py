from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/register/')
def register():
    return render_template('register.html')

# @app.route('/home')
# def home_page():
#     return render_template('home.html')

# @app.route('/app')
# def