from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Project-4.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_preferences = request.form['user_preferences']
    if user_preferences == 'horror':
        return "Nun, Evil Dead, The Shining, The Exorcist, Psycho, Hereditary, Get Out, A Nightmare on Elm Street, The Conjuring, Halloween, It, The Babadook, The Witch, Saw, Paranormal Activity, The Texas Chain Saw Massacre, Rosemary's Baby, Sinister, The Ring, Don't Breathe, Poltergeist, Insidious-----Enjoy your movie night."
    elif user_preferences == 'comedy':
        return "Due Date, PK, Free Guy, Superbad, Anchorman: The Legend of Ron Burgundy, The Hangover, Bridesmaids, Step Brothers, The Grand Budapest Hotel, Ferris Bueller's Day Off, Dumb and Dumber, Super Troopers, Hot Fuzz, The Big Lebowski, Napoleon Dynamite, Old School, Tropic Thunder, Wedding Crashers, Shaun of the Dead, Groundhog Day, This Is the End, Zoolander and The 40-Year-Old Virgin.-----Enjoy your movie night."
    elif user_preferences == 'action':
        return "Avengers, Aquaman, Black Adam-----Enjoy your movie night."
    elif user_preferences == 'suspense':
        return "Nowhere, The Guilty, Gone Girl-----Enjoy your movie night."
    elif user_preferences == 'romance':
        return "365 Days, After, Titanic-----Enjoy your movie night."
    else:
        return "Sorry, at this time we are unable to providing your preference."

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)
