from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/home', methods=['POST'])
def index():
    answer = request.form['guess']

    
    if "Hello World!" in answer or "Hello World"  in answer:
        return render_template("index.html", guess = "Hello World! How Are You Today? Follow This URL To Find Out: https://soundcloud.com/louie-zong/hello-world ")
        

    else:
        return render_template("index.html",guess="That's Not Right...Better Luck Next Time...")
    
    

@app.route('/')
def home():
        return render_template('index.html')


if __name__ == "__main__":
    app.run( debug = True)