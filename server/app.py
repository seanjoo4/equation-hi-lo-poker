# app.py

from flask import Flask, render_template, jsonify
from events import socketio
from utils.utils import *

app = Flask(__name__,
            static_folder='../client/static',
            template_folder='../client')

@app.route('/')
def index():
    deck = generate_deck()
    return render_template('index.html')

if __name__ == '__main__':
    socketio.init_app(app)
    socketio.run(app, host='128.10.2.13', port=5000, debug=True)