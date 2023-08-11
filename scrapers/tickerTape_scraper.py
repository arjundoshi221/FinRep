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
tickers_df = get_tickers(url=TICKERS_URL).head(1)
# print(tickers_df.head(2))


def get_data(url: str) -> list:
    req = requests.get(url=url, headers={"User-Agent": "Chrome"})
    response = req.content
    html = BeautifulSoup(response, "html.parser")
    news_table = html.find(name="div", attrs={"data-section-tag": "olderNews"})
    news = []
    for name_box in news_table.find_all("p", class_="shave-root"):
        news.append(name_box.text.strip())

    return news


news = list()
for _, ticker in enumerate(tickers_df["tick"]):
    url = (
        "https://www.tickertape.in/stocks/"
        + ticker
        + "/news?checklist=basic&ref=stock-overview_overview-sections&type=news"
    )
    print(url)
    headlines = get_data(url)
    news.append(headlines)

print(news)
