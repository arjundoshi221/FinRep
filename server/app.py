from flask import Flask, render_template, request,redirect,flash,jsonify
from helpers import scraper

from pymongo import MongoClient
from pandas import DataFrame as df
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

mongo_uri=os.getenv('MONGO_URI')

#mongo_uri="mongodb+srv://jairajani1709:jaijaijai1709@cluster0.xpthex2.mongodb.net/FinRep?retryWrites=true&w=majority&appName=AtlasApp"
#SECRET_KEY='FINREP12345'
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

client = MongoClient(mongo_uri)

# Access your MongoDB database
db = client.get_database("FinRep")
collection=db.get_collection('News')


def validate(df):
       title=df.Title[0]
       print(title)
       query={'Title':title}
     
       if collection.count_documents(query,limit=1)!=0:
             return False
       else:
             return True
    
       


@app.route('/')
def main_page():
       
   return render_template('main.html')
	
@app.route('/fail')
def fail():
       return 'fail'

@app.route('/success')
def success():
       return 'success'

@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      data=request.form
      f = request.files['file']
      
      #f = request.files['file']
      
    
      result = scraper.scrape_data(f,data)
      

      if validate(result):
     
         documents = result.to_dict(orient='records')
      
         collection.insert_many(documents)
         
         flash('Uploaded')
         #f.save(f.filename)
         return jsonify({'status':"success"})
      else:
             flash('Error')
             return jsonify({'status':'File already uploaded'})
      

@app.route('/view',methods=['GET'])
def data():
       if request.method=='GET':
             documents=list(collection.find({}))
             for doc in documents:
                    doc['_id'] = str(doc['_id'])

             #print(documents)
             return jsonify(documents)

@app.route('/viewdates',methods=['POST'])
def viewdates():
     if request.method=='POST':
           data=request.form
           date1=data.get('date1','')
           start_date = datetime.datetime.strptime(date1, '%m/%d/%Y')
           date2=data.get('date2','')
           end_date = datetime.datetime.strptime(date2, '%m/%d/%Y')
           name=data.get('name','')
           if name=='':
                 query = {
              'Date': {
                     '$gte': start_date,
                     '$lte': end_date,
                     
              }
             }
           else:

              query = {
                     'Date': {
                            '$gte': start_date,
                            '$lte': end_date,
                            
                     },
                     'Analyst_Name':name}
           result = list(collection.find(query))
           for doc in result:
                    doc['_id'] = str(doc['_id'])

           return jsonify(result)

             



if __name__ == '__main__':
   app.run(port=int(5000),debug = True)