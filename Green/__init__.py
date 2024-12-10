from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Import routes (imported after app creation to avoid circular import)
from Green import routes
