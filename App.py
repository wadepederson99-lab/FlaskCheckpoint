from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# --- Page 1: Home Page ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index-results', methods=['GET', 'POST'])
def index_results():
    if request.method == 'POST':
        fan_name = request.form.get('fan_name', 'Wild Fan')
        years_fan = request.form.get('years_fan', '1')
        favorite_color = request.form.get('favorite_color', 'Forest Green')
        return render_template('index_results.html',
                               fan_name=fan_name,
                               years_fan=years_fan,
                               favorite_color=favorite_color)
    return redirect(url_for('index'))

# --- Page 2: About Page ---
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-results', methods=['GET', 'POST'])
def about_results():
    if request.method == 'POST':
        visitor_name = request.form.get('visitor_name', 'Wild Fan')
        attended = request.form.get('attended', 'Not yet')
        favorite_memory = request.form.get('favorite_memory', 'Cheering on the Wild!')
        return render_template('about_results.html',
                               visitor_name=visitor_name,
                               attended=attended,
                               favorite_memory=favorite_memory)
    return redirect(url_for('about'))

# --- Page 3: Seasons Page ---
@app.route('/seasons')
def seasons():
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime('%B')
    return render_template('seasons.html', now=now, year=current_year, month=current_month)

@app.route('/seasons-results', methods=['GET', 'POST'])
def seasons_results():
    if request.method == 'POST':
        fan_name = request.form.get('fan_name', 'Wild Fan')
        favorite_season = request.form.get('favorite_season', 'Winter')
        playoff_prediction = request.form.get('playoff_prediction', 'Stanley Cup Bound!')
        return render_template('seasons_results.html',
                               fan_name=fan_name,
                               favorite_season=favorite_season,
                               playoff_prediction=playoff_prediction)
    return redirect(url_for('seasons'))

# --- Page 4: Minnesota Wild Players Page ---
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

@app.route('/players-results', methods=['GET', 'POST'])
def players_results():
    if request.method == 'POST':
        fan_name = request.form.get('fan_name', 'Wild Fan')
        favorite_player = request.form.get('favorite_player', 'Kirill Kaprizov')
        position = request.form.get('position', 'Forward')
        reason = request.form.get('reason', 'Great player!')
        return render_template('players_results.html',
                               fan_name=fan_name,
                               favorite_player=favorite_player,
                               position=position,
                               reason=reason)
    return redirect(url_for('players'))

# --- Page 5: Minnesota Wild Facts Page ---
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

@app.route('/facts-results', methods=['GET', 'POST'])
def facts_results():
    if request.method == 'POST':
        fan_name = request.form.get('fan_name', 'Wild Fan')
        submitted_fact = request.form.get('submitted_fact', '')
        know_nordy = request.form.get('know_nordy', 'Yes')
        knowledge_level = request.form.get('knowledge_level', 'Superfan')
        return render_template('facts_results.html',
                               fan_name=fan_name,
                               submitted_fact=submitted_fact,
                               know_nordy=know_nordy,
                               knowledge_level=knowledge_level)
    return redirect(url_for('facts'))

if __name__ == '__main__':
    app.run(debug=True)
