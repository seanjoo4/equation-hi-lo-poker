# server.py

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return "Flask with SocketIO is running!"

@socketio.on('connect')
def handle_connection():
    print('Client connected')
    
@socketio.on('disconnect')
def handle_disconnection():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000)
