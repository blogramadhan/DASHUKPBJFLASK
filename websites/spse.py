from flask import Blueprint, render_template
import pandas as pd

# Create a Blueprint
spse = Blueprint("spse", __name__)