import unittest
from bs4 import BeautifulSoup
from urllib import urlopen
from get_yelp_users import is_valid_yelp_user_review_page
from get_yelp_users import is_valid_yelp_user_friends_page

class GetYelpUsersTest(unittest.TestCase):
	def test_is_valid_yelp_user_review_page(self):
		self.assertFalse(is_valid_yelp_user_review_page(get_html('http://www.google.com')))
		self.assertFalse(is_valid_yelp_user_review_page(get_html('http://www.yelp.com/user_details?userid=1yQUQL1fqOMJzw-cy5mbJg')))
		self.assertTrue(is_valid_yelp_user_review_page(get_html('http://www.yelp.com/user_details_reviews_self?userid=1yQUQL1fqOMJzw-cy5mbJg')))

	def test_is_valid_yelp_user_friends_page(self):
		self.assertTrue(is_valid_yelp_user_friends_page(get_html('http://www.yelp.com/user_details_friends?userid=1yQUQL1fqOMJzw-cy5mbJg')))
		self.assertTrue(is_valid_yelp_user_friends_page(get_html('http://www.yelp.com/user_details_friends?userid=hHEqhNgpBhj9AoHJeW-PnQ')))
		self.assertFalse(is_valid_yelp_user_friends_page(get_html('http://www.yelp.com/user_details_reviews_self?userid=1yQUQL1fqOMJzw-cy5mbJg')))

def get_html(url):
	return BeautifulSoup(urlopen(url))

if __name__ == '__main__':
	unittest.main()
