import socket
import time
import psutil

host = socket.gethostname()
port = 5000

server = socket.socket()
server.bind((host, port))

server.listen(1)
conn, address = server.accept()

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_usage_str = f"{cpu_usage}%"
    conn.sendall(cpu_usage_str.encode()) 


# server.close()
