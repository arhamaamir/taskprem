import socket
import time
import socketio

host = socket.gethostname()
port = 5000

sio = socketio.Client()

@sio.on('connect', namespace='/ws')
def ws_connect():
    print('Connected to server')

@sio.on('disconnect', namespace='/ws')
def ws_disconnect():
    print('Client disconnected')

sio.connect('http://localhost:5000/ws', wait_timeout = 10)  


client = socket.socket()
client.connect((host, port))

while True:

    cpu_usage = client.recv(1024).decode()  
    print("CPU usage of System from First Program:", cpu_usage)

    sio.emit('send_cpu_usage', {'cpu_usage': cpu_usage}, namespace='/ws')

