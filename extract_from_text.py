import re
import urllib.request

def extract_integers(filename):
	"""
	Find all integers in an url file and return them as a list.

	Args:
		filename (str): URL to the text file.

	Returns:
		numbers (list[int]): List of integers found in the text file. 
	"""

	numbers = list()

	for line in urllib.request.urlopen(filename):
		number = re.findall('[0-9]+', line.decode('utf-8'))
		if len(number) != 0:
			numbers += [eval(i) for i in number]

	return numbers

if __name__=='__main__':
	"""
	Example usage.
	"""

	test_file = 'http://py4e-data.dr-chuck.net/regex_sum_42.txt'
	file = 'http://py4e-data.dr-chuck.net/regex_sum_1629605.txt'

	n = extract_numbers(file)
	print(sum(n))

