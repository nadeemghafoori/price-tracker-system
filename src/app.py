from flask import Flask, render_template
from src.common.database import Database

app = Flask(__name__)
app.config.from_object('src.config')    # loading the config file inside the app
# used for securing cookies
app.secret_key = '<your-secret-key-here>'

@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/')             # www.mysite.com
def home():
    return render_template('home.html')

from src.models.users.views import user_blueprint           # a set of roots that can be put in a different file and registered in the main app
from src.models.alerts.views import alert_blueprint
from src.models.stores.views import store_blueprint
app.register_blueprint(user_blueprint, url_prefix = "/users")
app.register_blueprint(alert_blueprint, url_prefix = "/alerts")
app.register_blueprint(store_blueprint, url_prefix = "/stores")