from flask import Flask, request, jsonify, render_template
from app import app
from app.model import analyze_script

# Define the home route which renders the index.html template
@app.route('/')
def home():
    return render_template('index.html')

# Define the upload route to handle POST requests for script analysis
@app.route('/upload', methods=['POST'])
def upload_script():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        # Extract the text content from the JSON data
        content = data.get('text', '')
        # Analyze the script for triggers
        triggers = analyze_script(content)
        # Return the triggers in a JSON response
        return jsonify({"triggers": triggers})
    except Exception as e:
        # Handle any exceptions and return an error message
        return jsonify({"error": str(e)}), 500
