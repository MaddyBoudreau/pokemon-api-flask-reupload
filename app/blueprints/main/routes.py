from flask import render_template, redirect, url_for, request, flash
from . import bp as app
from app.blueprints.main.models import Pokemon
from flask_login import login_required, current_user
import requests
from app import db

my_request = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = my_request.json()

@app.route("/")
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    pokemon = Pokemon.query.all()

    pokemon.sort(key=lambda post: post.date_created, reverse=True)

    print(pokemon)

    context = {
        "pokemon": pokemon,
    }


@app.route("/usercollection")
def usercollection():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('usercollection.html')