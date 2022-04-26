from bs4 import BeautifulSoup
import requests

URL = 'https://afm.kg/aksessuary'

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

def get_requests(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_data(html):
    soup = BeautifulSoup(html,"html.parser")
    items = soup.find_all("div",class_='col-in')
    acsesuar = []


    for i in items:
        acsesuar.append(
            {
                "link":i.find("a", class_='link').get("href"),
                # "image": URL + i.find("div", class_="pic").find("img").get("src")
            }
        )
    return acsesuar


def scrapy_aksessuary():
    html = get_requests(URL)
    if html.status_code == 200:
        acsesuar = []
        html = get_requests(f"https://afm.kg/aksessuary")
        acsesuar.extend(get_data(html.text))
        return acsesuar
    else:
        raise Exception("Error in scrapy script function")