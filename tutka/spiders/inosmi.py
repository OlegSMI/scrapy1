import scrapy
from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
import re


url = "https://inosmi.ru"

rubrics = [
    'https://inosmi.ru/military/',
    'https://inosmi.ru/politic/'
]

class InosmiSpider(scrapy.Spider):

    name = "inospider"
    schet = 0
    ids = 0

    def start_requests(self):

        for ss in rubrics:
            yield scrapy.Request(url=ss, callback=self.parse)

    
    def parse(self, response): 

        for i in response.css('article.rubric-list__article'):
            yield scrapy.Request(url = url + i.css('a::attr(href)').get(), callback=self.parse_datas)

        next_page = response.css('a.input-button::attr(href)').get()
        if next_page is not None and self.schet != 10:
            print(self.schet)
            next_page = response.urljoin(next_page)
            self.schet += 1   
            yield scrapy.Request(next_page, callback=self.parse)


    def parse_datas(self, response):

        name = response.css('h1::text').get()
        source_photo = response.css('footer.article-header__image-copyright').css('a::text').get()
        date = response.css('time.article-header__date::text').get()
        text = response.css('div.article-body').css('p').getall()
        views_count = response.css('span.article-stats__item_views::text').get()
        com_count = response.css('a.article-stats__item_comments::text').get()
        href = str(response)[5:].replace('>', '')
        text = ''
        for i in response.css('div.article-body_indented').css('p::text'):
            abz = i.get().replace(u'\xa0', ' ')
            text += abz
    
        self.ids +=1 
        yield{
            'id': self.ids,
            'article': name,
            'source_photo': source_photo,
            'date': date,
            'views_count': views_count,
            'comment_count': com_count,
            'href': href,
            'text': text
        }