FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install fitz
RUN pip3 install PyMuPDF


COPY . /app
EXPOSE 3000
CMD python ./app.py