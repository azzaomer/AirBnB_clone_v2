from flask import Flask

app = Flask(__name__)

@app.route("/")
deff hello_world():
    return "Hello HBNB!"
