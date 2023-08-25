from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, async_mode='gevent')  

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/ws')
def ws_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/ws')
def ws_disconnect():
    print('Client disconnected')

@socketio.on('send_cpu_usage', namespace='/ws')
def send_cpu_usage(message):
    cpu_usage = message['cpu_usage']
    print('Received CPU Usage:', cpu_usage)
    socketio.emit('cpu_usage', cpu_usage, namespace='/ws')

if __name__ == '__main__':
    socketio.run(app, debug=True)



# https://desktime.com/pricing for hurerah copysot
# https://desktime.com/pricing
# tcpa.tools reference web

