#/usr/bin/python3
from flask import Flask, request
from waitress import serve
import pickle, re, threading, time, requests, json
#import sched

app = Flask(__name__)
#s = sched.scheduler(time.time, time.sleep)
global coins_id_list

@app.route('/coinPrice', methods = ['GET'])
def coin_price():
  params = re.sub('\[|\]|\s', '', str(coins_id_list))
  print('params', type(params), params)
  r = requests.get('https://web-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id='+params)
  
  print(json.dumps(r.text, indent=4, sort_keys=False))
  #return request.query_string
  return params

@app.route('/marketPairPrice', methods = ['GET'])
def market_pair_price():
  string = str(coins_id_list)
  params = re.sub(',', '-', string)
  print('params', params)
  return request.query_string
  return params

def update_prices(): 
    threading.Timer(50.0, update_prices).start()
    print("Doing stuff...",  time.localtime())
    # do your stuff
    #s.enter(10, 1, update_prices, (sc,))

def load_files() -> list:
  with open('coins_id_list.txt', 'rb') as f:
    temp = pickle.load(f)
    print(temp)
    return temp

if __name__ == "__main__":
  coins_id_list = load_files()
  #s.enter(10, 1, update_prices, (s,))
  #s.run()
  
  update_prices()
  print('aqui')
  app.run(debug=True)
  serve(app, host="0.0.0.0", port=8080)
