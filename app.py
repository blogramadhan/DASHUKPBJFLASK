from flask import Flask
import pandas as pd
import duckdb
from home import home_bp
from sirup import sirup_bp
from spse import spse_bp
from epurchasing import epurchasing_bp
from monitoring import monitoring_bp

app = Flask(__name__)

# Daftarkan Blueprint
app.register_blueprint(home_bp)
app.register_blueprint(sirup_bp, url_prefix='/sirup')
app.register_blueprint(spse_bp, url_prefix='/spse')
app.register_blueprint(epurchasing_bp, url_prefix='/epurchasing')
app.register_blueprint(monitoring_bp, url_prefix='/monitoring')

if __name__ == '__main__':
    app.run(debug=True, port='1234')