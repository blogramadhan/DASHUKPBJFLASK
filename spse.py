from flask import Blueprint, render_template_string
import pandas as pd

# Create a Blueprint
spse_bp = Blueprint('spse_bp', __name__)