import scrapy
from scrapy import Selector
import re

urls = ["https://news.google.com", 
        "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru",
        "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFppYm5vU0FuSjFLQUFQAQ?hl=ru&gl=RU&ceid=RU%3Aru"
    ]


class QuotesSpider(scrapy.Spider):

    name = "googlespid"
    ids = 0

    def start_requests(self):

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        for i in response.css('div.NiLAwe'):
            text = i.css('a.DY5T1d::text').get()
            source = i.css('a.wEwyrc::text').get()
            date = re.findall('datetime="[-:TZ0-9"]+', response.css('time').get())
            href = urls[0] + response.css('a.VDXfz::attr(href)').get().replace('.','')

            self.ids +=1 
            yield {
                'id': self.ids,
                'name': text,
                'date': date,
                'source': source,
                'href': href
            }