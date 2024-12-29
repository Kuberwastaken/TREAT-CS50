from flask import Flask
from flask_cors import CORS

# Set the template and static folder paths
app = Flask(__name__, 
            template_folder='C:/Users/yokub/Documents/TREAT-Project/templates', 
            static_folder='C:/Users/yokub/Documents/TREAT-Project/static')
CORS(app)

from . import routes
