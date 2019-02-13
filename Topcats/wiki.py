from bs4 import BeautifulSoup
import requests


def get_wiki(film):
	"""
	Hämtar en wikipediasida och söker efter poster.
	"""

	search_result = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={film}+hastemplate:%22Infobox%20film%22&format=json').json()
	print(search_result)
	try:
		id = search_result['query']['search'][0]['pageid']
		title = search_result['query']['search'][0]['title']
	except IndexError:
		return None
	
	template_info = requests.get(f'https://en.wikipedia.org/w/api.php?action=parse&pageid={id}&section=0&prop=wikitext&format=json')

	resp = requests.get(f'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles={title}&rvsection=0&rvparse').json()

	# Utvinner html-kod ur data-requesten.
	page_one = next(iter(resp['query']['pages'].values()))
	revisions = page_one.get('revisions', [])
	html = next(iter(revisions[0].values()))

	# Letar upp img-taggen i html-koden.
	soup = BeautifulSoup(html, 'html.parser')
	poster = soup.find_all('img')

	print(html)
	for link in poster:
		return link.get('srcset')
