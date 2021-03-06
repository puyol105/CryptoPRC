#/usr/bin/python3

#from requests import *
import requests
from requests.api import request
from bs4 import BeautifulSoup
import sys
import re
import json
import time
import pickle
import pprint
#import filters_names

global coins_id_list
coins_id_list = []

global marketpairs_id_list
marketpairs_id_list = []


def extract_coins(coins:dict) -> dict:
  coins_list = []
  n_pag = 0;
  rank = 1
  
  while n_pag < 1:
    if(n_pag == 0):
      page_url = 'https://coinmarketcap.com/'
    else:
      page_url = f'https://coinmarketcap.com/?page={n_pag}'
    
    n_pag+=1
      
    time.sleep(5)
    page_request = requests.get(page_url)
    rank, coins_list = extract_coin(page_request.text, coins_list, rank)
  
  coins['cryptomoedas'] = coins_list
  return coins

# --------------------------------------------------------------------------------------------------

def extract_coin(page:str, coins:list, rank:int) -> list:
  soup = BeautifulSoup(page, 'html.parser')
  #print('html', soup.prettify())

  n_iter = 0
  for tr in soup.find('tbody'):
    
    coin = {}
    coin['rank'] = rank
    rank +=1
    
    if n_iter < 10:
      n_iter += 1
      coin_url_soup = tr.find('a', class_='cmc-link').get('href')
      coin_url = coin_url_soup

      coin_url = f'https://coinmarketcap.com{coin_url}'

      r = requests.get(coin_url)
      time.sleep(2.5)

      soup = BeautifulSoup(r.text, 'html.parser')
      #print('html', soup.prettify())

      if(nome_soup := soup.find('h2', class_='sc-1q9q90x-0 iYFMbU h1___3QSYG')):
        nome = nome_soup.get_text("|", strip=True).split('|')[0]
        coin['name'] = nome

      if(symbol := nome_soup.find('small', class_='nameSymbol___1arQV')):
        coin['symbol'] = symbol.string

      if( data_json := soup.find('script', { "id" : "__NEXT_DATA__"}).string):
        if(coin_id := re.search(r'info":{"id":(\d*?),', data_json)):
          coin['id'] = coin_id.group(1)
          coins_id_list.append(int(coin_id.group(1)))

      if(original_url := soup.find('meta', attrs={'property' : 'og:url'}).get('content')):
        coin['original_url'] = original_url
        id = (original_url.split('/currencies/')[1])[:-1]
        coin['slug'] = id
      
      if(max_supply := soup.find(class_='maxSupplyValue___1nBaS')):
        coin['max_supply'] = max_supply.string

      if(about_soup := soup.find('div', class_='sc-2qtjgt-0 eApVPN')):
        about = ''
        for p_about in about_soup.find_all('p'):
          #print('p_about: ', p_about, '\np_about get_text()', p_about.get_text(), 'type p_about get_text()', type(p_about.get_text()))
          about = about + p_about.get_text()
        coin['about'] = about

      if(website_soup := soup.find('a', class_ = 'button___2MvNi' )):
        coin['website'] = website_soup.get('href')

      if(table := soup.find_all('div', class_='sc-16r8icm-0 hTLJPb')):
        for t in table:
          table_header = t.find('h4', class_='sc-1q9q90x-0 jdftjI')

          # Coins Links
          if(table_header.string == f'{nome} Links'):
            table_links = t.find_all('div', class_='sc-16r8icm-0 elzRBB')
            links = [] 
            explorers = []
            community = []

            for tl in table_links:
              
              table_links_header = tl.find('h6', class_='modalHeading___3qgbp').string
            
              fields = tl.find_all('a')
              for f in fields:
                
                if(table_links_header == 'Links'):
                  
                  # Source code
                  if(f.get_text() == 'Source code'):
                    coin['source_code'] = f.get('href')
                  
                  # Whitepaper
                  elif(f.get_text() == 'Whitepaper'):
                    coin['whitepaper'] = f.get('href')
                  
                  # Chat
                  elif(f.get_text() == 'Chat'):
                    links.append(f.get('href'))
                  
                  # Other
                  else:
                    links.append(f.get_text())

                if(table_links_header == 'Explorers'):
                  explorers.append(f.get_text())
                # Community
                if(table_links_header == 'Community'):
                  # Reddit
                  if(f.get_text() == 'Reddit'):
                    community.append(f.get('href'))
                  # Twitter
                  elif(f.get_text() == 'Twitter'):
                    community.append(f.get('href'))
                  # Other
                  else:
                    community.append(f.get_text())
                # Other
                #else:
                  #print('tem Outro', f.get_text())
                  #print('field_string: ', f.get_text(), 'field: ', f.prettify() , '\n')

              coin['other_links'] = links
              coin['explorers'] = explorers
              coin['community'] = community

          # Coins Tags
          if(table_header.string == f'{nome} Tags'):

            table_tags = t.find_all('div', class_='sc-16r8icm-0 dvhdfY')
            for tg in table_tags:
              table_tags_header = tg.find('h6', class_='modalHeading___3qgbp').string

              fields = tg.find_all('div', class_='tagBadge___3p_Pk')
              prop_list = []
              
              for f in fields:
                prop_list.append(f.string)

              header = re.sub(r'\s|-', '_', table_tags_header).lower()
              coin[header] = prop_list
          # Other            
          #else:
            #print('outro\n table_header: ', table_header.string, '\n')

      coins.append(coin)

  return (rank, coins)

# --------------------------------------------------------------------------------------------------

def extract_exchanges(exchanges:dict) -> dict:

  exchanges_list = []
  base_url = 'https://coinmarketcap.com'

                # vazia ?? a spot
  #exchange_types = ['', 'derivatives', 'dex', 'lending']
  exchange_types = [ 'dex', 'lending']

  for exchange_type in exchange_types:
    r = requests.get('https://coinmarketcap.com/rankings/exchanges/' + exchange_type)

    time.sleep(1)
    
    exchanges_soup = BeautifulSoup(r.text, 'html.parser')

    exchanges_soup = exchanges_soup.find('tbody')
    
    n_iter = 0
    for exchange_soup_tr in exchanges_soup.find_all('tr'):
     # print('n_iter', n_iter, 'exchange_soup_tr', exchange_soup_tr)
      n_iter +=1

      if(n_iter > 30):

        exchange = {}

        if( exchange_href := exchange_soup_tr.find('a', class_='cmc-link').get('href')):
          slug = exchange_href.split('/')[2]
        
        exchange['slug'] = slug

        exchange_request = requests.get(base_url + exchange_href)
        
        time.sleep(1)

        exchange_soup = BeautifulSoup(exchange_request.text, 'html.parser')
        
        if(nome_soup := exchange_soup.find('h2', class_='sc-1q9q90x-0 sc-1xafy60-3 aeSJT')):
          exchange['name'] = nome_soup.string

        if(exchange_type == ''):
          exchange_type = 'spot'
        
        exchange['type'] = exchange_type
        
        if( data_json := exchange_soup.find('script', { "id" : "__NEXT_DATA__"}).string):
          if(id := re.search(r'info":{"id":(\d*?),', data_json)):
            exchange['id'] = id.group(1)
        
        if(about_soup := exchange_soup.find('div', class_='sc-2qtjgt-0 eApVPN')):
          about = ''
          for p_about in about_soup.find_all('p'):
            #print('p_about: ', p_about, '\np_about get_text()', p_about.get_text(), 'type p_about get_text()', type(p_about.get_text()))
            about = about + p_about.get_text()
          
          if( span_about_soup := about_soup.find('span')):
            about = about + span_about_soup.get_text()
          
          exchange['about'] = about

        if(exchange_info_ul := exchange_soup.find('ul', class_ = 'uxo8xk-0 jlcQeb cmc-details-panel-links')):
          others = []
          
          if(exchange_inf_ul := exchange_info_ul.find_all('a')):
            for exchange_info_a in exchange_inf_ul:

              info = exchange_info_a.string
              
              if(info == 'Chat'):
                exchange['chat'] = exchange_info_a.get('href')
              
              elif(info == 'Fees'):
                exchange['fees'] = exchange_info_a.get('href')
              
              else:
                others.append(exchange_info_a.get('href'))
              
            
            exchange['website'] = others[0]
            others.pop(0)
            exchange['others'] = others
          

          # Exchange Market Pairs

          # if(exchange_type == 'derivatives'):
          #   #perpetual
          #   market_pairs_perpetual_request = requests.get(f'https://api.coinmarketcap.com/data-api/v3/exchange/market-pairs/latest?slug={slug}&category=perpetual&start=1&limit=500')
          #   market_pairs_perpetual_json = json.loads(market_pairs_perpetual_request.text) #.json?
          #   if (market_pairs_perpetual_json['status']['error_message'] == 'SUCCESS'):
          #     exchange['pairs_perpetual'] = dict(market_pairs_perpetual_json.get('data'))
          #   time.sleep(2.5)

          #   #futures
          #   market_pairs_futures_request = requests.get(f'https://api.coinmarketcap.com/data-api/v3/exchange/market-pairs/latest?slug={slug}&category=futures&start=1&limit=500')
          #   market_pairs_futures_json = json.loads(market_pairs_futures_request.text)
          #   if (market_pairs_futures_json['status']['error_message'] == 'SUCCESS'):
          #     exchange['pairs_futures'] = dict(market_pairs_futures_json.get('data'))
          #   time.sleep(2.5)

          # else:
          #   #spot
          #   market_pairs_spot_request = requests.get(f'https://api.coinmarketcap.com/data-api/v3/exchange/market-pairs/latest?slug={slug}&category=spot&start=1&limit=500')
          #   market_pairs_spot_json = json.loads(market_pairs_spot_request.text)
            
          #   if (market_pairs_spot_json['status']['error_message'] == 'SUCCESS'):
          #     exchange['pairs_spot'] = dict(market_pairs_spot_json.get('data'))
          #   time.sleep(2.5)
          
          #time.sleep(5.0)
        exchanges_list.append(exchange)
  
  exchanges['exchanges'] = exchanges_list
  return exchanges

# --------------------------------------------------------------------------------------------------
# Pedir uma p??gina de moeda para teste
def coin_page(coin_id):
  coin_page = f'https://coinmarketcap.com/currencies/{coin_id}'
  coin_request = requests.get(coin_page)
  soup = BeautifulSoup(coin_request.text, 'html.parser')
  print('html', soup.prettify())

  #   <script id="__NEXT_DATA__" type="application/json">
  if( data_json := soup.find('script', { "id" : "__NEXT_DATA__"}).string):
    if(coin_extracted_id := re.search(r'info":{"id":(\d*?),', data_json)):
      print('coin_extracted_id', coin_extracted_id.group(1))

# --------------------------------------------------------------------------------------------------
# Pedir uma p??gina exchange para teste
def exchange_page():
  exchange_page = f'https://coinmarketcap.com/exchanges/venus/'
  exchange_request = requests.get(exchange_page)
  soup = BeautifulSoup(exchange_request.text, 'html.parser')
  print('html', soup.prettify())

# --------------------------------------------------------------------------------------------------

def main():
  if(len(sys.argv) > 1):
    coin_page(sys.argv[1])

  try:
    with open('coins.json', 'w') as file: 
      coins = {}
      out_coins = extract_coins(coins)
      file.write(json.dumps(out_coins, indent=4, sort_keys=False))
      #print(json.dumps(out_coins, indent=4, sort_keys=True))
  except Exception as error:
    print('error processing coins', error)

  #pp = pprint.PrettyPrinter(indent=4)
  #pp.pprint(out_coins)
  
  try:
    with open('exchanges.json', 'w') as file: 
      exchanges = {}
      out_exchanges = extract_exchanges(exchanges)
      file.write(json.dumps(out_exchanges, indent=4, sort_keys=False))
      #print(json.dumps(out_exchanges, indent=4, sort_keys=False))
  except Exception as error:
    print('error processing exchanges', error)

  #pp = pprint.PrettyPrinter(indent=4)
  #pp.pprint(out_exchanges)


main()