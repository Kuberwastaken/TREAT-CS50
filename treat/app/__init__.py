from flask import Flask
from flask_cors import CORS
import os

# Get the absolute path for the template and static folders
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, "../../templates") # Path to the templates folder
static_dir = os.path.join(base_dir, "../../static") # Path to the static folder

# Create an instance of the Flask class with the specified template and static folders
app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir
)

# Enable Cross-Origin Resource Sharing (CORS) for the app
CORS(app)

# Import routes after initializing the Flask app to avoid circular import issues
from app import routes
