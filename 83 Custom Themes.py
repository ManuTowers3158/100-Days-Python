from tinydb import TinyDB, Query  # Import TinyDB and Query for potential database usage (though not used in this script)
from flask import Flask, request  # Import Flask to create the web app and request to handle query parameters

app = Flask(__name__)  # Initialize the Flask app

# Route for the homepage (currently returns an empty page)
@app.route('/')
def index():
    page = ""
    return page

# Route for the first entry
@app.route('/entry1', methods=["GET"])
def entry1():
    entry = "Entry 1"  # Set the title for the entry
    text = "El camino de los 1000 pasos empieza con 1"  # Set the text for the entry

    # Safely get the 'templ' query parameter from the URL (e.g., ?templ=alternative)
    templ = request.args.get("templ", "").lower()

    # Determine which stylesheet to use based on the 'templ' parameter
    if templ == "alternative":
        template = "static/Template/blog_style2.css"  # Use alternative stylesheet
    else:
        template = "static/Template/blog_style.css"  # Use default stylesheet

    # Try to read and process the HTML template file
    try:
        with open("static/Template/Blog_multi_style.html", "r") as f:
            page = f.read()  # Read the entire HTML file content
    except IOError:
        return "Error: Unable to open the template file.", 500  # Return error message if the file cannot be opened

    # Replace placeholders in the HTML template with actual data
    page = page.replace("{Template}", template)  # Replace the stylesheet placeholder
    page = page.replace("{Day entry}", entry)  # Replace the entry title placeholder
    page = page.replace("{Text}", text)  # Replace the entry text placeholder

    return page  # Return the processed HTML page

# Route for the second entry
@app.route('/entry2', methods=["GET"])
def entry2():
    entry = "Entry 2"  # Set the title for the entry
    text = "Venga ladrillo a ladrillo se hace castillo"  # Set the text for the entry

    # Safely get the 'templ' query parameter from the URL (e.g., ?templ=alternative)
    templ = request.args.get("templ", "").lower()

    # Example URL to use the alternative stylesheet: http://127.0.0.1:81/entry2?templ=alternative

    # Determine which stylesheet to use based on the 'templ' parameter
    if templ == "alternative":
        template = "static/Template/blog_style2.css"  # Use alternative stylesheet
    else:
        template = "static/Template/blog_style.css"  # Use default stylesheet

    # Try to read and process the HTML template file
    try:
        with open("static/Template/Blog_multi_style.html", "r") as f:
            page = f.read()  # Read the entire HTML file content
    except IOError:
        return "Error: Unable to open the template file.", 500  # Return error message if the file cannot be opened

    # Replace placeholders in the HTML template with actual data
    page = page.replace("{Template}", template)  # Replace the stylesheet placeholder
    page = page.replace("{Day entry}", entry)  # Replace the entry title placeholder
    page = page.replace("{Text}", text)  # Replace the entry text placeholder

    return page  # Return the processed HTML page

# Start the Flask app on host '0.0.0.0' and port 81
app.run(host='0.0.0.0', port=81)
