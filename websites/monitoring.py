from flask import Blueprint, render_template
import pandas as pd

# Create a Blueprint
monitoring = Blueprint("monitoring", __name__)