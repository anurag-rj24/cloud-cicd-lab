from flask import Flask, render_template
import os

app = Flask(__name__)

# Customizable variables for demonstration
AUTHOR_NAME = "Anurag"
PIPELINE_STATUS = "CI/CD Pipeline is Live & Running!"
VERSION = "v2.0.0"
MESSAGE = "Updated live via GitHub CI/CD Pipeline!"

@app.route("/")
def index():
    return render_template(
        "index.html",
        name=AUTHOR_NAME,
        status=PIPELINE_STATUS,
        version=VERSION,
        message=MESSAGE,
        hostname=os.uname().nodename if hasattr(os, "uname") else os.environ.get("COMPUTERNAME", "k8s-pod")
    )

@app.route("/health")
def health():
    return {"status": "healthy", "version": VERSION, "author": AUTHOR_NAME}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
