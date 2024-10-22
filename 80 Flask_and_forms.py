from tinydb import TinyDB, Query  # Import TinyDB for database handling and Query for searching
from flask import Flask, request  # Import Flask to create the web app and request to handle form data

app = Flask(__name__)  # Initialize the Flask app

# Initialize the TinyDB database for storing user credentials
db = TinyDB('./Support Files/80_Flask_forms_databse.json')
User = Query()  # Create a TinyDB query object for searching users


# Route to handle the form submission (POST request)
@app.route("/process", methods=["POST"])
def process():
    isthere = False  # Variable to check if user exists
    page = ""  # Variable to store the HTML content for the response
    form = request.form  # Get the submitted form data
    user = form["Username"]  # Get the username from the form
    ans = form["Password"]  # Get the password from the form

    try:
        # Search for the user in the database
        result = db.search(User.name == user)
        isthere = True  # User found
    except:
        # If the search fails, return an error message
        page += "Username, email, or password incorrect"
        return page

    try:
        # Retrieve the original password from the database
        password_original = result[0]["password"]

        # Check if the entered password matches the original
        if ans == password_original:
            try:
                # Open the HTML template for the dashboard or page
                with open("static/Template/Blog.html", "r") as f:
                    page = f.read()
            except IOError:
                # If the template file cannot be opened, return an error message
                print("Error: Unable to open the template file.")
                return "Error: Unable to open the template file.", 500

            # Replace placeholders in the HTML template with actual data
            page = page.replace("{Day entry}", "3158")  # Replace placeholder with Day entry
            page = page.replace("{Text}", "Welcome aboard Captain")  # Replace placeholder with welcome text
            page = page.replace("{link}", " ")  # Replace placeholder with an empty link
        else:
            # If the password does not match, show an error message
            page += "Username, email, or password incorrect"
    except:
        # Handle any exceptions that occur during password verification
        page += "Username, email, or password incorrect"

    return page  # Return the final page content (either the template or an error message)


# Route for the homepage that displays the login form
@app.route('/')
def index():
    # HTML content for the login form, which submits to "/process" via POST
    page = """
    <form method="post" action="/process">
        <p>Name: <input type="text" name="Username" required></p>
        <p>Email: <input type="email" name="Email" required></p>
        <p>Password: <input type="password" name="Password" required></p>
        <input type="hidden" name="user ID" value="232">  <!-- Hidden field for additional user data -->
        <button type="submit">Login</button>
    </form>"""
    return page  # Return the form as the homepage content


# Start the Flask app on host '0.0.0.0' and port 81
app.run(host='0.0.0.0', port=81)
