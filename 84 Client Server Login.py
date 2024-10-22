import time

from tinydb import TinyDB, Query
from flask import Flask, request, redirect , jsonify , render_template_string

app = Flask (__name__)

db = TinyDB('./Support Files/84_User_databse.json')
User = Query()

page_signup = """
            <div class="boxed-title">
                <form method="POST" action="/sign_up_process">
                    <p>
                        Username: <input type="text" name="Username" required class="input-field">
                    </p>
                    <p>
                        Email: <input type="email" name="Email" required class="input-field">
                    </p>
                    <p>
                        Password: <input type="password" name="Password" required class="input-field">
                    </p>
                    <button type="submit" class="button">Sign Up</button>
                    
                </form>
            </div>
            <style>
                body {
                    background-color: #001f3f; /* Dark navy blue background */
                    color: white; /* Text color for the body */
                    font-family: Arial, sans-serif; /* Font family */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh; /* Full viewport height */
                    margin: 0; /* Remove default margin */
                }
                .boxed-title {
                    background-color: #C0C0C0; /* Dark silver background */
                    color: #0056b3; /* Night blue text color */
                    padding: 20px; /* Space inside the box */
                    border: 2px solid #4a4a4a; /* Darker border for contrast */
                    border-radius: 10px; /* Rounded corners */
                    text-align: center; /* Center align the text */
                    margin: 20px auto; /* Margin around the box */
                    max-width: 90%; /* Maximum width for responsiveness */
                }
                .input-field {
                    width: 90%; /* Full width for inputs */
                    padding: 10px;
                    font-size: 16px;
                    border: 2px solid #001f3f; /* Dark navy blue border */
                    border-radius: 5px;
                    margin-bottom: 10px; /* Space between input fields */
                    box-sizing: border-box; /* Include padding and border in element's total width and height */
                }
                .button {
                    display: inline-block;
                    padding: 10px;
                    font-size: 16px;
                    color: #C0C0C0; /* Dark silver text color */
                    background-color: #001f3f; /* Dark navy blue background */
                    border: 2px solid #001f3f; /* Blue border to match background */
                    border-radius: 5px;
                    text-align: center;
                    cursor: pointer;
                    transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
                    font-family: Arial, sans-serif; /* Ensure consistent font */
                    width: 200px; /* Fixed width for buttons */
                    margin: 10px 0; /* Space around buttons */
                }
                .button:hover {
                    background-color: #C0C0C0; /* Dark silver background on hover */
                    color: #001f3f; /* Dark navy blue text color on hover */
                }
                form {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                p {
                    margin: 10px 0; /* Space between paragraphs */
                    width: 100%; /* Ensure full width for alignment */
                }
                input {
                    box-sizing: border-box; /* Ensure padding and border are included in the width */
                }
            </style>
        """

page_login = """
            <div class="boxed-title">
                <form method="post" action="/login_verification">
                    <p>
                        Username: <input type="text" name="Username" required class="input-field">
                    </p>
                    <p>
                        Password: <input type="password" name="Password" required class="input-field">
                    </p>
                    <button type="submit" name="action" value="True" class="button">Log in</button>
                    
                </form>
            </div>
            <style>
                body {
                    background-color: #001f3f; /* Dark navy blue background */
                    color: white; /* Text color for the body */
                    font-family: Arial, sans-serif; /* Font family */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh; /* Full viewport height */
                    margin: 0; /* Remove default margin */
                }
                .boxed-title {
                    background-color: #C0C0C0; /* Dark silver background */
                    color: #0056b3; /* Night blue text color */
                    padding: 20px; /* Space inside the box */
                    border: 2px solid #4a4a4a; /* Darker border for contrast */
                    border-radius: 10px; /* Rounded corners */
                    text-align: center; /* Center align the text */
                    margin: 20px auto; /* Margin around the box */
                    max-width: 90%; /* Maximum width for responsiveness */
                }
                .input-field {
                    width: 90%; /* Full width for inputs */
                    padding: 10px;
                    font-size: 16px;
                    border: 2px solid #001f3f; /* Dark navy blue border */
                    border-radius: 5px;
                    margin-bottom: 10px; /* Space between input fields */
                    box-sizing: border-box; /* Include padding and border in element's total width and height */
                }
                .button {
                    display: inline-block;
                    padding: 10px;
                    font-size: 16px;
                    color: #C0C0C0; /* Dark silver text color */
                    background-color: #001f3f; /* Dark navy blue background */
                    border: 2px solid #001f3f; /* Blue border to match background */
                    border-radius: 5px;
                    text-align: center;
                    cursor: pointer;
                    transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
                    font-family: Arial, sans-serif; /* Ensure consistent font */
                    width: 200px; /* Fixed width for buttons */
                    margin: 10px 0; /* Space around buttons */
                }
                .button:hover {
                    background-color: #C0C0C0; /* Dark silver background on hover */
                    color: #001f3f; /* Dark navy blue text color on hover */
                }
                form {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                p {
                    margin: 10px 0; /* Space between paragraphs */
                    width: 100%; /* Ensure full width for alignment */
                }
                input {
                    box-sizing: border-box; /* Ensure padding and border are included in the width */
                }
            </style>
        """

@app.route('/')
def index():
    page = """
        <div class="boxed-title">
            <form method="get" action="/process">
                <p><button type="submit" name="action" value="signup" class="button">Sign Up</button></p>
                <p><button type="submit" name="action" value="login" class="button">Login</button></p>
            </form>
        </div>
        <style>
            body {
                background-color: #001f3f; /* Dark navy blue background */
                color: white; /* Text color for the body */
                font-family: Arial, sans-serif; /* Font family */
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh; /* Full viewport height */
                margin: 0; /* Remove default margin */
            }
            .boxed-title {
                background-color: #C0C0C0; /* Dark silver background */
                color: #0056b3; /* Night blue text color */
                padding: 20px; /* Space inside the box */
                border: 2px solid #4a4a4a; /* Darker border for contrast */
                border-radius: 10px; /* Rounded corners */
                text-align: center; /* Center align the text */
                margin: 20px auto; /* Margin around the box */
                max-width: 90%; /* Maximum width for responsiveness */
            }
            .button {
                display: inline-block;
                padding: 10px;
                font-size: 16px;
                color: #C0C0C0; /* Dark silver text color */
                background-color: #001f3f; /* Dark navy blue background */
                border: 2px solid #001f3f; /* Blue border to match background */
                border-radius: 5px;
                text-align: center;
                cursor: pointer;
                transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
                font-family: Arial, sans-serif; /* Ensure consistent font */
                width: 150px; /* Fixed width for buttons */
                margin: 10px; /* Space around buttons */
            }
            .button:hover {
                background-color: #C0C0C0; /* Dark silver background on hover */
                color: #001f3f; /* Dark navy blue text color on hover */
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            p {
                margin: 10px 0; /* Space between paragraphs */
            }
        </style>
    """

    return page

# Route to handle the action parameter and redirect to either sign-up or login
@app.route('/process', methods=['GET'])
def process():
    action = request.args.get('action')  # Get the 'action' parameter from the URL
    if action == 'signup':
        return redirect("/signup")  # Redirect to the sign-up page if action is 'signup'
    elif action == 'login':
        return redirect("/login")  # Redirect to the login page if action is 'login'
    else:
        return 'No action specified'  # Return a message if no action is specified

# Route for the sign-up page (returns HTML form page content, e.g., page_signup could be defined elsewhere)
@app.route('/signup', methods=['GET'])
def signup():
    return page_signup  # This should be replaced with the actual sign-up form HTML page content

# Route to process the sign-up form data (POST request)
@app.route('/sign_up_process', methods=['POST'])
def signup_process():
    # Retrieve the form data (Username, Email, Password) submitted by the user
    username = request.form.get('Username')
    email = request.form.get('Email')
    password = request.form.get('Password')

    # Ensure all form fields are provided
    if username and email and password:
        User = Query()  # TinyDB query object for searching
        existing_user = db.search(User.Username == username)  # Search for existing user by username

        # If the username already exists, return an error message
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400  # Return a JSON response with error

        # Insert the new user's data into the database
        db.insert({
            'Username': username,
            'Email': email,
            'Password': password
        })

        # HTML content with JavaScript for redirection
        success_page = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Success</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #001f3f; /* Dark navy blue background */
                    color: #C0C0C0; /* Dark silver text color */
                    font-family: Arial, sans-serif;
                }
                .message-box {
                    background-color: #C0C0C0; /* Dark silver background */
                    color: #0056b3; /* Night blue text color */
                    padding: 20px;
                    border: 2px solid #4a4a4a; /* Darker border for contrast */
                    border-radius: 10px;
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <div class="message-box">
                <p>Sign up successful</p>
            </div>
            <script>
                // Redirect after 3 seconds
                setTimeout(function() {
                    window.location.href = "/login";
                }, 3000); // 3000 milliseconds = 3 seconds
            </script>
        </body>
        </html>
        """

        return render_template_string(success_page)

    else:
        return jsonify({"error": "Missing required fields"}), 400


@app.route('/login', methods=['GET'])
def login():
    return page_login


@app.route('/login_verification', methods=['POST'])
def login_verification():
    username = request.form.get('Username')
    password = request.form.get('Password')

    if username and password:
        User = Query()
        user = db.search(User.Username == username)

        if user and user[0]['Password'] == password:
            # HTML content for successful login
            success_page = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Login Successful</title>
                    <style>
                        body {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            margin: 0;
                            background-color: #001f3f; /* Dark navy blue background */
                            color: #C0C0C0; /* Dark silver text color */
                            font-family: Arial, sans-serif;
                        }
                        .message-box {
                            background-color: #C0C0C0; /* Dark silver background */
                            color: #0056b3; /* Night blue text color */
                            padding: 20px;
                            border: 2px solid #4a4a4a; /* Darker border for contrast */
                            border-radius: 10px;
                            text-align: center;
                        }
                    </style>
                </head>
                <body>
                    <div class="message-box">
                        <p>Login successful</p>
                    </div>
                    
                </body>
                </html>
                """
            return render_template_string(success_page)

        else:
            # HTML content for unsuccessful login
            error_page = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Login Failed</title>
                    <style>
                        body {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            margin: 0;
                            background-color: #001f3f; /* Dark navy blue background */
                            color: #C0C0C0; /* Dark silver text color */
                            font-family: Arial, sans-serif;
                        }
                        .message-box {
                            background-color: #C0C0C0; /* Dark silver background */
                            color: #0056b3; /* Night blue text color */
                            padding: 20px;
                            border: 2px solid #4a4a4a; /* Darker border for contrast */
                            border-radius: 10px;
                            text-align: center;
                        }
                    </style>
                </head>
                <body>
                    <div class="message-box">
                        <p>Incorrect Username/Password</p>
                    </div>
                    <script>
                        // Redirect to login page after 3 seconds
                        setTimeout(function() {
                            window.location.href = "/login";
                        }, 3000); // 3000 milliseconds = 3 seconds
                    </script>
                </body>
                </html>
                """
            return render_template_string(error_page)

    else:
        return jsonify({"error": "Username and password are required"}), 400

app.run(host='0.0.0.0',port=81)