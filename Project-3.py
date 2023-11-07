from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Project-3.html')

@app.route('/facebook')
def facebook():
    return render_template("facebook.html")

@app.route('/google')
def google():
    return render_template("google.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)
