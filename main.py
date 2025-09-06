# app.py
import socket
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message="Привет, мир через Cloudflare Tunnel!")

@app.route('/api/data')
def get_data():
    return {"data": [1, 2, 3, 4, 5]}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)