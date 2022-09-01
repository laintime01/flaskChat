# This is a flask chat page using flask and flask-socketio
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def manage_message(message):
    print("Received message: " + message)
    if message != "User connected!":
        send(message, broadcast=True)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    # can change localhost to 192.168.x.x to chat with other pc
    socketio.run(app, host="localhost", allow_unsafe_werkzeug=True)
