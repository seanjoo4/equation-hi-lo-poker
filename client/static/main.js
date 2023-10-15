var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    console.log('Connected to the server');
});

socket.on('response', function(data) {
    // Handle incoming messages from the server
    console.log('Received response:', data);
});

function sendMessage() {
    var message = document.getElementById('message').value;
    socket.emit('message', message);
}

document.addEventListener('DOMContentLoaded', function () {
    var sendButton = document.getElementById('sendButton');
    sendButton.addEventListener('click', function () {
        sendMessage();
    });
});

