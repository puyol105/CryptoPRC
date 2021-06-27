#/usr/bin/python3
from json import dump
from flask import Flask, request, jsonify, json
from flask_cors import CORS
from waitress import serve
import pickle, re, threading, time, requests
from werkzeug.wrappers import response
#import sched

app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
#s = sched.scheduler(time.time, time.sleep)
global coins_id_list

def list_to_query_string(id_list:list) -> str:
  if( len(id_list) == 1):
    return str(id_list[0])

@app.route('/coinPrice', methods = ['GET'])
def coin_price(): 
  req_query_id = request.args.getlist("id")
  print('req_query_id', req_query_id, type(req_query_id))
  query_string = list_to_query_string(req_query_id)
  print('query_string', query_string)
  r_prices = requests.get('https://web-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + query_string)
  json_data = r_prices.json()

  if(json_data['status']['error_code'] == 0):
    data = json.dumps(json_data['data'])
    print('data', data)

  response = app.response_class(
    response = data,
    status = 200,
    mimetype = 'application/json'
  ) 
  return response
  

@app.route('/marketPairPrice', methods = ['GET'])
def market_pair_price():
  string = str(coins_id_list)
  params = re.sub(',', '-', string)
  print('params', params)
  return request.query_string
  return params

def update_prices(): 
    threading.Timer(15, update_prices).start()
    print("Doing stuff...",  time.localtime())

if __name__ == "__main__":
  print('aqui')
  serve(app, host="0.0.0.0", port=9000)
  app.run(debug=False)




# TRASH ------------
#main 
#coins_id_list = load_files()
  #s.enter(10, 1, update_prices, (s,))
  #s.run()
  
  #update_prices()
  

  # def update_prices(): 
  #   threading.Timer(15, update_prices).start()
  #   print("Doing stuff...",  time.localtime())
    # do your stuff
    #s.enter(10, 1, update_prices, (sc,))

#def load_files() -> list:
  # with open('coins_id_list.txt', 'rb') as f:
  #   temp = pickle.load(f)
  #   print(temp)
  #   return temp
