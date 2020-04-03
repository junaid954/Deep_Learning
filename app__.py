from flask import Flask, templating
app = Flask("rock")
@app.route("/heap/")
def rain ():
    return templating.render_template("index.html")

