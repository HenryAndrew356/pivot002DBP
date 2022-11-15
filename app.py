from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
# , methods=["GET","POST"]
@app.route('/register/')
def register():
    return render_template('formToCv.html')

@app.route('/matrix/')
def matrix():
    return render_template('matrix.html')
# cvOfForm
@app.route('/cvOfForm/')
def cvOfForm():
    return render_template('cvOfForm.html')

if __name__=='__main__':
    app.run()