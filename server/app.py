# app.py

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__,
            static_folder='../client/static',
            template_folder='../client')

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connection():
    print('Client connected')
    
@socketio.on('disconnect')
def handle_disconnection():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    socketio.emit('response', message)

if __name__ == '__main__':
    socketio.run(app, debug=True)