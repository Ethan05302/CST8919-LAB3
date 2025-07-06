from flask import Flask, request, jsonify
import logging
import sys

app = Flask(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/')
def home():
    logging.info("Home endpoint accessed.")  
    return "Flask Login App Lab 3 is Running."

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == "admin" and password == "password123":
        logging.info(f"Login SUCCESS for user: {username}")
        return jsonify({"message": "Login successful"}), 200
    else:
        logging.warning(f"Login FAILED for user: {username}")
        return jsonify({"message": "Login failed"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
