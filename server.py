from flask import Flask
from routes import setup_routes
from config import PORT

app = Flask(__name__)
setup_routes(app)

if __name__ == "__main__":
    app.run(port=PORT)
