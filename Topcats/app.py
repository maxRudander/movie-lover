from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from functions import get_headlines, get_title_content

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

'''@app.route("/static/<path:path>")
def serve_static_files(path):
    return send_from_directory("static", path)'''

if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)
