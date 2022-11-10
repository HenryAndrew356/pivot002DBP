from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    print("Ingreso al Home")
    return render_template('home.html')

@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/matrix/')
def matrix():
    return render_template('matrix.html')

# 