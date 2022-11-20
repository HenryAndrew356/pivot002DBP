from flask import Flask, render_template,request,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
# , methods=["GET","POST"]
@app.route('/register/', methods=["GET","POST"])
def register():
    return render_template('formToCv.html')

@app.route('/matrix/')
def matrix():
    return render_template('matrix.html')
# cvOfForm
@app.route('/cvOfForm/', methods=["GET","POST"])
def cvOfForm():
    data=request.get_json()
    textField001="TxtFieldTest"
    print(data)
    return render_template('cvOfForm.html',field001=textField001)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
            # return  '''
        #           <h1>The language value is: {}</h1>
        #           <h1>The framework value is: {}</h1>
        #         '''.format(language, framework)
        return render_template('page02.html',language=language,framework=framework)
    return render_template('page01.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__=='__main__':
    app.run()