from flask import request, jsonify
from app import app
from app.model import analyze_script

@app.route('/')
def home():
    return "Welcome to the TREAT Project!"

@app.route('/upload', methods=['POST'])
def upload_script():
    try:
        file = request.files['file']
        content = file.read().decode('utf-8')
        triggers = analyze_script(content)
        return jsonify({"triggers": triggers})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
