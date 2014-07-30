#/usr/bin/python
from bs4 import BeautifulSoup
from urllib import urlopen
import sys
import os

# Make sure the page is a yelp user page in the reviews tab.
def is_valid_user_page(html):
	if "Yelp" not in html.title.text:
		return False

	if "All Reviews" not in html.body.h3.text:
		return False

	return True

def main():
	assert(len(sys.argv) == 2)
	user_page_html = BeautifulSoup(urlopen(sys.argv[1]))
	assert(is_valid_user_page(user_page_html))

if __name__ == "__main__":
	main()