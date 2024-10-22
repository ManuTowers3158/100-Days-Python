from tinydb import TinyDB, Query
from flask import Flask, request, redirect , jsonify , render_template_string ,session

app = Flask (__name__)

db = TinyDB('Support Files/84_User_databse.json')
User = Query()

app.secret_key = 'your_secret_key_here'

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


@app.route('/process', methods=['GET'])
def process():
    action = request.args.get('action')
    if action == 'signup':
        return redirect("/signup")
    elif action == 'login':
        # Handle login logic
        return redirect("/login")
    else:
        return 'No action specified'


@app.route('/signup', methods=['GET'])
def signup():
    return page_signup


@app.route('/sign_up_process', methods=['POST'])
def signup_process():
    username = request.form.get('Username')
    email = request.form.get('Email')
    password = request.form.get('Password')

    if username and email and password:
        User = Query()
        existing_user = db.search(User.Username == username)

        if existing_user:
            return jsonify({"error": "Username already exists"}), 400

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
            # Store the username in the session
            session['username'] = username
            # HTML content for successful login
            success_page = f"""
                                    <!DOCTYPE html>
                                    <html lang="en">
                                    <head>
                                        <meta charset="UTF-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                        <title>Login Successful</title>
                                        <style>
                                            body {{
                                                display: flex;
                                                flex-direction: column;
                                                justify-content: center;
                                                align-items: center;
                                                height: 100vh;
                                                margin: 0;
                                                background-color: #001f3f; /* Dark navy blue background */
                                                color: #C0C0C0; /* Dark silver text color */
                                                font-family: Arial, sans-serif;
                                            }}
                                            .message-box {{
                                                background-color: #C0C0C0; /* Dark silver background */
                                                color: #0056b3; /* Night blue text color */
                                                padding: 20px;
                                                border: 2px solid #4a4a4a; /* Darker border for contrast */
                                                border-radius: 10px;
                                                text-align: center;
                                            }}
                                            .username {{
                                                margin-top: 10px;
                                                font-size: 1.2em;
                                                font-weight: bold;
                                            }}
                                            .logout-button {{
                                                margin-top: 20px;
                                                padding: 10px 20px;
                                                font-size: 1em;
                                                color: #fff;
                                                background-color: #0056b3;
                                                border: none;
                                                border-radius: 5px;
                                                cursor: pointer;
                                            }}
                                            .logout-button:hover {{
                                                background-color: #003d7a;
                                            }}
                                        </style>
                                    </head>
                                    <body>
                                        <div class="message-box">
                                            <p>Login successful</p>
                                            <p class="username">Welcome, {username}!</p>
                                            <form action="/logout" method="get">
                                                <button type="submit" class="logout-button">Logout</button>
                                            </form>
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

@app.route('/logout')
def logout():
    # Clear all session data and redirect to login page
    session.clear()
    return redirect('/')

app.run(host='0.0.0.0',port=81)
