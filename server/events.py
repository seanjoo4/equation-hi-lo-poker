from flask_socketio import emit
import socketio

@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)

@socketio.on('connect')
def handle_connect():
    emit('message', 'User connected', broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    emit('message', 'User disconnected', broadcast=True)