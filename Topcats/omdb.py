import requests
import omdb

""" 
API data-requests go to: http://www.omdbapi.com/?apikey=[db0723c0]&
API poster-requests go to: http://img.omdbapi.com/?apikey=[db0723c0]&
"""

data_response = requests.get('http://www.omdbapi.com/?t=taken&apikey=f6aaec81')
if data_response.status_code is not 200:
	# Bad response / something went wrong
	print(data_response.status_code)
for item in data_response.json():
	print(item)