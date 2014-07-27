#/usr/bin/python
from bs4 import BeautifulSoup
from urllib import urlopen
import sys
import os
import argparse

def reviews_with_funny_vote(tag):
	try:
		return (tag['class'] is "review review-with-no-actions")
		# and (tag.contents[0])
	except:
		return False

def scrape_restaurant(restaurant_link):
	restaurant_html = BeautifulSoup(urlopen(restaurant_link))
	full_reviews = restaurant_html.find_all("div", class_="review review-with-no-actions")
	# full_reviews = restaurant_html.find_all(reviews_with_funny_vote)
	for full_review in full_reviews:
		review_text

def main():
    assert(len(sys.argv) == 1)

if __name__ == "__main__":
    main()
