from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/seasons')
def seasons():
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime('%B')

    return render_template('seasons.html', now=now, year=current_year, month=current_month)

# New Page 1: Minnesota Wild Players Page
@app.route('/players')
def players():
    my_favorite = "Kirill Kaprizov"
    player_list = [
        "Kirill Kaprizov",
        "Matt Boldy",
        "Joel Eriksson Ek",
        "Brock Faber",
        "Marc-Andre Fleury"
    ]
    return render_template('players.html', favorite=my_favorite, players=player_list)

# New Page 2: Minnesota Wild Facts Page
@app.route('/facts')
def facts():
    top_fact = "The Minnesota Wild's official mascot is Nordy, who wears jersey #18,001 and has a green 'M' on his forehead!"
    fastest_speed = "Over 100 mph (NHL Slap Shot)"
    fact_list = [
        "The Minnesota Wild were founded in 1997 and played their inaugural NHL season in 2000–01.",
        "Xcel Energy Center in Saint Paul has been the Wild's home arena since their first season.",
        "The franchise officially retired jersey #1 in honor of the fans ('the Team of 18,000') on opening night.",
        "The team logo features an animal head contour incorporating a forest, a river, a red sky, and the North Star as the eye."
    ]
    return render_template('facts.html', featured_fact=top_fact, speed=fastest_speed, facts=fact_list)

if __name__ == '__main__':
    app.run(debug=True)
