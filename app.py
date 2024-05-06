import datetime
from flask import Flask
from waitress import serve

app = Flask(__name__)

last_visit_map = {}


@app.route("/ping")
def ping():
    return "Pong"


@app.route("/profile/<name>")
def profile(name: str):
    last_visit = "This is your first visit!"
    if last_visit_map.__contains__(name):
        last_visit = "Your last visit was at " + last_visit_map.get(name).strftime("%H:%M:%S on %d/%M/%Y") + "!"

    last_visit_map[name] = datetime.datetime.now()
    return f"Welcome to you profile {name}. {last_visit}"


if __name__ == '__main__':
    serve(app=app, host="0.0.0.0", port=8080)
