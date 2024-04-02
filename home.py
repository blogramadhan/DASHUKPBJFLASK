from flask import Blueprint, render_template_string
import pandas as pd

# Create a Blueprint
dataframe_bp = Blueprint('dataframe_bp', __name__)

# Sample DataFrame
data = {
    'Name': ['John Doe', 'Jane Doe', 'Jim Brown'],
    'Age': [23, 28, 31],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

@dataframe_bp.route('/')
def view_dataframe():
    # Convert DataFrame to HTML
    df_html = df.to_html(classes='table table-striped', index=False)

    # Simple HTML template
    html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flask DataFrame</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
                <h2>Pandas DataFrame to HTML</h2>
                {{ df_html | safe }}
            </div>
        </body>
        </html>
    """

    return render_template_string(html_template, df_html=df_html)
