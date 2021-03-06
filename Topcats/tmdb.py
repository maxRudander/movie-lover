import requests


def get_trailer(film):
	"""
	Letar efter en trailer från tmdb och returnerar denna ifall en hittas.
	"""

	try:
		data_response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=d4e35699aa07152cd0a3e572fff5f595&language=en-US&query={film}&page=1&include_adult=false').json()
		id = data_response['results'][0]['id']
		video_response = requests.get(f'http://api.themoviedb.org/3/movie/{id}/videos?api_key=d4e35699aa07152cd0a3e572fff5f595').json()
		return 'https://www.youtube.com/embed/' + video_response['results'][0]['key']
	except IndexError:
   		return None
