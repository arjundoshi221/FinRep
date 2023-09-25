import typing as t
import requests
from bs4 import BeautifulSoup


def get_content(url: str) -> str:
    req = requests.get(url=url, headers={"User-Agent": "Chrome"})
    response = req.content
    html = BeautifulSoup(response, "html.parser")
    content_div = html.find("div", attrs={"class": "content_wrapper"})
    p_tags = content_div.find_all("p")
    texts: t.List[str] = [p_tag.text.replace("\xa0", " ") for p_tag in p_tags]
    return " ".join(texts)


def main():
    content = get_content(
        "https://www.moneycontrol.com/news/business/stocks/gmr-airports-trades-down-despite-lower-q1-losses-nod-to-raise-rs-5000-cr-11193321.html"
    )
    print(content)


if __name__ == "__main__":
    main()
