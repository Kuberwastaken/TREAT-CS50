from flask import Flask, request, jsonify, render_template
from app import app
from app.model import analyze_script

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_script():
    try:
        data = request.get_json()
        content = data.get('text', '')
        triggers = analyze_script(content)
        return jsonify({"triggers": triggers})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
