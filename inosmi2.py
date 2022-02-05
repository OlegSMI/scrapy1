import requests
from bs4 import BeautifulSoup

def get_news_of_page(url, params):
    all_news = []
    req = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(req.text, "lxml")
    all_news_html = soup.find_all("article", class_="rubric-list__article")
    for item in all_news_html:
        try:
            href = "https://inosmi.ru/" + item.find("a").get("href")
            headline = item.select(".rubric-list__article-title_small a")[0].text.strip().replace(u'\xa0', ' ')
            text = item.select(".rubric-list__article-announce a")[0].text.strip().replace(u'\xa0', ' ')
            count_views = item.select(".article-stats__item_views")[0].text.strip()
            count_comments = item.select(".article-stats__item_comments")[0].text.strip()
            date = item.find("time", class_="rubric-list__article-date").get("datetime").replace('+03:00', '')
            news = {"Дата": date, "Заголовок": headline, "Текст": text, "Количество просмотров": count_views,
                    "Количество комментариев": count_comments, "Ссылка": href}
            all_news.append(news)
        except: continue
    return all_news


url = "https://inosmi.ru/ajax/archive/get.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
params = {"date_from": "", "date_to": "", "id": "", "date": ""}

count_page = 30
all_news = []
for i in range(count_page):
    news_of_page = get_news_of_page(url, params)

    """В иносми на каждой странице выводится по 14 новостей. 
    И при загрузке новой страницы с новостями в параметрах передается номер последней новости на 
    предыдущей странице, ее дата и время в соответствующем формате.
    Блок ниже и сделан для этой пагинации """
    href = news_of_page[-1]["Ссылка"]
    id_for_params = href[href.rfind('/') + 1: href.rfind('.html')]
    date_for_params = news_of_page[-1]["Дата"].replace('-', '').replace(':', '')
    params = dict.fromkeys(["date_to", "date"], date_for_params)
    params["id"] = id_for_params

    for item in news_of_page:
        all_news.append(item)

k = 0
for i in all_news:
    k+=1
    print(f'{k} - {i}')
