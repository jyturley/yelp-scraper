#/usr/bin/python
from bs4 import BeautifulSoup
from urllib import urlopen
from urlparse import urlparse
import sys
import os
import csv

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

def scrape_reviews_to_file(user_soup, file):
	fieldnames = ('user_id', 'funny', 'cool', 'useful', 'restaurant', 'review')
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	headers = dict((n,n) for n in fieldnames)
	writer.writerow(headers)

def add_user_friends_to_list(user_soup, users_to_visit):
	assert(is_valid_yelp_user_friends_page(user_soup))
	# num_user_friends = user_soup.find(class_='range-of-total')
	for friend in user_soup.find_all('div', class_='friend_box'):
		try:
			friend_location = friend.find(class_='user-location').text
			if friend_location != "San Francisco, CA":
				continue
			friend_url = urlparse(friend.find(class_='photo-box pb-ss').a.get('href'))
			users_to_visit.append(friend_url.query)

		except:
			print "Something went wrong with %s" % friend

def get_yelp_users(seen_users, users_to_visit, csv_file):
	f = open(csv_file, 'wb')
	while users_to_visit:
		user = users_to_visit.pop()
		if user in seen_users:
			continue

		seen_users.add(user)
		print "Getting friends for user: %s" % user
		print "# seen: %d\t# to visit: %d" % (len(seen_users), len(users_to_visit))
		if len(seen_users) > MAX_USERS:
			break;
		user_soup = BeautifulSoup(urlopen('http://www.yelp.com/user_details_friends?%s' % user))
		scrape_reviews_to_file(user_soup, f)
		add_user_friends_to_list(user_soup, users_to_visit)
	f.close()
	return seen_users

def main():
	assert(len(sys.argv) == 3)
	url = urlparse(sys.argv[1])
	csv = sys.argv[2]
	seen_users = set()
	users_to_visit = []

	assert("www.yelp.com" in url.netloc)

	if "friends" not in url.path:
		print "moving to friends page"
		query = url.query
		url = urlparse("http://www.yelp.com/user_details_friends?%s" % query)

	users_to_visit.append(url.query)
	get_yelp_users(seen_users, users_to_visit, csv)

if __name__ == "__main__":
	main()