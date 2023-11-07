from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Project-1.html')

@app.route('/youtube')
def scrape_youtube():
    url = 'https://www.youtube.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return render_template('youtube.html', data=soup.prettify())
    return "Failed to fetch data from YouTube."

@app.route('/amazon')
def scrape_amazon():
    url = 'https://www.amazon.in/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return render_template('amazon.html', data=soup.prettify())
    return "Failed to fetch data from Amazon."

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)
