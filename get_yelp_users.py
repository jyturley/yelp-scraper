#/usr/bin/python
from bs4 import BeautifulSoup
from urllib import urlopen
from urlparse import urlparse
import sys
import os

MAX_USERS = 1000

# Make sure the page is a yelp user page in the reviews tab.
def is_valid_yelp_user_review_page(html):
	if "Yelp" not in html.title.text:
		return False
	if "All Reviews" not in html.body.h3.text:
		return False

	return True

def is_valid_yelp_user_friends_page(html):
	return True if "Friends" in html.body.h3.text else False

def add_user_friends_to_list(user, users_to_visit):
	pass

def get_yelp_users(seen_users, users_to_visit):
	while users_to_visit:
		user = users_to_visit.pop()
		if user in seen_users:
			continue

		seen_users.add(user)
		if len(seen_users) > MAX_USERS:
			break;
		add_user_friends_to_list(user, users_to_visit)
	return seen_users

def main():
	assert(len(sys.argv) == 2)
	url = urlparse(sys.argv[1])
	seen_users = set()
	users_to_visit = []

	assert("www.yelp.com" in url.netloc)

	if "friends" not in url.path:
		query = url.query
		url = urlparse("http://www.yelp.com/user_details_friends?%s" % query)

	users_to_visit.append(url.query)
	get_yelp_users(seen_users, users_to_visit)

	# user_page_html = BeautifulSoup(urlopen(sys.argv[1]))
	# assert(is_valid_yelp_user_review_page(user_page_html))


if __name__ == "__main__":
	main()