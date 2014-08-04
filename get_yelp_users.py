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

def add_user_friends_to_list(user_id_query, users_to_visit):
	html = BeautifulSoup(urlopen('http://www.yelp.com/user_details_friends?%s' % user_id_query))
	assert(is_valid_yelp_user_friends_page(html))
	# num_user_friends = html.find(class_='range-of-total')
	for friend in html.find_all('div', class_='friend_box'):
		try:
			friend_location = friend.find(class_='user-location').text
			if friend_location != "San Francisco, CA":
				continue
			friend_url = urlparse(friend.find(class_='photo-box pb-ss').a.get('href'))
			users_to_visit.append(friend_url.query)

		except:
			print "Something went wrong with %s" % friend

def get_yelp_users(seen_users, users_to_visit):
	while users_to_visit:
		user = users_to_visit.pop()
		if user in seen_users:
			continue

		seen_users.add(user)
		print "Getting friends for user: %s" % user
		print "# seen: %d\t# to visit: %d" % (len(seen_users), len(users_to_visit))
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
		print "moving to friends page"
		query = url.query
		url = urlparse("http://www.yelp.com/user_details_friends?%s" % query)

	users_to_visit.append(url.query)
	get_yelp_users(seen_users, users_to_visit)

if __name__ == "__main__":
	main()