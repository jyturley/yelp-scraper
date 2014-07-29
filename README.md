# Scraping Yelp

Have you ever wondered what the funniest Yelp review ever written was? Or the coolest? Unfortunately, the Yelp API currently has no way of finding this out. I decided I find out myself.

## Requirements

Python 2.7 is required. Install dependencies with:

    pip install -r requirements.txt

## Step 1: Crawl Yelp to get a list of users.

There are two ways to go about finding the funniest yelp review. Scraping reviews from the restaurant-page or scraping reviews from the user-page. Thankfully, each user-page already allows users to sort reviews by their funny score, so I'll go with approach two.

The first step in this approach is to gather a large list of users (Ideally, every user on yelp that has written a review, but for the purposes of this experiment, I'll limit myself to all users in the Bay Area). This can be done by a simple BFS web crawl of any yelp-user page and the pages of his or her friend:

    python get_yelp_users

