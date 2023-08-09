from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/calculate', methods=['POST'])
def calculate():
    return ''