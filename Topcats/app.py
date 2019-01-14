from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
import omdb
import tmdb

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search/<film>")
def movie_request(film):
	film_data = {
			'title': omdb.get_movie(film)['Title'],
			'plot': omdb.get_movie(film)['Plot'],
			'poster': tmdb.get_poster(film)
			}
	return render_template("test.html", film_data=film_data)

if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)
