from flask import Flask
from flask_cors import CORS
import os

# Get the absolute path for the template and static folders
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, "../../templates")
static_dir = os.path.join(base_dir, "../../static")

app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir
)
CORS(app)

# Import routes after initializing Flask app to avoid circular import issues
from app import routes
