import scrapy
from scrapy import Selector
import re

url_host = "https://news.google.com"

url_world = url_host + "/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru"
url_russia = url_host + "/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFppYm5vU0FuSjFLQUFQAQ?hl=ru&gl=RU&ceid=RU%3Aru"

urls = []

urls.append(url_host)
urls.append(url_world)
urls.append(url_russia)

class QuotesSpider(scrapy.Spider):

    name = "googlespider"

    def start_requests(self):

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response): 

        fin = response.css('a.wEwyrc::text').getall()
        

        yield response.css('a.wEwyrc::text').getall()


    #     for href in response.css('a.VDXfz::attr(href)').getall():
    #         yield scrapy.Request(url=url_host + href.replace('.',''), callback=self.get_page)


    # def get_page(self, response):

    #     addr = re.findall('https://[-./a-z0-9_]+', response.css('body').get())[-2]
    #     yield scrapy.Request(url=addr, callback=self.get_page2)


    # def get_page2(self, response):

    #     name = response.css('h1::text').get()
    #     name2 = response.css('h2::text').get()
    #     text = response.css('p::text').getall()
    #     text2 = response.css('div.article__text::text').getall()
    #     yield {
    #             'name_article': name,
    #             'name_article2': name2,
    #             'date_article': 'date',
    #             'sssss': str(response)
    #             # 'text_article': text,
    #             # 'text_article2': text2
    #             # 'author_article':
    #         }
        
        
        
        
        # a.wEwyrc