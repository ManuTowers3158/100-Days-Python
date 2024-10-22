from tinydb import TinyDB, Query
from flask import Flask, send_from_directory, abort

app = Flask(__name__)

# Initialize TinyDB
db = TinyDB('static/Template/Journal.json')


def get_text_and_link_for_key(db, key):
    query = Query()

    # Retrieve all entries from the database
    all_entries = db.all()

    # Print all entries to debug and verify the structure
    print("Database Entries:")
    for entry in all_entries:
        print(entry)

    # Check if the key exists directly in the entries
    for entry in all_entries:
        if entry.get('entry') == key:
            # Extract the 'data' dictionary
            data = entry.get('data', {})
            text = data.get('Text', None)
            link = data.get('link', None)
            return text, link

    print(f"No entry found for key {key}")
    return None, None


@app.route('/')
def index():
    return "Welcome to the Blog!"


@app.route('/<pageNumber>')
def pageChange(pageNumber):
    if not pageNumber.isdigit():
        abort(404)

    key_to_lookup = int(pageNumber)
    text, link = get_text_and_link_for_key(db, key_to_lookup)
    print(f"Text: {text}, Link: {link}")

    try:
        with open("static/Template/Blog.html", "r") as f:
            page = f.read()
    except IOError:
        print("Error: Unable to open the template file.")
        return "Error: Unable to open the template file.", 500

    # Replace placeholders in the HTML template
    page = page.replace("{Day entry}", pageNumber)
    page = page.replace("{Text}", text if text else "No text available")
    page = page.replace("{link}", link if link else "No link available")

    return page


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)


