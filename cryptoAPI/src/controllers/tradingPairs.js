var TradingPairs = module.exports;

const db = require('../config/db');

TradingPairs.getTradingPairCoin = async function (slug,pairType) {
  try {
    const result = await db.query(
      `select * where{
        ?tp a :TradingPair.
        ?tp a :${pairType}.
        ?tp :market_url ?marketurl.
        ?tp :market_id ?marketid.
        ?tp :éNegociado ?exchange.
        ?exchange :name ?exchangeName.
        ?tp :temParCoinSell ?coinSell.
        optional{
            ?coinSell :slug ?slugSell.
        }
        optional{
          ?coinSell :symbol ?symbolSell.
        }
        optional{
          ?coinSell :name ?nameSell.
        }
        optional{
            ?coinSell :id ?idSell.
        }
        ?coin :éParBuy|:éParSell ?tp.
        
        ?coin :slug ?slugBuy.
        ?coin :name ?nameBuy.
        filter(?slugBuy='${slug}')
    } `);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};


TradingPairs.getTradingPairExchange = async function (slug,pairType) {
  try {
    const result = await db.query(
      `select * where { 
        ?s a :Exchange ;
             :name ?name ;
             :slug ?slug ;
             :temTradingPair ?tp .
          ?tp a :${pairType} .
          ?tp :market_url ?marketurl.
          ?tp :market_id ?marketid.
          ?tp :temParCoinBuy ?coinbuy .
          ?coinbuy :name ?namebuy .
          ?coinbuy :slug ?slugbuy .
          ?coinbuy :symbol ?symbolbuy .
          ?tp :temParCoinSell ?coinsell .
          ?coinsell :name ?namesell .
          ?coinsell :slug ?slugsell .
          ?coinsell :symbol ?symbolsell .
             filter(?slug='${slug}')
      }`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};