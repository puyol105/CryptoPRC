var TradingPairs = module.exports;

const db = require('../config/db');

TradingPairs.listTradingPairs = async function () {
  try {
    const result = await db.query(
      `select ?trading_pair ?market_url where { 
        ?trading_pair a :TradingPair ;
                      :market_url ?market_url .
      } limit 100`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};

TradingPairs.listTradingPair = async function (id) {
  try {
    const result = await db.query(
      `select ?trading_pair ?market_url ?market_id where { 
        ?trading_pair a :TradingPair ;
                      :market_url ?market_url ;
                :market_id ?market_id .
        filter( ?market_id = ${id})
      } limit 100`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};