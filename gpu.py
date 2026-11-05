from flask import Flask,render_template,request
from bs4 import BeautifulSoup as bs4
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()