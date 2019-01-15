from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
import omdb
import tmdb
import wiki

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search/<film>")
def movie_request(film):
    try:
        film_data = {
            'title': omdb.get_movie(film)['Title'],
            'plot': omdb.get_movie(film)['Plot'],
			'video': tmdb.get_trailer(film),
            'junk' : wiki.get_wiki(film)
        }
        if film_data["plot"] == "N/A":
            film_data["plot"] = "Finns ingen beskrivning tillgänglig"

        return render_template("search.html", film_data=film_data)
    except KeyError:
        flash("Det finns ingen film med titeln du angav", "success")
        return redirect("/")

@app.route("/search/")
def page_not_found():
    ''' Runs when no search data is submitted '''
    flash("Ingen filmtitel angavs", "success")
    return redirect("/")

if __name__ == "__main__":
    app.secret_key='secret123'
    app.run(debug=True)
