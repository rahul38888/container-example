import datetime
import logging
import logging.config
import socket

from flask import Flask
from waitress import serve

app = Flask(__name__)

last_visit_map = {}

logging.config.fileConfig("logging.ini")
logger = logging.getLogger("main")

host_ip = socket.gethostbyname(socket.gethostname())


@app.route("/ping")
def ping():
    logger.info("Ping api triggered")
    return "Pong"


@app.route("/profile/<name>")
def profile(name: str):
    logger.info(f"Profile api triggered by {name}")
    last_visit = f"This is your first visit on <b>{host_ip}</b>\n"
    if last_visit_map.__contains__(name):
        last_time = last_visit_map.get(name).strftime("%H:%M:%S on %d/%M/%Y")
        last_visit = f"Your last visit time on <b>{host_ip}</b> was <b>{last_time}</b>!\n"

    last_visit_map[name] = datetime.datetime.now()
    return f"Welcome to you profile {name}. {last_visit}"


if __name__ == '__main__':
    serve(app=app, host="0.0.0.0", port=8080)
