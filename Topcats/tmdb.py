import requests


def get_trailer(film):
	"""
	Letar efter en trailer från tmdb och returnerar denna ifall en hittas.
	"""

	data_response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=d4e35699aa07152cd0a3e572fff5f595&language=en-US&query={film}&page=1&include_adult=false').json()
	id = data_response['results'][0]['id']
	
	video_response = requests.get(f'http://api.themoviedb.org/3/movie/{id}/videos?api_key=d4e35699aa07152cd0a3e572fff5f595').json()
	
	try:
		video_src = 'https://www.youtube.com/embed/' + video_response['results'][0]['key']
		good_stuff = video_src

		return good_stuff
	except IndexError:
   		return None
