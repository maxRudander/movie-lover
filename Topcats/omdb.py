import requests


data_response = requests.get('http://www.omdbapi.com/?t=taken&apikey=f6aaec81')
if data_response.status_code is not 200:
	# Bad response / something went wrong
	print(data_response.status_code)
else:
	print(data_response.json()['Plot'])
