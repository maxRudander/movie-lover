from bs4 import BeautifulSoup
import requests


def get_wiki(film):
	
	search_result = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={film}+hastemplate:%22Infobox%20film%22&format=json').json()
	
	id = search_result['query']['search'][0]['pageid']
	title = search_result['query']['search'][0]['title']
	
	template_info = requests.get(f'https://en.wikipedia.org/w/api.php?action=parse&pageid={id}&section=0&prop=wikitext&format=json')
	
	resp = requests.get(f'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles={title}&rvsection=0&rvparse').json()
	
	page_one = next(iter(resp['query']['pages'].values()))
	revisions = page_one.get('revisions', [])
	html = next(iter(revisions[0].values()))
	soup = BeautifulSoup(html, 'html.parser')
	poster = soup.find_all('img')

	print(html)
	for link in poster:
		return link.get('srcset')