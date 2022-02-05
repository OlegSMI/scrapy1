import scrapy
from scrapy import Selector
import re

url = "https://www.rbc.ru/"

AJAX_HOST = "https://www.rbc.ru/v10/ajax/get-news-by-filters/?offset="

class QuotesSpider(scrapy.Spider):
    name = "normspider"
    ids = 0

    def start_requests(self):

        # yield scrapy.Request(url=url, callback=self.parse)
        for offset in range(0, 1020, 20):
            if offset == 1020:
                yield scrapy.Request(url=url, callback=self.parse)
            yield scrapy.Request(url=(AJAX_HOST + str(offset)), callback=self.parse_ajax)


    def parse(self, response):
        
        news = response.css("a.news-feed__item::attr(href)").getall()
        for new in news:
            yield scrapy.Request(new, callback=self.parse_page)


    def parse_ajax(self, response):

        for addr in re.findall('https://w[./a-z0-9]+', response.text):
            yield scrapy.Request(addr, callback=self.parse_page)


    def parse_page(self, response):
        
        author = response.css("span.article__authors__author__name::text").get()
        if author is None:
            author = 'Non author'

        name = response.css("h1.js-slide-title::text").get()
        if name is None:
            name = 'Non name'

        date = response.css("span.article__header__date::text").get()
        if date is None:
            date = 'Non date'

        text = ''
        for i in response.css('div.article__text_free').css('p::text'):
            abz = i.get().replace(u'\n', ' ')
            text += abz

        self.ids +=1 
        yield {
            'id': self.ids,
            'article': name,
            'author': author,
            'date': date,
            'text': text
        }