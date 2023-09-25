import fitz
import glob
import pandas as pd
import uuid

TICKER = "HDFCBC"
PATHS = glob.glob("./HDFC news/*.pdf")

# List of dates of news articles
dates: list[str] = []

# Titles of news articles
titles: list[str] = []

times = []
source_tickers = []
sources = []
text_contents = []

for path in PATHS:
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()

    text: list[str] = text.split("\n")
    FLAG = False
    for idx, line in enumerate(text):
        if line[0].isdigit():
            date = ""
            tokens = line.split(" ")
            date, time, source_ticker, source = (
                tokens[0],
                tokens[4],
                tokens[5],
                tokens[6:],
            )
            dates.append(date)
            times.append(time)
            source_tickers.append(source_ticker)
            sources.append(" ".join(source))

            title = text[idx + 1]
            titles.append(title)
            FLAG = True
        if FLAG:
            break

    text_contents.append(" ".join(text[idx + 2 :]))

assert len(dates) == len(text_contents), "Shape error"
ids = [str(uuid.uuid4()) for _ in range(len(titles))]

# TODO: Update once we get all company tickera
ticker_lst = [TICKER for _ in range(len(titles))]

result: pd.DataFrame = pd.DataFrame(
    columns=[
        "ID",
        "Date",
        "Time",
        "Ticker",
        "Source_ticker",
        "Source",
        "Title",
        "Content",
    ]
)
result["ID"] = ids
result["Date"] = dates
result["Time"] = times
result["Ticker"] = ticker_lst
result["Source_ticker"] = source_tickers
result["Source"] = sources
result["Title"] = titles
result["Content"] = text_contents


# TODO: Convert this to `.parquet`
result.to_csv("Scraped_pdf_data.csv", index=False)
