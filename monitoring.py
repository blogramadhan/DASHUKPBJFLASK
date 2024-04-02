from flask import Blueprint, render_template_string
import pandas as pd

# Create a Blueprint
monitoring_bp = Blueprint('monitoring_bp', __name__)