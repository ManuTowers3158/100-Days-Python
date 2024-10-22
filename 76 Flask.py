# This Flask web application serves as a simple portfolio and link tree.
# It allows users to navigate between a "LinkTree" page and a "MyPortfolio" page.

from flask import Flask  # Import Flask to create the web application

app = Flask(__name__,
            static_url_path="/static")  # Initialize the Flask app, set the static folder for serving static files (CSS, images)


# Route for the homepage, providing links to "LinkTree" and "MyPortfolio" pages
@app.route('/')
def index():
    # HTML content with links to two other pages
    page = f"""<html><body>
    <p><a href = "/LinkTree"> LinkTree </a></p>
    <p><a href = "/MyPortfolio"> MyPortfolio </a></p>
    </body>
    </html>"""
    return page  # Return the HTML page


# Route for the "LinkTree" page
@app.route("/LinkTree")
def LinkTree():
    # HTML content for the LinkTree page, which displays personal links (LinkedIn, GitHub, YouTube) and a profile image
    page = """
<html>
<head>
    <meta charset="UTF-8">
    <meta name ="viewport" content="width=device-width">
    <title>LinkTree</title>
    <link href="/static/75_Tree_Style.css" rel="stylesheet" type="text/css"/>  <!-- Link to external CSS file -->
</head>
<body>
    <h1 class="boxed-title">Manuel Torres</h1>  <!-- Title with name -->
    <img src="static/Manu_profile.jpg" width="50%">  <!-- Profile image -->
    <p class="p2"> If you think it is possible, you have to make it possible</p>
    <h2 class="boxed-h2">Professional</h2>  <!-- Section for professional links -->
    <div class="link-box">
    <p><a href="https://www.linkedin.com/in/manutorres0520/"> LinkedIn</a></p>
    <p><a href="https://github.com/ManuTowers3158"> GitHub</a></p>
    <p><a href="https://www.youtube.com/@ManuelTorres-nm6hi"> YouTube</a></p>
    </div>
    <script src="script.js"></script>  <!-- Link to external JavaScript file (optional functionality) -->
</body>
</html>"""
    return page  # Return the HTML page


# Route for the "MyPortfolio" page
@app.route("/MyPortfolio")
def MyPortfolio():
    # HTML content for the MyPortfolio page, showcasing various projects with descriptions and YouTube links
    page = """
<html>
<head>
    <meta charset="UTF-8">
    <meta name ="viewport" content="width=device-width">
    <title>Portfolio</title>
    <link href="static/blog_style.css" rel="stylesheet" type="text/css"/>  <!-- Link to external CSS file -->
</head>
<body>
    <h1 class="boxed-title">Manuel Torres Portfolio</h1>

    <!-- Project descriptions with images and YouTube links -->
    <h2 class="boxed-h2">Day 72 Project Secret Diary</h2>
    <p>This challenge provides a practical introduction to security measures in software development, particularly in the context of user authentication systems.
        <a href="https://www.youtube.com/watch?v=hyNIcmTi7lU&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=121"> Link to day 72</a></p>
    <img src="static/72.png" width="50%">

    <h2 class="boxed-h2">Day 69 Project GUI Story Path</h2>
    <p>This challenge is an excellent opportunity to practice integrating various programming skills in a creative project.
        <a href="https://www.youtube.com/watch?v=edwWQJUxApQ&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=115"> Link to day 69</a></p>
    <img src="static/69.png" width="50%">

    <h2 class="boxed-h2">Day 65 Project Character Object Programming</h2>
    <p> This challenge enhanced our ability to define and manipulate classes and subclasses in Python.
        <a href="https://www.youtube.com/watch?v=edfFZoCDou0&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=107"> Link to day 65</a></p>
    <img src="static/65.png" width="50%">

    <h2 class="boxed-h2">Day 56 Project Music Streaming</h2>
    <p>The Day 56 Challenge provided an engaging exercise in organizing a list of songs from a CSV file into artist-specific directories.
    <a href="https://www.youtube.com/watch?v=aahj2VWYra4&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=89"> Link to day 56</a></p>
    <img src="static/56.png" width="50%">

    <h2 class="boxed-h2">Day 14 Project Rock, Paper Scissors</H2>
    <p>This challenge tasked participants with creating a digital version of the classic game Rock, Paper, Scissors.
        <a href="https://www.youtube.com/watch?v=5YP8QIpR1SQ&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=16"> Link to day 14</a></p>
    <img src="static/14.png" width="50%">

    <script src="script.js"></script>  <!-- Link to external JavaScript file (optional functionality) -->
</body>
</html>"""
    return page  # Return the HTML page


# Run the Flask app on host '0.0.0.0' and port 81
app.run(host='0.0.0.0', port=81)
