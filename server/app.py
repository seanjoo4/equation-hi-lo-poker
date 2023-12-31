# app.py

from flask import Flask, render_template, jsonify
from events import socketio
from utils.utils import *

app = Flask(__name__,
            static_folder='../client/static',
            template_folder='../client')

@app.route('/')
def index():
    deck = shuffle_deck(generate_deck())
    players = generate_players(10)

    for player in  players:
        deal_cards(deck, player)
        print(str(player))

    return render_template('index.html')

if __name__ == '__main__':
    socketio.init_app(app)
    socketio.run(app, port=5000, debug=True)

