from bs4 import BeautifulSoup as BS
import requests
from django.views.decorators.csrf import csrf_exempt

URL = 'https://kanobu.ru'

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0",
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="knb-cell")
    games_new = []

    for item in items:
        games_new.append(
            {
                "title_name": item.find("div", class_="BaseElementCard_body__dFPiu").get_text(),
                "description": item.find("div", class_="BaseElementCard_genres__VF5Dy").get_text(),
                "title_url": URL + item.find("a").get("href"),
                "image": item.find("figure", class_='knb-card--base knb-card--mask-static').find('img').get('src'),
            }
        )
    return games_new

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        all_games = []
        for page in range(0, 1):
            html = get_html(f'https://kanobu.ru/games/popular/', params=page)
            all_games.extend(get_data(html.text))
            return all_games

    else:
        raise Exception('Ошибка в парсере')

