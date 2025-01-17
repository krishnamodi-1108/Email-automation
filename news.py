# API Key: 11b809c11cf347e2bf67c944404ce369
import requests
from pprint import pprint

class NewsFeed:
    """
    Class representing newsFeed containing News Title and Article Links
    """

    base_url = "https://newsapi.org/v2/everything"
    apiKey = "11b809c11cf347e2bf67c944404ce369"
    def __init__(self,interest,from_date,to_date,language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get_data(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''

        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = (f"{self.base_url}?"
               f"q={self.interest}&"
               f"from={self.from_date}&"
               f"to={self.to_date}&"
               f"language={self.language}&"
               f"apiKey={self.apiKey}")
        return url


if __name__ == "__main__":
    newsFeed = NewsFeed(interest='nasa',from_date='2025-01-15',to_date='2025-01-15',language='en')
    newsFeed = NewsFeed('nasa','2025-01-13','2025-01-13','en')
    print(newsFeed.get_data())