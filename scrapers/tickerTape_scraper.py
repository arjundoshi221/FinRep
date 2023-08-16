# https://pub.towardsai.net/real-time-stock-news-sentiment-analyzer-54eaa91c5634

# TODO: Correct mappings for stock tickers
# TODO: First latest news for every stock, follow on "data-section-tag"

from bs4 import BeautifulSoup
import pandas as pd
import requests


def get_tickers(url: str) -> pd.DataFrame:
    """
    Returns stock owner name + ticker

    Args:
        url (str): url

    Returns:
        pd.DataFrame: data
    """
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
        href = a.get("href")
        news_info.append((title, publisher, href))

    return news_info


news = list()
tickers_df = tickers_df[tickers_df["tick"] == "ICBK"]
print(tickers_df.shape)
for _, ticker in enumerate(tickers_df["tick"]):
    print(f"$$$$$$$ {ticker}")
    url = (
        "https://www.tickertape.in/stocks/"
        + ticker
        + "/news?checklist=basic&ref=stock-overview_overview-sections&type=news"
    )
    headlines = get_data(url)
    news.append(headlines)

print(news)
