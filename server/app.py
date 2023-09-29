from flask import Flask, render_template, request,redirect,flash,jsonify
from helpers import scraper

from pymongo import MongoClient
from pandas import DataFrame as df
from dotenv import load_dotenv
import os


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

mongo_uri=os.getenv('MONGO_URI')

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

             print(documents)
             return jsonify(documents)
             



if __name__ == '__main__':
   app.run(debug = True)