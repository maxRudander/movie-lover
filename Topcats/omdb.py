import requests


def get_movie(film):
	data_response = requests.get(f'http://www.omdbapi.com/?t={film}&apikey=f6aaec81')
	if data_response.status_code is not 200:
		# Bad response / something went wrong
		print(data_response.status_code)
	else:
		return data_response.json()
