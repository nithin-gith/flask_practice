from opcode import hascompare
from flask import Flask,render_template
import json
app = Flask(__name__)

data_file = open('data.json',"r")
data = json.loads(data_file.read()) 


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',posts=data,title= "Home")

@app.route('/about')
def about():
    return render_template('about.html',title ="About") 

if __name__ == '__main__':
    app.run(debug=True)