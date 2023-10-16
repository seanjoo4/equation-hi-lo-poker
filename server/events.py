from flask_socketio import SocketIO
from utils.utils import generate_deck

socketio = SocketIO()

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