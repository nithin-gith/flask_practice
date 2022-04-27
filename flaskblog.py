from flask import Flask, flash, redirect,render_template, url_for
from forms import RegistrationForm,LoginForm
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ENVIRONMENT_VARIABLE'

data_file = open('data.json',"r")
data = json.loads(data_file.read()) 


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',posts=data,title= "Home")

@app.route('/about')
def about():
    return render_template('about.html',title ="About") 

@app.route('/register',methods =['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',title ="Register", form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title ="Registration", form = form)

if __name__ == '__main__':
    app.run(debug=True)