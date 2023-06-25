from flask import Flask
from routes.main import main_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run()
