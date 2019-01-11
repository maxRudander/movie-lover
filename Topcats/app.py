from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from functions import get_headlines, get_title_content
import omdb

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search/<film>")
def movie_request(film):
	film_data = {
			'title': omdb.get_movie(film)['Title'],
			'plot': omdb.get_movie(film)['Plot']
			}
	return render_template("search.html", film_data=film_data)

'''@app.route("/static/<path:path>")
def serve_static_files(path):
    return send_from_directory("static", path)'''

if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)
