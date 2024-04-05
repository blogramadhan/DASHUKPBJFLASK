from flask import Blueprint, render_template
import pandas as pd

# Create a Blueprint
epurchasing_bp = Blueprint('epurchasing_bp', __name__)