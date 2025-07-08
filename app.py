from flask import Flask, jsonify
import json

app = Flask(__name__)

DATA_FILE = 'data.json'

@app.route('/api/')
def get_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except json.JSONDecodeError:
        return jsonify({"error": "Error reading data"}), 500

if __name__ == '__main__':
    app.run(debug=True)