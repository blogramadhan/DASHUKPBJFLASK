from flask import Blueprint, render_template_string
import pandas as pd

# Create a Blueprint
sirup_bp = Blueprint('sirup_bp', __name__)