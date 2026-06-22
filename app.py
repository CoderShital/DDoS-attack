from flask import Flask
from utils import logger_config
from routes.main_routes import main_bp
from routes.dashboard_routes import dashboard_bp
from routes.extension_routes import extension_bp

app = Flask(__name__)

@app.route("/log")
def all_logs():
    pass


app.register_blueprint(main_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(extension_bp)

if __name__ == "__main__":
    app.run(debug=True)