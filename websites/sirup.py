from flask import Blueprint, render_template
import pandas as pd

# Create a Blueprint
sirup_bp = Blueprint('sirup_bp', __name__)