var TradingPairs = module.exports;

const db = require('../config/db');

TradingPairs.getTradingPair = async function (slug,type) {
  try {
    const result = await db.query(
      `select * where{
        ?tp a :TradingPair.
        ?tp a :${type}.
        ?tp :market_url ?url.
        ?tp :market_id ?id.
        ?tp :éNegociado ?exchange.
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
        filter(?slugBuy='${slug}')
    } `);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};