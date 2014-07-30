import unittest
from bs4 import BeautifulSoup
from urllib import urlopen
from get_yelp_users import is_valid_user_page


class GetYelpUsersTest(unittest.TestCase):
	def test_is_valid_user_page(self):
		self.assertFalse(is_valid_user_page(get_html('http://www.google.com')))
		self.assertFalse(is_valid_user_page(get_html('http://www.yelp.com/user_details?userid=1yQUQL1fqOMJzw-cy5mbJg')))
		self.assertTrue(is_valid_user_page(get_html('http://www.yelp.com/user_details_reviews_self?userid=1yQUQL1fqOMJzw-cy5mbJg')))

def get_html(url):
	return BeautifulSoup(urlopen(url))

if __name__ == '__main__':
	unittest.main()
