#/usr/bin/python3
import sys
import json
import re

unformated_category_list =''' Store of Value
                          Atomic Swaps
                          Centralized exchange
                          Collectibles & NFTs
                          Decentralized exchange
                          DeFi
                          Derivatives
                          Discount token
                          Privacy
                          Zero Knowledge Proofs
                          Interoperability
                          Masternodes
                          Oracles
                          Prediction Markets
                          Reputation
                          Scaling
                          State channels
                          Smart Contracts
                          Stablecoin
                          Stablecoin - Algorithmically-Stabilized
                          Stablecoin - Asset-Backed
                          Staking
                          DAO
                          Wallet
                          DApp
                          Substrate
                          Storage
                          Yield farming
                          AMM
                          Social Token
                          DEX
                          Rebase
                          Tokenized Stock
                          Fan token
                          Seigniorage
                          Polkadot Ecosystem
                          Yield Aggregator
                          Yearn Partnerships
                          LP Tokens
                          Binance Launchpool
                          Social Money
                          Coinbase Ventures Portfolio
                          Three Arrows Capital Portfolio
                          Polychain Capital Portfolio
                          Governance
                          Launchpad
                          Binance Launchpad
                          Binance Labs Portfolio
                          Avalanche Ecosystem
                          DeFi Index
                          Tourism
                          Options
                          Lending / Borrowing
                          Metaverse
                          Analytics
                          Polkastarter
                          DAO Maker
                          Blockchain Capital Portfolio
                          BoostVC Portfolio
                          CMS Holdings Portfolio
                          DeFiance Capital
                          Coinfund Portfolio
                          DCG Portfolio
                          DragonFly Capital Portfolio
                          Electric Capital Portfolio
                          Fabric Ventures Portfolio
                          Framework Ventures
                          Fenbushi Capital Portfolio
                          Galaxy Digital Portfolio
                          Hashkey Capital Portfolio
                          Kinetic Capital
                          Huobi Capital
                          LedgerPrime Portfolio
                          Alameda Research Portfolio
                          A16Z Portfolio
                          1Confirmation Portfolio
                          Winklevoss Capital
                          USV Portfolio
                          Placeholder Ventures Portfolio
                          Pantera Capital Portfolio
                          Multicoin Capital Portfolio
                          ParaFi capital
                          Paradigm XZY Screener
                          DuckSTARTER
                          Poolz Finance
                          Exnetwork Capital Portfolio
                          Trustswap Launchpad
                          PolkaFoundry Red Kite
                          Polygon Ecosystem
                          Bounce Launchpad
                          Bulletproofs
                          Mimble Wimble
                          Mixer & Coinjoin
                          RingCT
                          Escrow
                          Quantum-Resistant
                          Sharding
                          Timestamping
                          Layer 2
                          Rollups
                          Sidechain
                          [deprecated] Polychain Ventures portfolio
                          Leverage tokens
                          Data Availability Proofs
                          Draper Venture Network Portfolio
                          Cross Chain Aggregator Dex
                          Mobile Payments
                          Red Packets
                          Platform Token
                          Hacken Foundation
                          Superstarter
                          Chromia Ecosystem
                          Genpad
                          Doggone Doggerel '''



unformated_algorithm_list = ''' DAG
                                DPoS
                                Hybrid - PoW & PoS
                                PoS
                                PoW
                                Multiple algorithms
                                CryptoNight
                                Equihash
                                NeoScrypt
                                Quark
                                Scrypt
                                SHA-256
                                X11
                                X13
                                DBft
                                DPoR
                                Hybrid - dPoW & PoW
                                Hybrid - PoS & LPoS
                                Hybrid - PoS & PoD
                                Hybrid - PoS & PoP
                                Hybrid - PoS & PoW & PoT
                                Hybrid - PoW & nPoS
                                Hybrid - PoW & PoM & PoSII
                                LPoS
                                mFBA
                                PoA
                                POBh
                                PoC
                                PoI
                                PoP
                                PoSign
                                PoST
                                PoWT
                                Scrypt-adaptive-N
                                TPoS
                                1GB AES Pattern Search
                                Argon2
                                Blake
                                Blake (14r)
                                BLAKE256
                                Blake2b
                                Blake2S
                                C11
                                Cloverhash
                                CryptoNight-Lite
                                Cuckoo Cycle
                                Dagger
                                Dagger-Hashimoto
                                Equihash-BTG
                                Ethash
                                Groestl
                                Grostl-512
                                HMQ1725
                                IMesh
                                Keccak
                                Lyra2RE
                                Lyra2REv2
                                Lyra2Z
                                M7 POW
                                M7M
                                Mars
                                Myr-Groestl
                                NIST5
                                Ouroboros
                                PHI1612
                                POS 2.0
                                POS 3.0
                                Proof-of-Authority
                                Proof-of-BibleHash
                                QuBit
                                Scrypt-n
                                SHA-512
                                SHA-256D
                                SHA-3
                                Shabal-256
                                Skein
                                SkunkHash
                                SkunkHash v2 Raptor
                                Time Travel
                                Whirlpool
                                X11Evo
                                X11GOST
                                X13-BCD
                                X14
                                X15
                                X16R
                                x17
                                XEVAN
                                yescript
                                ZPool
                                Hybrid - PoW & DPoS
                                SIGMA
                                rPOS '''

unformated_plataform_list = ''' Ethereum
                                Asset Backed Coin
                                Polkadot
                                Binance Chain
                                Binance Smart Chain
                                Heco Ecosystem
                                Solana Ecosystem
                                Aave Tokens
                                Wrapped Tokens
                                Synthetics
                                ETH 2.0 Staking
                                Omni
                                Nxt
                                Counterparty
                                BitShares
                                Komodo
                                Ardor
                                NuBits
                                Horizon
                                Ubiq
                                XRP
                                Waves
                                Stellar
                                Burst
                                Ethereum Classic
                                NEM
                                Neo
                                VeChain
                                Qtum
                                Binance Coin
                                EOS
                                ICON
                                Cosmos
                                Bitcoin Cash
                                PIVX
                                Ontology
                                Nebulas
                                TRON
                                RSK Smart Bitcoin
                                IOST
                                Wanchain
                                HTMLCOIN
                                Neblio
                                Zeepin
                                TrueChain
                                Phore
                                INT Chain
                                v.systems
                                Teloscoin
                                VITE
                                GXChain
                                EthereumDark
                                Hive
                                Yocoin
                                Stratis
                                Horizen '''


unformated_industry_list = ''' Adult
                              Marketing
                              Asset management
                              Commodities
                              Cybersecurity
                              Art
                              Education
                              Energy
                              Events
                              Gambling
                              Hardware
                              Health
                              Marketplace
                              Media
                              Philanthropy
                              Medium of Exchange
                              Platform
                              Real Estate
                              Cosmos Ecosystem
                              Services
                              Sports
                              Logistics
                              VR/AR
                              Communications & Social Media
                              AI & Big Data
                              Enterprise solutions
                              Distributed Computing
                              Loyalty
                              Content Creation
                              Crowdfunding
                              Crowdsourcing
                              Data Provenance
                              E-commerce
                              Filesharing
                              Gaming
                              Entertainment
                              Identity
                              IoT
                              Jobs
                              Memes
                              Mobile
                              Music
                              Payments
                              Research
                              Sharing Economy
                              Video
                              Insurance
                              Fiat
                              Agriculture
                              Fashion
                              Food & Beverage
                              Government
                              Hospitality
                              Retail
                              Manufacturing
                              Maritime
                              Military
                              Transport
                              Luxury
                              Search Engine
                              Geospatial services
                              LelantusMW
                              Software '''


global category_list
category_list = [line.strip() for line in unformated_category_list.split('\n')]
#print('tags_list', tags_list)

global algorithm_list
algorithm_list = [line.strip() for line in unformated_algorithm_list.split('\n')]
#print('algorithm_list', algorithm_list)

global plataform_list 
plataform_list = [line.strip() for line in unformated_plataform_list.split('\n')]
#print('plataform_list', plataform_list)

global industry_list
industry_list = [line.strip() for line in unformated_industry_list.split('\n')]
#print('industry_list', industry_list)

def normalize_string(data:str):
  for c in ['\\', '/', '&', '[', ']', '(', ')']:
    data = data.replace(c, '')
  return data.replace(' ', '_')

def normalize_about(data:str):
  for c in ['\\', '\n', ';', '"', '\'']:
    data = data.replace(c, '')
  return data


coin = '''
###  http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#coin_bitcoin_BTC
:coin_bitcoin_BTC rdf:type owl:NamedIndividual ,
                           :Coin ;
                  x:temAlgorithm :algorithm_sha_256 ;
                  x:temCategory :category_store_of_value ;
                  x:temIndustry :industry_adult ;
                  x:temPlataform :plafaform_bitcoin_fakeplataform ;
                  :éParBuy :trading_pair_BTC-USDT_perpetual ,
                           :trading_pair_BTC-USDT_spot ;
                  x:about "Bitcoin is a decentralized cryptocurrency originally described in a 2008 whitepaper by a person, or group of people, using the alias Satoshi Nakamoto. It was launched soon after, in January 2009." ;
                  x:community "bitcointalk.org" ,
                             "https://reddit.com/r/bitcoin" ;
                  x:explorers "blockchain.coinmarketcap.com" ,
                             "blockchain.info" ;
                  x:id 1 ;
                  x:max_supply "21,000,000" ;
                  x:mineable "true"^^xsd:boolean ;
                  x:name "Bitcoin" ;
                  x:original_url "https://coinmarketcap.com/currencies/bitcoin/" ;
                  x:other_links "bitcoin.org" ,
                               "bitcoin1.org" ;
                  x:rank 1 ;
                  x:slug "bitcoin" ;
                  x:source_code "https://github.com/bitcoin/" ;
                  x:symbol "BTC" ;
                  x:website "https://bitcoin.org/" ;
                  x:whitepaper "https://bitcoin.org/bitcoin.pdf" .
'''

exchange = '''
###  http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#exchange_binance_spot
:exchange_binance_spot rdf:type owl:NamedIndividual ,
                                :Exchange ;
                       :temTradingPair :trading_pair_BTC-USDT_perpetual ,
                                       :trading_pair_BTC-USDT_spot ;
                       :about "Binance Futures Launches Monday & Tuesday Bounty! To welcome first-time users, Binance Futures will reward its users with a $5000 Bonus Jackpot every Monday and Tuesday of the week. Please check for more details here.'," ;
                       :chat "https://t.me/binanceexchange" ;
                       :fees "https://www.binance.com/en/fee/schedule" ;
                       :id 270 ;
                       :name "Binance" ;
                       :other_links "https://twitter.com/binance" ,
                                    "https:/insta.com/binance" ;
                       :slug "binance" ;
                       :type "derivatives" ,
                             "spot" ;
                       :website "https://www.binance.com/" .
'''

def gen_coin(elements):
  for coin in elements:
      data = ''
      data = f'''
###  http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#coin_{coin.get('id')}_{coin.get('symbol')}
:coin_{coin.get('id')}_{coin.get('symbol')} rdf:type owl:NamedIndividual ,
                           :Coin ;\n'''
      # about
      if(about := coin.get('about')):
        about = normalize_about(about)
        data += f'''\t\t:about "{about}" ;\n'''
      # base_currency_id
      if(coin.get('id')):
        data += f'''\t\t:id {coin['id']} ;\n'''
      # max_supply
      if(coin.get('max_supply')):
        data += f'''\t\t:max_supply "{coin['max_supply']}" ;\n'''

      # other/mineable
      if(other := coin.get('other')):
        for o in other:
          if(o == 'Mineable'):
            data += f'''\t\t:mineable "true"^^xsd:boolean ;\n'''
          else:
            data += f'''\t\t:mineable "false"^^xsd:boolean ;\n'''
          break;
      # consensus_algorithm
      if(consensus_algorithm := coin.get('consensus_algorithm')):
        for c in consensus_algorithm:
          c_formated = normalize_string(c)
          if(c in algorithm_list):
            data += f'''\t\t:temAlgorithm :algorithm_{c_formated} ;\n'''
      # property
      if(property := coin.get('property')):
        for p in property:
          p_formated = normalize_string(p)
          if(p in plataform_list):
            data += f'''\t\t:temPlataform :plataform_{p_formated} ;\n'''
          elif(p in category_list):
            data += f'''\t\t:temCategory :category_{p_formated} ;\n'''
          elif(p in industry_list):
            data += f'''\t\t:temIndustry :industry_{p_formated} ;\n'''

      #plataform
      if(platform := coin.get('platform')):
        for p in platform:
          p_formated = normalize_string(p)
          if(p in plataform_list):
            data += f'''\t\t:temPlataform :plataform_{p_formated} ;\n'''

      # community
      if(community := coin.get('community')):
          for index,c in (enumerate(coin.get('community'))):
            if(len(community) == 1):
              data += f'''\t\t:community "{c}" ;\n'''
            elif(index == 0):
              data += f'''\t\t:community "{c}" ,\n'''
            elif(index == len(community)-1):
              data += f'''\t\t\t "{c}" ;\n'''
            else:
              data += f'''\t\t\t "{c}" ,\n'''

      # explorers
      if(explorers := coin.get('explorers')):
          for index,e in enumerate(explorers):
            if(len(explorers) == 1):
              data += f'''\t\t:explorers "{e}" ;\n'''
            elif(index == 0):
              data += f'''\t\t:explorers "{e}" ,\n'''
            elif(index == len(explorers)-1):
              data += f'''\t\t\t "{e}" ;\n'''
            else:
              data += f'''\t\t\t "{e}" ,\n'''

      # other_links
      if(other_links := coin.get('other_links')):
          for index,o in (enumerate(coin.get('other_links'))):
            if(len(other_links) == 1):
              data += f'''\t\t:other_links "{o}" ;\n'''
            elif(index == 0):
              data += f'''\t\t:other_links "{o}" ,\n'''
            elif(index == len(other_links)-1):
              data += f'''\t\t\t "{o}" ;\n'''
            else:
              data += f'''\t\t\t "{o}" ,\n'''

      # name
      if(coin['name']):
        data += f'''\t\t:name "{coin['name']}" ;\n'''
      # original url
      if(coin['original_url']):
        data += f'''\t\t:original_url "{coin['original_url']}" ;\n'''
      # rank
      if(coin['rank']):
        data += f'''\t\t:rank {coin['rank']} ;\n'''
      # source_code
      if(coin.get('source_code')):
        data += f'''\t\t:source_code "{coin['source_code']}" ;\n'''
      # slug
      if(coin.get('slug')):
        data += f'''\t\t:slug "{coin['slug']}" ;\n'''
      # website
      if(coin.get('website')):
        data += f'''\t\t:website "{coin['website']}" ;\n'''
      # whitepaper
      if(coin.get('whitepaper')):
        data += f'''\t\t:whitepaper "{coin['whitepaper']}" ;\n'''
      # symbol
      if(coin.get('symbol')):
        data += f'''\t\t:symbol "{coin['symbol']}" .\n'''
      print(data)
      data = ""

def gen_exchange(elements):
  exchange_id_set = set()
  for exchange in elements:
    #print(f'''A processar ... :exchange_{exchange.get('id')}_{exchange.get('slug')}''')
    data = ''
    individual_name = f''':exchange_{exchange.get('id')}_{exchange.get('slug')}'''
    if( individual_name in exchange_id_set):
      #gera triplo
      data += f'''{individual_name} :type "{exchange.get('type')}" .\n'''
      if( exchange.get('pairs_futures')):
        data += f'''{individual_name} :type "futures" .\n'''
        #print(f'''A processar pairs futures ... :exchange_{exchange.get('id')}_{exchange.get('slug')}''')
    else:
      exchange_id_set.add(individual_name)

    data += f''' 
###  http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#exchange_{exchange.get('id')}_{exchange.get('slug')}
:exchange_{exchange.get('id')}_{exchange.get('slug')} rdf:type owl:NamedIndividual ,
                                :Exchange ;\n'''
    # about
    if(about := exchange.get('about')):
      about = normalize_about(about)
      data += f'''\t\t:about "{about}" ;\n'''
    # chat
    if(chat := exchange.get('chat')):
      data += f'''\t\t:chat "{chat}" ;\n'''
    # fees
    if(fees := exchange.get('fees')):
      data += f'''\t\t:fees "{fees}" ;\n'''
    # id
    if(id := exchange.get('id')):
      data += f'''\t\t:id {id} ;\n'''
    # other_links
      if(other_links := exchange.get('others')):
          for index,o in (enumerate(exchange.get('others'))):
            if(len(other_links) == 1):
              data += f'''\t\t:other_links "{o}" ;\n'''
            elif(index == 0):
              data += f'''\t\t:other_links "{o}" ,\n'''
            elif(index == len(other_links)-1):
              data += f'''\t\t\t "{o}" ;\n'''
            else:
              data += f'''\t\t\t "{o}" ,\n'''
    # slug
    if(slug := exchange.get('slug')):
      data += f'''\t\t:slug "{slug}" ;\n'''
    
    # website
    if(website := exchange.get('website')):
      data += f'''\t\t:website "{website}" ;\n'''
    # name
    if(name := exchange.get('name')):
      data += f'''\t\t:name "{name}" ;\n'''
    # type
    if(type := exchange.get('type')):
      data += f'''\t\t:type "{type}" .\n'''

    # type + trading_pairs
    for key in exchange.keys():
      #print('KEY', key)
      if( pair := re.match(r'pairs_(spot|perpetual|futures)', key)):
        market_pairs = exchange.get(pair.group(0))
        #print('trading pairs', trading_pairs)
        gen_trading_pairs(id, slug, pair.group(1), market_pairs)
        #print('pair', pair, 'pair group(1)', pair.group(1))

    #if(type := exchange.get(r'pairs_(spot|perpetual|futures)')):
    #  data += f'''\t\t:slug "{slug}" .\n'''
    
#       a='''
#                   :type "derivatives" ,
#                             "spot" ;
#                       :website "https://www.binance.com/" .    
# '''
    print(data)
    data = ""

def gen_trading_pairs(id, slug, type, market_pairs):
  for mp in market_pairs.get('marketPairs'):
    data = f''' 
###  http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#trading_pair_{mp.get('exchangeId')}_{mp.get('baseSymbol')}_{mp.get('quoteSymbol')}_{type}
:trading_pair_{mp.get('marketId')}_{mp.get('baseSymbol')}_{mp.get('quoteSymbol')}_{type} rdf:type owl:NamedIndividual ,
                                          :{type.capitalize()}Pair ,
                                          :TradingPair ;
                                 :temParCoinBuy :coin_{mp.get('baseCurrencyId')}_{mp.get('baseSymbol')};
                                 :temParCoinSell :coin_{mp.get('quoteCurrencyId')}_{mp.get('quoteSymbol')} ;
                                 :éNegociado :exchange_{id}_{slug} ;
                                 :market_id {mp.get('marketId')} ;
                                 :market_url "{mp.get('marketUrl')}" .    
'''
    print(data)
    data=''

def gen_category():
  for c in category_list:
    c_formated = normalize_string(c)
    data = f'''
###  http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#category_{c_formated}
:category_{c_formated} rdf:type owl:NamedIndividual ,
                                  :Category ;
                        :name "{c}" .'''
    print(data)
    data = ""

def gen_algorithm():
  for a in algorithm_list:
    a_formated = normalize_string(a)
    data = f'''
###  http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#algorithm_{a_formated}
:algorithm_{a_formated} rdf:type owl:NamedIndividual ,
                            :Algorithm ;
                  :name "{a}" .'''
    print(data)
    data = ""

def gen_plataform():
  for p in plataform_list:
    p_formated = normalize_string(p)
    data = f'''
###  http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#plafaform_{p_formated}
:plafaform_{p_formated} rdf:type owl:NamedIndividual ,
                                          :Plataform ;
                                 :name "{p}" .'''
    print(data)
    data = ""

def gen_industry():
  for i in industry_list:
    i_formated = normalize_string(i)
    data = f'''
###  http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#industry_{i_formated}
:industry_{i_formated} rdf:type owl:NamedIndividual ,
                         :Industry ;
                :name "{i}" .'''
    print(data)
    data = ""


def main():
  gen_category()
  gen_algorithm()
  gen_plataform()
  gen_industry()

  if(len(sys.argv) > 2):
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
      data = json.load(file)
      gen_coin(data.get('cryptomoedas'))
    with open(sys.argv[2], 'r', encoding='utf-8') as file:
     data = json.load(file)
     gen_exchange(data.get('exchanges'))

main()


