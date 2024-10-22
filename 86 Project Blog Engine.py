from flask import Flask, render_template_string, render_template, request, redirect ,jsonify, session
import json
from tinydb import TinyDB, Query

app = Flask(__name__, static_folder='Support Files/Blog_Engine')
# Set the secret key for session management
app.secret_key = 'your_secret_key'
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
db = TinyDB('Support Files/Blog_Engine/86_User_database.json')


def load_missions():
    # Load the mission entries from the JSON file
    with open('./Support Files/Blog_Engine/86_Blog_Entries.json', 'r') as file:
        return json.load(file)


@app.route('/')
def index():
    # Load missions from JSON file
    missions = load_missions()

    if 'username' in session:
        login_button_text = 'Logout'
        button_value = 'logout'
        show_entry_form = True
    else:
        login_button_text = 'Log In'
        button_value = 'login'
        show_entry_form = False

    # Updated HTML template with logo and title side by side
    template = """
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Manu's Blog</title>
            <style>
                body {
                    background-color: #001f3f; /* Dark navy blue background */
                    color: white; /* Text color for the body */
                    font-family: Arial, sans-serif; /* Font family */
                    display: flex;
                    flex-direction: column; /* Stack elements vertically */
                    align-items: flex-start; /* Align items to the left */
                    height: 100vh; /* Full viewport height */
                    margin: 0; /* Remove default margin */
                    padding: 20px; /* Add padding to the body */
                    box-sizing: border-box; /* Ensure padding is included in width */
                }
                .header {
                    display: flex;
                    flex-direction: column; /* Stack elements vertically in the header */
                    align-items: flex-start; /* Align items to the left */
                    margin-bottom: 20px; /* Space below the header */
                    width: 100%; /* Ensure the header takes full width */
                }
                .header-top {
                    display: flex;
                    align-items: center; /* Align items vertically centered */
                    width: 100%; /* Ensure the container takes full width */
                    position: relative; /* Position relative to align the button */
                }
                .logo {
                    width: 100px; /* Adjust logo size */
                    height: 100px; /* Ensure height matches width for circular shape */
                    margin-right: 20px; /* Space between logo and title */
                    border-radius: 50%; /* Make the image circular */
                    object-fit: cover; /* Ensure image fits well within the circle */
                }
                .title-container {
                    background-color: #C0C0C0; /* Silver grey background for the title box */
                    padding: 10px 20px; /* Space inside the box */
                    border-radius: 5px; /* Rounded corners */
                    margin-right: 20px; /* Space between title box and login button */
                }
                .title {
                    color:  #0056b3; /* Navy blue text color */
                    font-size: 2em; /* Font size for the title */
                    margin: 0; /* Remove default margin */
                }
                .login-button {
                    background-color: #C0C0C0; /* Silver grey background */
                    color: #001f3f; /* Dark navy blue text color */
                    border: 2px solid #001f3f; /* Dark blue border */
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-size: 16px;
                    text-align: center;
                    cursor: pointer;
                    transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
                    position: absolute; /* Positioning to place it relative to the header */
                    top: 50%; /* Position it in the middle vertically of the header-top */
                    right: 20px; /* Adjust this value to move the button horizontally */
                }
                .login-button:hover {
                    background-color: #001f3f; /* Dark navy blue background on hover */
                    color: #C0C0C0; /* Dark silver text color on hover */
                }
                .subheader {
                    color: #C0C0C0; /* Dark silver text color */
                    font-size: 1.5em; /* Font size for the subheader */
                    margin: 0 0 20px 0; /* Margin below the subheader */
                }
                .mission {
                    background-color: #C0C0C0; /* Silver grey background for each mission */
                    color: #001f3f; /* Dark navy blue text color for the body of the entry */
                    padding: 15px;
                    border-radius: 8px;
                    margin-bottom: 20px;
                    width: 60vw; /* Fixed width of 60% of the viewport width */
                    box-sizing: border-box; /* Ensure padding is included in width */
                }
                .mission .entry-title {
                    color: #001f3f; /* Dark navy blue text color for the entry titles */
                    font-size: 1em;
                    font-weight: bold;
                }
                .mission .date {
                    color: gray; /* Gray text color for the date */
                }
                .entry-form {
                    background-color: #C0C0C0; /* Silver grey background */
                    color: #001f3f; /* Dark navy blue text color */
                    padding: 20px;
                    border-radius: 8px;
                    margin-top: 20px; /* Space above the form */
                    margin-bottom: 40px; /* Add space below the form */
                    width: 60vw; /* Fixed width of 60% of the viewport width */
                    box-sizing: border-box; /* Ensure padding is included in width */
                    display: flex;
                    flex-direction: column; /* Stack form elements vertically */
                }
                .entry-form input, .entry-form textarea {
                    width: 100%;
                    padding: 10px;
                    font-size: 16px;
                    margin-bottom: 10px;
                    border: 2px solid #001f3f; /* Dark navy blue border */
                    border-radius: 5px;
                    box-sizing: border-box; /* Include padding and border in element's total width and height */
                }
                
                .entry-form input[type="date"] {
                    font-size: 16px;
                }
                
                .entry-form button {
                    background-color: #001f3f; /* Dark navy blue background */
                    color: #C0C0C0; /* Dark silver text color */
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                    transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
                }
                
                .entry-form button:hover {
                    background-color: #C0C0C0; /* Dark silver background on hover */
                    color: #001f3f; /* Dark navy blue text color on hover */
                }
                
                .form-spacer {
                    height: 40px; /* Adjust the height as needed for spacing */
                }
                
            </style>
        </head>
        <body>
            <div class="header">
                <div class="header-top">
                    <img src="{{ url_for('static', filename='Logo manu.png') }}" class="logo" alt="Blog Logo">
                    <div class="title-container">
                        <h1 class="title">Manu's Blog</h1>
                    </div>
                
                    <form method="get" action="/process">
                        <button type="submit" name="action" value={{ button_value }} class="login-button">
                        {{ login_button_text }}</button>
                    </form>
                </div>
            </div>
            
            <div class="subheader">Entries:</div>
            {% if show_entry_form %}
            <div class="entry-form">
                <form method="post" action="/submit_entry">
                    <input type="text" name="title" placeholder="Title" required>
                    <input type="date" name="date" required>
                    <textarea name="text" placeholder="Text" rows="4" required></textarea>
                    <button type="submit">Submit Entry</button>
                </form>
            </div>
            
            {% endif %}
            
            {% for mission in missions %}
            <div class="mission">
                <div class="entry-title">{{ mission.Title }}</div>
                <div class="date">{{ mission.Date }}</div>
                <p>{{ mission.Text }}</p>
            </div>
            {% endfor %}
            
        </body>
        </html>"""

    return render_template_string(template, missions=missions, login_button_text=login_button_text,button_value=
    button_value, show_entry_form=show_entry_form)

@app.route('/process', methods=['GET'])
def process():
    action = request.args.get('action')
    if action == 'signup':
        return redirect("/signup")
    elif action == 'login':
        # Handle login logic
        return redirect("/login")
    elif action == "logout":
        return redirect("/logout")

    else:
        return 'No action specified'

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
        # Store the username in the session
        session['username'] = username
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
                    <script>
                        // Redirect to login page after 3 seconds
                        setTimeout(function() {
                            window.location.href = "/";
                        }, 3000); // 3000 milliseconds = 3 seconds
                    </script>
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
    session.pop('username', None)  # Remove the user from the session
    logout_page = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Logout Successful</title>
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
                            <p>Logout successful</p>
                        </div>
                        <script>
                            // Redirect to login page after 1.5 seconds
                            setTimeout(function() {
                                window.location.href = "/";
                            }, 1500); // 1500 milliseconds = 1.5 seconds
                        </script>
                    </body>
                    </html>
                    """
    return render_template_string(logout_page)


def save_missions(missions):
    """Save mission entries to the JSON file."""
    with open('Blog_Engine/86_Blog_Entries.json', 'w') as file:
        json.dump(missions, file, indent=4)

@app.route('/submit_entry', methods=['POST'])
def submit_entry():
    title = request.form.get('title')
    date = request.form.get('date')
    text = request.form.get('text')

    # Load existing missions (if needed for further processing)
    missions = load_missions()

    # Add the new entry to the list
    new_entry = {
        'Title': title,
        'Date': date,
        'Text': text
    }
    missions.append(new_entry)

    # Save the updated missions back to the JSON file
    save_missions(missions)

    # After saving the entry, redirect to the home page
    return redirect('/')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
