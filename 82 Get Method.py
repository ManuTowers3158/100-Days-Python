from tinydb import TinyDB, Query  # Import TinyDB for database handling (though not used in this current script)
from flask import Flask, request  # Import Flask to create the web app and request to handle URL query parameters

app = Flask(__name__)  # Initialize the Flask app

# Route to handle the homepage with a GET request
@app.route('/', methods=["GET"])
def index():
    get = request.args  # Get the query parameters from the URL
    # Example URL: http://127.0.0.1:81/?lang=spanish
    if get["lang"].lower() == "spanish":  # Check if the 'lang' parameter is 'spanish'
        # Return the page in Spanish
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
                           "Jefe Maestro no se detenga, el Covenant está muy cerca"
                       </div>
                   </body>
                   </html>
                   """
        return page
    else:
        # Return the page in English (default case)
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
                           "Welcome aboard Captain Torres"
                       </div>
                   </body>
                   </html>
                   """
        return page

# Start the Flask app on host '0.0.0.0' and port 81
app.run(host='0.0.0.0', port=81)
