#/usr/bin/python3
from json import dump
from flask import Flask, request, jsonify, json, abort
from flask_cors import CORS
from waitress import serve
import pickle, re, threading, time, requests
from werkzeug.wrappers import response
import sys

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

#----------------------------------------------------------------

def list_to_query_string(id_list:list) -> str:
  if( len(id_list) == 1):
    return str(id_list[0])

#----------------------------------------------------------------

def filter_json( data_json, ids_list):
  result = []
  for data in data_json:
    if( str(data['id']) in ids_list ):
      result.append(data)
  return result

#----------------------------------------------------------------

def filter_json_2( data_json, ids_list):
  result = []
  #print('data_json', data_json, 'ids_list', ids_list)
  for data in data_json:
    #print(data['marketId'], ids_list)
    if( str(data['marketId']) in ids_list ):
      #print('data ---', data, '\n')
      result.append(data)
  print('tamanho', len(result))
  return result

#----------------------------------------------------------------

@app.route('/', methods = ['GET'])
def main_page():  
  return 'Rotas disponiveis /coinsPrice?id=1,2...'

#----------------------------------------------------------------

@app.route('/coinPrice', methods = ['GET'])
def coin_price(): 
  if (req_query_id := request.args.getlist("id")) is None:
    abort(404, description="No request query id provided")

  print('req_query_id', req_query_id, type(req_query_id))
  query_string = list_to_query_string(req_query_id)
  print('query_string', query_string)
  
  r_prices = requests.get('https://web-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + query_string)
  json_data = r_prices.json()

  if(json_data['status']['error_code'] == 0):
    data = json.dumps(json_data['data'])
    print('data', data)
  else:
    abort(404, description="Status error_code = 0")

  response = app.response_class(
    response = data,
    status = 200,
    mimetype = 'application/json'
  ) 
  return response

#----------------------------------------------------------------

@app.route('/exchangePrice', methods = ['GET'])
def exchange_price(): 
  if (req_query_id := request.args.getlist("id")) is None:
    abort(404, description="No request query id provided")
  
  #print('req_query_category', req_query_category, type(req_query_category))

  # query_string = list_to_query_string(req_query_id)
  # print('query_string', query_string)
  
  # r_prices_quotes = requests.get('https://web-api.coinmarketcap.com/v1/exchange/quotes/latest?id=' + query_string)
  # json_data_quotes = r_prices_quotes.json()

  r_prices_listings = requests.get('https://web-api.coinmarketcap.com/v1/exchange/listings/latest')
  json_data_listings = r_prices_listings.json()

  if(json_data_listings['status']['error_code'] == 0):
    data = filter_json(json_data_listings['data'], req_query_id)
    data = json.dumps(data)
  else:
    abort(404, description="Status error_code = 0")

  response = app.response_class(
    response = data,
    status = 200,
    mimetype = 'application/json'
  ) 
  return response

#----------------------------------------------------------------

# VER DEPOIS
@app.route('/marketPairPrice', methods = ['GET'])
def market_pair_price():
  
  if (req_query_id := request.args.getlist("slug")) is None:
    abort(404, description="No request query id provided")
  query_id_string = list_to_query_string(req_query_id)

  if (req_query_category := request.args.getlist("category")) is None:
    abort(404, description="No request query category provided")
  query_category_string = list_to_query_string(req_query_category)

  if (req_query_market := request.args.getlist("market")) is None:
    abort(404, description="No request query market provided")
  query_market_string = list_to_query_string(req_query_market)
  
  print('req_query_id', req_query_id, 'req_query_category', req_query_category, 'req_query_market', req_query_market)
  print('query_id_string', query_id_string, 'query_category_string', 'query_market_string', query_market_string)
  
  url = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug={query_id_string}&start=1&limit=700&category={query_category_string}&sort=cmc_rank_advanced'
  print('url', url)
  r_market_pair = requests.get(url)

  json_data_market_pair = r_market_pair.json()
  #print('status', json_data_market_pair['status']['error_code'])

  if(json_data_market_pair['status']['error_code'] == '0'):
    print('entrou')
    with open('mercados.json', 'w') as f:
      f.write(json.dumps(json_data_market_pair['data']['marketPairs'], indent=4, sort_keys=False))

    data = filter_json_2(json_data_market_pair['data']['marketPairs'], req_query_market[0].split(','))
    data = json.dumps(data)
  else:
    abort(404, description="Status error_code = 0")

  #data = json.dumps(json_data_market_pair)

  response = app.response_class(
    response = data,
    status = 200,
    mimetype = 'application/json'
  ) 
  return response
  
#----------------------------------------------------------------
 

def update_prices(): 
    threading.Timer(15, update_prices).start()
    print("Doing stuff...",  time.localtime())

if __name__ == "__main__":
  print('Server listening at port 9000')
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

