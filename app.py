from flask import Flask
import os

app = Flask(__name__)

INSTANCE_NAME = os.getenv("HOSTNAME", "flask-instance")

@app.route("/")
def index():
    print(f"Request handled by: {INSTANCE_NAME}", flush=True)
    return f"Hello from {INSTANCE_NAME}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
