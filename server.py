from flask import Flask

app = Flask(__name__)
@app.route("/")
def helloword():
    return "<b>My First Flask application in action!</br>"