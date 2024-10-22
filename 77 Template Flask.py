from flask import Flask,redirect
app= Flask(__name__,
static_url_path="/static")

@app.route('/')
def index():
    page = ""
    return page

@app.route("/blog/entry1")
def hr():
    return redirect("/entry1")

@app.route("/blog/entry2")
def br():
    return redirect("/entry2")


@app.route('/entry1')
def entry1():
    entry="Entry 1"
    text = "El camino de los 1000 pasos empieza con 1"
    link = "https://www.youtube.com/@ManuelTorres-nm6hi"
    page = ""
    f = open("static/Template/Blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{Day entry}",entry)
    page = page.replace("{Text}", text)
    page = page.replace("{link}", link)
    return page

@app.route('/entry2')
def entry2():
    entry="Entry 2"
    text = "Venga ladrillo a ladrillo se hace castillo"
    page = ""
    f = open("static/Template/Blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{Day entry}",entry)
    page = page.replace("{Text}", text)
    return page

app.run(host='0.0.0.0',port=81)