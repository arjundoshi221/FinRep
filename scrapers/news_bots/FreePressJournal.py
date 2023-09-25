import requests
from bs4 import BeautifulSoup


def get_content(url: str) -> str:
    req = requests.get(url=url, headers={"User-Agent": "Chrome"})
    response = req.content
    html = BeautifulSoup(response, "html.parser")
    content_div = html.find("article", attrs={"id": "fjp-article"})
    p_tags = content_div.find_all("p")
    texts = [p_tag.text for p_tag in p_tags][:-1]
    return " ".join(texts)


def main():
    content = get_content(
        "https://www.freepressjournal.in/business/icici-bank-rewards-employees-with-over-5-lakh-shares-as-stock-options"
    )
    print(content)


if __name__ == "__main__":
    main()
