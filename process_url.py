import re
import urllib.request
from bs4 import BeautifulSoup

def extract_integers_from_line(string):
	"""
	Find all integers in an url text file and return them as a list.

	Args:
		string (str): Source string line.

	Returns:
		numbers (list[int]): List of integers found in the string line. 
	"""

	numbers = list()

	number = re.findall('[0-9]+', string)
	if len(number) != 0:
		numbers += [eval(i) for i in number]

	return numbers

def extract_integers(source, source_type='list'):
	"""
	Find all integers in an url text file and return them as a list.

	Args:
		source (str): Text source: list or url.
		source_type (str): Indicate source object type: 'list' or 'url'.

	Returns:
		numbers (list[int]): List of integers found in the text file. 
	"""

	numbers = list()

	if source_type == 'url': 
		for line in urllib.request.urlopen(source):
			numbers += extract_integers_from_line(line.decode('utf-8'))

	elif source_type == 'list':
		for line in source:
			numbers += extract_integers_from_line(line)

	return numbers

def extract_tags(url, tag):
	"""
	Extract all instances of a specified tag from html file.

	Args:
		url (string): Source URL.
		tag (string): Tag name.

	Returns:
		taglines (list[string]): List of strings containing the taglines.
	"""

	taglines = list()

	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve all of the anchor tags
	tag_list = soup(tag)
	for t in tag_list:
		taglines += t

	return taglines

def bla(url, count, position):
	"""
	"""

	cnt = 0
	while cnt < count:

		html = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html, 'html.parser')
		tag_list = soup('a')

		for index, item in enumerate(tag_list):
			if index == position-1:
				url = item.get('href', None)
				name = item.contents[0]
				break
			else:
				continue
		cnt += 1

	print('Last name:', name)


if __name__=='__main__':
	"""
	Example usage.
	"""

	file_sample = 'http://py4e-data.dr-chuck.net/regex_sum_42.txt'
	file_actual = 'http://py4e-data.dr-chuck.net/regex_sum_1629605.txt'

	n = extract_integers(file_actual, 'url')
	print(sum(n))


	url_sample = 'http://py4e-data.dr-chuck.net/comments_42.html'
	url_actual = 'http://py4e-data.dr-chuck.net/comments_1629607.html'

	m = extract_tags(url_actual, 'span')
	mn = extract_integers(m, 'list')
	print(sum(mn))


	problem_sample = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
	problem_actual = 'http://py4e-data.dr-chuck.net/known_by_Jessamy.html'

	o = bla(problem_sample, 4, 3)
	p = bla(problem_actual, 7, 18)