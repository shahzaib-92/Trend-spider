import requests
import re
from bs4 import BeautifulSoup


def trendList():
    # get response from the url.
    url = "https://trends24.in/pakistan/"
    response = requests.get(url)

    # html parser
    soup = BeautifulSoup(response.text, "html.parser")

    # get the first matching element.
    tagElements = soup.find('div', attrs={'id': 'trend-list'})

    # get the list of tag elements.
    trend_cards = tagElements.findAll('div', attrs={'class': 'trend-card'})

    # get the text of ol element of the first trend_card.
    trendString: str = trend_cards[0].ol.get_text(separator=",")
    trendList = trendString.split(",")

    # filter the trend list and ignore all the texts which involve number of tweets
    p = re.compile("^[0-9].*K$")
    trendListWithoutTweets = [l for l in trendList if not p.match(l)]
    return trendListWithoutTweets
