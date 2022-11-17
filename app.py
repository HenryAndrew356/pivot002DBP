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
    textField001="TxtFieldTest"
    return render_template('cvOfForm.html',field001=textField001)

if __name__=='__main__':
    app.run()