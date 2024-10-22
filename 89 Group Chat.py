from flask import Flask, render_template_string, render_template, request, redirect ,jsonify, session
import json
from datetime import datetime
from tinydb import TinyDB, Query

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to use sessions
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
page_signup = """
            <div class="boxed-title">
                <form method="POST" action="/sign_up_process">
                    <p>
                        Username: <input type="text" name="Username" required class="input-field">
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
# Helper function to sort messages by date
# Helper function to get the last 5 messages (newest at the bottom)
def get_last_five_messages(chat_data):
    all_messages = []  # Initialize a list to hold all messages across chats

    # Loop through each chat in the chat_data
    for chat in chat_data:
        username = chat["username"]  # Extract the username for each chat

        # Loop through each message in the current chat
        for message in chat["messages"]:
            # Append each message along with its username and date to all_messages
            all_messages.append({
                "username": username,
                "date": datetime.strptime(message["date"], "%Y-%m-%d %H:%M:%S"),
                # Convert date string to datetime object
                "message": message["message"]  # The actual message content
            })

    # Sort all messages by date in ascending order (oldest first)
    all_messages.sort(key=lambda x: x["date"], reverse=False)

    # Return the last 5 messages from the sorted list (newest of the oldest ones)
    return all_messages[-5:]


@app.route('/')
def index():
    # Load JSON file
    chat_data = load_chat_data()

    # Get the last 5 messages
    last_five_messages = get_last_five_messages(chat_data)

    # Load the HTML file and render it
    with open('Support Files/Group_chat/89_index.html', 'r') as html_file:
        html_content = html_file.read()

    # Pass session and the last 5 messages to the template
    return render_template_string(html_content, messages=last_five_messages, session=session)


# Sign In page route
@app.route('/sign-up')
def sign_up():
    return page_signup

# Login page route
@app.route('/login')
def login():
    return page_login


@app.route('/login_verification', methods=['POST'])
def login_verification():
    username = request.form.get('Username')
    password = request.form.get('Password')

    # Load the JSON chat data
    chat_data = load_chat_data()

    if username and password:
        # Check if the username exists and matches the password
        user = next((u for u in chat_data if u["username"] == username), None)

        if user and user["password"] == password:
            # Store the username in the session
            session['username'] = username
            # If the user is Manu3158, they are the admin
            if username == "Manu3158":
                session['admin'] = True
            else:
                session['admin'] = False

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

# Load the JSON data
def load_chat_data():
    with open('Support Files/Group_chat/89_group_chat.json', 'r') as f:
        return json.load(f)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the user from the session
    session.pop('admin', None)  # Remove the admin status from the session
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


@app.route('/send_message', methods=['POST'])
def send_message():
    if 'username' in session:
        # Get the new message from the form
        new_message = request.form.get('new_message')
        username = session['username']

        # Load the current chat data
        chat_data = load_chat_data()

        # Find the user in the chat data and add the new message
        for user in chat_data:
            if user["username"] == username:
                user["messages"].append({
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "message": new_message
                })
                break

        # Save the updated data back to the JSON file
        with open('Support Files/Group_chat/89_group_chat.json', 'w') as f:
            json.dump(chat_data, f, indent=4)

        return redirect('/')
    else:
        return redirect('/login')

@app.route('/sign_up_process', methods=['POST'])
def signup_process():
    # Get the username and password from the submitted form
    username = request.form.get('Username')
    password = request.form.get('Password')

    # Load the current chat data (from a JSON file or other source)
    chat_data = load_chat_data()

    # Check if both username and password are provided
    if username and password:
        # Check if the username already exists in the chat data
        existing_user = next((user for user in chat_data if user["username"] == username), None)

        # If the username already exists, return an error message with a 400 status code
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400

        # Create a new user with the provided username and password (empty message list)
        new_user = {
            'username': username,
            'password': password,  # Password could be hashed for security purposes
            'messages': []  # Initialize an empty list for the user's messages
        }
        # Append the new user to the chat data
        chat_data.append(new_user)

        # Save the updated chat data to the JSON file
        with open('Support Files/Group_chat/89_group_chat.json', 'w') as f:
            json.dump(chat_data, f, indent=4)  # Write the modified chat data with pretty formatting
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
        return jsonify({"error": "Username and password are required"}), 400

@app.route('/delete_message', methods=['POST'])
def delete_message():
    # Check if the user is an admin (only admins can delete messages)
    if 'admin' in session and session['admin']:
        # Get the message date and username from the submitted form
        message_date = request.form.get('message_date')  # Date of the message to be deleted
        username = request.form.get('username')  # Username of the person who sent the message

        # Load the current chat data (from a JSON file or other source)
        chat_data = load_chat_data()

        # Find the user by matching the username
        for user in chat_data:
            if user["username"] == username:
                # Filter out the message with the specified date, effectively deleting it
                user["messages"] = [m for m in user["messages"] if m["date"] != message_date]
                break  # Stop looping after finding the user

        # Save the updated chat data back to the JSON file
        with open('Support Files/Group_chat/89_group_chat.json', 'w') as f:
            json.dump(chat_data, f, indent=4)  # Write the modified chat data with pretty formatting

        # Redirect to the homepage after deleting the message
        return redirect('/')
    else:
        # If the user is not an admin, redirect to the login page
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
