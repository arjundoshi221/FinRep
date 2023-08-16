import requests
from bs4 import BeautifulSoup


# TODO: Fix code to get all articles
def get_content(url: str) -> str:
    req = requests.get(url=url, headers={"User-Agent": "Chrome"})
    response = req.content
    html = BeautifulSoup(response, "html.parser")


def main():
    content = get_content("")
    print(content)


if __name__ == "__main__":
    main()
