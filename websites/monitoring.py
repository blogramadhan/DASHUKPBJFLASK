from flask import Blueprint, render_template
import pandas as pd

# Create a Blueprint
monitoring_bp = Blueprint('monitoring_bp', __name__)