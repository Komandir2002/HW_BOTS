from bs4 import BeautifulSoup
import requests

URL = "https://multoigri.ru/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
}


def get_requests(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

def get_data_game(html):
    soup = BeautifulSoup(html,  "html.parser")
    items = soup.find_all("a", class_='games-list_game-link')
    game = []

    for item in items:
        game.append(
            {
                "image": URL + item.find("img").get("src"),
                "link": URL + item.find("link", itemprop='url').get("href"),

            }
        )
    return game


def scrapy_script_game():
    html = get_requests(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 3):
            html = get_requests(f"https://multoigri.ru/?page={page}")
            anime.extend(get_data_game(html.text))
        return anime
    else:
        raise Exception("Error in scrapy script function")