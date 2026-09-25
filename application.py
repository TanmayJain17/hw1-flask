import os
import platform
import socket

from flask import Flask, jsonify

application = Flask(__name__)
app = application


@application.get("/")
def index():
    return jsonify(
        message="hello from HW1",
        host=socket.gethostname(),
        python=platform.python_version(),
        port=os.environ.get("PORT", "n/a"),
    )


@application.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
