# import scrapy
# from selenium import webdriver
# from scrapy import Selector
# import time 
# from bs4 import BeautifulSoup

# url = "https://www.rbc.ru/"
# driver = webdriver.Chrome(executable_path="C:\sel\chromedriver.exe")
# driver.get(url)
# SCROLL_PAUSE_TIME = 1
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# content = driver.page_source
# with open('webpage.html', 'w', encoding='utf-8') as f:
#     f.write(content)


# class QuotesSpider(scrapy.Spider):
#     name = "spider"
#     with open("C:\\Users\\User\\Desktop\\scrapy\\tutka\\tutka\\spiders\\webpage.html", "r") as f:
#         contents = f.read()
#     soup = BeautifulSoup(contents, 'lxml')

#     news = soup.span.news-feed__item__title.text

#     for new in news:
#         new.get().replace("\n", "").replace("\r", "")
        







                # text = response.css('p::text').getall()
        # txt = response.css('div.article-body').css('p')
        # for abz in txt:
        #     text.append(abz.css('strong::text').get())