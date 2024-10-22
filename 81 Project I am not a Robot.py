from tinydb import TinyDB, Query  # Import TinyDB for database handling and Query for searching
from flask import Flask, request  # Import Flask and request to handle form data

app = Flask(__name__)  # Initialize the Flask app

# Initialize TinyDB (though it's not currently used in this logic)
db = TinyDB('80_Flask_forms_databse.json')
User = Query()

# Route to handle form submission (POST request)
@app.route("/process", methods=["POST"])
def process():
    page = ""  # Variable to store the HTML response
    form = request.form  # Get the submitted form data
    made = form["metalmade"]  # Get the "Are you made of metal?" response
    question = form["Question"]  # Get the infinity +1 question response
    food = form["food"]  # Get the user's favorite food response

    # Check if the user is a robot based on their answers
    if made == "Yes" or food == "oil":  # Robot if "Yes" to metal or if favorite food is oil
        print("You are a Robot")
        # HTML response for robot detection
        page = """
           <html>
           <head>
               <style>
                   body {
                       background-color: #001f3f; /* Blue Navy background */
                       display: flex;
                       justify-content: center;
                       align-items: center;
                       height: 100vh;
                       margin: 0;
                   }
                   .center-box {
                       background-color: silver; /* Silver center box */
                       padding: 50px;
                       border-radius: 10px;
                       text-align: center;
                       font-family: Arial, sans-serif;
                       font-size: 24px;
                       color: #000;
                   }
               </style>
           </head>
           <body>
               <div class="center-box">
                   You are a robot 😡
               </div>
           </body>
           </html>
           """
    else:
        # Not a robot response
        print("You are not a Robot")
        page = """
            <html>
            <head>
                <style>
                    body {
                        background-color: #001f3f; /* Blue Navy background */
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .center-box {
                        background-color: silver; /* Silver center box */
                        padding: 50px;
                        border-radius: 10px;
                        text-align: center;
                        font-family: Arial, sans-serif;
                        font-size: 24px;
                        color: #000;
                    }
                </style>
            </head>
            <body>
                <div class="center-box">
                    You are not a robot 👍
                </div>
            </body>
            </html>
            """

    # Debugging print statements (uncomment if needed for debugging)
    # print(made, question, food)
    # page = f"""
    #     <h1>Form Data Received</h1>
    #     <p>Are you made of metal?: {made}</p>
    #     <p>What is infinity +1?: {question}</p>
    #     <p>What is your favorite food?: {food}</p>
    #     """

    return page  # Return the generated HTML page

# Route for the homepage that displays the form
@app.route('/')
def index():
    # HTML content for the form, which submits to "/process" via POST
    page = """
    <form method="post" action="/process">
        <p>Are you made of metal?:</p>
        <p><label><input type="radio" name="metalmade" value="Yes"> Yes</label></p>
        <p><label><input type="radio" name="metalmade" value="No"> No</label></p>
        <p>What is infinity +1?: <input type="text" name="Question" required></p>
        <!-- Dropdown Menu for favorite food -->
        <p>What is your favorite food?:</p>
        <select name="food">
            <option value="pizza">Apple</option>
            <option value="oil">Oil</option>
            <option value="chicken">Chicken</option>
        </select>
        <button type="submit">I am not a Robot</button>
    </form>"""
    return page  # Return the form as the homepage content

# Start the Flask app on host '0.0.0.0' and port 81
app.run(host='0.0.0.0', port=81)
