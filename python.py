from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def main():
    return "Welcome to gangwar Final Test API Server"

@app.route('/host')
def host():
    return f"Hostname: {socket.gethostname()}"

@app.route('/ip')
def ip():
    import requests
    return f"My IP is: {requests.get('https://api.ipify.org').text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
