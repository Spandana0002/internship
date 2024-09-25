const socket = io();

const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const messagesDiv = document.getElementById('messages');

sendButton.onclick = () => {
    const message = messageInput.value;
    socket.emit('message', message);
    messageInput.value = '';
};

socket.on('response', (msg) => {
    const messageElement = document.createElement('div');
    messageElement.textContent = msg;
    messagesDiv.appendChild(messageElement);
});
