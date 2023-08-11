# https://pub.towardsai.net/real-time-stock-news-sentiment-analyzer-54eaa91c5634

from bs4 import BeautifulSoup
import pandas as pd
import requests


def get_tickers(url: str) -> pd.DataFrame:
    req = requests.get(url=url, headers={"User-Agent": "Chrome"})
    response = req.content
    html = BeautifulSoup(response, "html.parser")
    ticks_table = html.find(class_="page")

    ticks = list()
    stocks = list()
    for name_box in ticks_table.find_all("a", href=True):
        stocks.append(name_box.text.strip())
        ticks.append(name_box["href"].split("-")[-1].strip())
    d = {"stock": stocks, "tick": ticks}
    df = pd.DataFrame(data=d)
    return df


TICKERS_URL = "https://www.tickertape.in/stocks"
tickers_df = get_tickers(url=TICKERS_URL)


def get_data(url: str) -> list:
    req = requests.get(url=url, headers={"User-Agent": "Chrome"})
    response = req.content
    html = BeautifulSoup(response, "html.parser")
    news_div = html.find(name="div", attrs={"data-section-tag": "olderNews"})
    news_info = []
    links = news_div.find_all(name="a", attrs={"class": "news-card"})
    for a in links:
        title = a.find("h5", attrs={"class": "news-title"}).find("p").text
        publisher = a.find("p", attrs={"class": "news-info"}).find_all("span")[-1].text

        news_info.append((title, publisher))

    return news_info


news = list()
for _, ticker in enumerate(tickers_df["tick"]):
    url = (
        "https://www.tickertape.in/stocks/"
        + ticker
        + "/news?checklist=basic&ref=stock-overview_overview-sections&type=news"
    )
    headlines = get_data(url)
    news.append(headlines)

print(news)
