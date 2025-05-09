import os
import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_info():
    author = os.getenv('AUTHOR', 'null')
    hostname = socket.gethostname()
    address = socket.gethostbyname(hostname)
    info = f"AUTHOR: {author}, Hostname: {hostname}, Ip: {address}"
    return info

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
