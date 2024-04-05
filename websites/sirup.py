from flask import Blueprint, render_template
import pandas as pd

# Create a Blueprint
sirup = Blueprint("sirup", __name__)