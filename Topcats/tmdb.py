import requests


def get_poster(film):

	data_response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=d4e35699aa07152cd0a3e572fff5f595&language=en-US&query={film}&page=1&include_adult=false').json()

	poster_url = 'https://image.tmdb.org/t/p/w500'+ data_response['results'][0]['poster_path']

	return(poster_url)