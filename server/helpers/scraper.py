import glob
import pandas as pd
import uuid
import fitz
import datetime


def scrape_data(file,data):
    print(type(file))
    TICKER = "HDFCBC"
     
    ''' analystName=form_data['analystName']
    timeInputted=form_data['timeInputted']
    analystSource=form_data['source']
    dateOfUpload=form_data['dateOfUpload']
    notes=form_data['notes']
    companyName=form_data['companyName']
    print(analystName,timeInputted,source,dateOfUpload,notes,companyName) '''

    analystName = [data.get('analystName', '')]
    timeInputted = data.get('timeInputted', '')
    analystSource = data.get('source', '')
    dateOfUploadStr = data.get('dateOfUpload', '')
    dateOfUpload = datetime.datetime.strptime(dateOfUploadStr, '%m/%d/%Y')
    notes = data.get('notes', '')
    companyName = data.get('companyName', '')

      # Print the values stored in the variables
    print("analystName:", analystName)
    print("timeInputted:", timeInputted)
    print("source:", analystSource)
    print("dateOfUpload:", dateOfUpload)
    print("notes:", notes)
    print("companyName:", companyName) 
  

    
    # List of dates of news articles
    dates: list[str] = []

    # Titles of news articles
    titles: list[str] = []

    times = []
    source_tickers = []
    sources = []
    text_contents = []

   
    doc = fitz.open(stream=file.read(), filetype="pdf")
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

    # TODO: Update once we get all company tickers
    ticker_lst = [TICKER for _ in range(len(titles))]

    result: pd.DataFrame = pd.DataFrame(
        columns=[
            'Analyst_Name',
            'Analyst_DateofUpload',
            'Analyst_TimeofUpload',
            'Analyst_Notes',
            'Analyst_Source',
            'Analyst_CompanyName',
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

    datesObj=datetime.datetime.strptime(dates[0], '%m/%d/%Y')
    result['Analyst_Name']=analystName
    result['Analyst_DateofUpload']=dateOfUpload
    result['Analyst_TimeofUpload']=timeInputted
    result['Analyst_Notes']=notes
    result['Analyst_Source']=analystSource
    result['Analyst_CompanyName']=companyName
    result["ID"] = ids
    result["Date"] = datesObj
    result["Time"] = times
    result["Ticker"] = ticker_lst
    result["Source_ticker"] = source_tickers
    result["Source"] = sources
    result["Title"] = titles
    result["Content"] = text_contents

    print(result)
    # TODO: Convert this to `.parquet`
    return result