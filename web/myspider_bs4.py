import scrapy
from bs4 import BeautifulSoup

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        s = BeautifulSoup(response.text, 'html.parser')

        for link in s.find_all('a'):
            yield {'href': link.get('href'), 'text': link.get_text()}
