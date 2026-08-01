"""Meridian Retail storefront — a tiny Flask app packaged as a container.

Routes:
  /         → greeting + which version/revision answered (as JSON)
  /healthz  → returns 200 so Cloud Run's health check keeps the revision serving

The greeting and version come from environment variables so you can change what
the app says at deploy time — without rebuilding the image. Cloud Run injects
PORT (default 8080) and K_REVISION (the revision that handled the request), which
this app reads to prove which build/deploy you're talking to.
"""
import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)

GREETING = os.environ.get("GREETING", "Hello from Meridian Retail")
VERSION = os.environ.get("APP_VERSION", "1.0")
# Cloud Run sets K_REVISION; locally we fall back to the hostname.
REVISION = os.environ.get("K_REVISION", socket.gethostname())


@app.route("/")
def home():
    return jsonify(message=GREETING, version=VERSION, revision=REVISION)


@app.route("/healthz")
def healthz():
    return "ok\n", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))