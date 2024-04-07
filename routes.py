import os
import random
import requests
from flask import redirect, render_template, request, url_for
from . import app, db
from .api import headers, base_url
from .models import Player

@app.route('/', methods=['GET', 'POST'])
def homepage():
    image_path = get_random_background_image()
    players = Player.query.all()
    return render_template('base.html', title='myFootball', image_path=image_path, players=players)

@app.route('/create_player', methods=['POST'])
def create_player():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    player = Player(first_name=first_name, last_name=last_name, times=0)
    db.session.add(player)
    db.session.commit()
    return redirect(url_for('homepage'))

@app.route('/<league>/<int:year>')
def get_standings(year, league):
    url = f"{base_url}/v3/standings?season={year}&league={league}"
    response = requests.get(url, headers=headers)
    standings = response.json()
    league = standings['response'][0]['league']['name']
    
    return render_template('standings.html', year=year, league=league, standings=standings)
    

@app.route('/196/<int:year>')
def get_wa_npl(year):
    url = f"{base_url}/v3/standings?season={year}&league=196"
    response = requests.get(url, headers=headers)
    standings = response.json()
    league = standings['response'][0]['league']['name']

    return render_template('WAnpl.html', year=year, league=league, standings=standings)

@app.route('/<league>/<int:year>/fixtures')
def get_league_fixtures(year, league):
    url = f"{base_url}/v3/fixtures?league={league}&season={year}"
    response = requests.get(url, headers=headers)
    fixtures = response.json()
    image_path = get_random_background_image()

    return render_template('fixtures.html', year=year, fixtures=fixtures, image_path=image_path)

@app.route('/<fixture>/stats')
def get_fixture_stats(fixture):
    print(fixture)
    url = f"{base_url}/v3/fixtures/statistics?fixture={fixture}"
    response = requests.get(url, headers=headers)
    stats = response.json()
    image_path = get_random_background_image()

    return render_template('stats.html', stats=stats, image_path=image_path)

def get_random_background_image():
    image_directory = 'static/images/'  # Update this with your image directory path
    image_files = os.listdir(image_directory)
    random_image = random.choice(image_files)
    return random_image
