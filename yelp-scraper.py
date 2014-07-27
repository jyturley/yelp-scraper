#/usr/bin/python
from bs4 import BeautifulSoup
from urllib import urlopen
import sys
import os
import argparse

def scrape_restaurant(restaurant_link):
	restaurant_html = BeautifulSoup(urlopen(restaurant_link))

def main():
    assert(len(sys.argv) == 1)

if __name__ == "__main__":
    main()
