import pandas as pd
import uuid
from pathlib import Path
import typing as t
from datetime import datetime

DIR_PATH = Path("./portfolio/PNB/news/")
TICKER = "PNB"
TXT_FILES_PATHS: t.List[Path] = [file_path for file_path in DIR_PATH.glob("*.txt")]

# NOTE: Add path of file here
# path = TXT_FILES_PATHS[6]

# Declaring all
date_format = "%b %d %Y"
dates: t.List[str] = []
times: t.List[str] = []
titles: t.List[str] = []
source_tickers: t.List[str] = []
sources: t.List[str] = []
text_contents: t.List[t.List[str]] = []

for path in TXT_FILES_PATHS:
    with open(path, "r") as f_in:
        file_contents: t.List[str] = f_in.read().split("\n")
        content = []

    for idx, line in enumerate(file_contents):
        # Get info for source of news
        if idx == 0:
            sources.append(line[6 : line.index("(") - 1])
            source_tickers.append(line[line.index("(") + 1 : line.index(")")])

        # Get date of news
        elif idx == 1:
            date: str = line[6 : 6 + 11].strip()
            date = str(datetime.strptime(date, date_format).date())
            time = line[-8:]
            dates.append(date)
            times.append(time)

        elif idx == 2:
            titles.append(line)

        else:
            content.append(line)
    text_contents.append(" ".join(content))

ids = [str(uuid.uuid4()) for _ in range(len(titles))]
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
# TODO: Update once we get all company tickera
ticker_lst = [TICKER for _ in range(len(titles))]
result["ID"] = ids
result["Date"] = dates
result["Time"] = times
result["Ticker"] = ticker_lst
result["Source_ticker"] = source_tickers
result["Source"] = sources
result["Title"] = titles
result["Content"] = text_contents

# TODO: Convert this to `.parquet`
result.to_csv("Scraped_txt_data.csv", index=False)
