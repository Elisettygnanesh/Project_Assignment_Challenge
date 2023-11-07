from flask import Flask, render_template, request
import requests
app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template('Project-2.html')

@app.route("/book",methods=['POST'])
def get_weatherdata():
    url = "https://bible-memory-verse-flashcard.p.rapidapi.com/get_chapter"
    querystring = {"book_name":request.form.get('book_name'),"chapter":request.form.get('chapter'),"text_mode":request.form.get("text_mode"),"uppercase_mode":request.form.get("uppercase_mode")}
    headers = {
	"X-RapidAPI-Key": "c0af90ad9fmsha3616858f9aad09p12a1cejsnb76392390c0a",
	"X-RapidAPI-Host": "bible-memory-verse-flashcard.p.rapidapi.com"}
    response = requests.get(url, headers=headers, params=querystring)
    data=response.json()
    return f"Data={data}"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005)

#Book name = 'John'
#Chapter number = '1'
#text mode = 'half' 
#uppercase mode = 'false'