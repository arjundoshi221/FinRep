import requests
from bs4 import BeautifulSoup


def get_content(url: str) -> str:
    req = requests.get(url=url, headers={"User-Agent": "Chrome"})
    response = req.content
    html = BeautifulSoup(response, "html.parser")
    content_div = html.find("div", attrs={"class": "contentbody"})
    p_tags = content_div.find_all("p")
    texts = [p_tag.text for p_tag in p_tags][:-1]
    return " ".join(texts)


def main():
    content = get_content(
        "https://www.thehindubusinessline.com/markets/mcap-of-seven-of-top-10-firms-falls-by-74603-cr-hdfc-bank-biggest-laggard/article67190149.ece"
    )
    print(content)


if __name__ == "__main__":
    main()
