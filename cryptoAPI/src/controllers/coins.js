var Coins = module.exports;

const db = require('../config/db');

                  //? o models não devia retornar e e api fazer o res.json?
// module.exports = async (req,res) => {
//   const result = await db.query(`select ?name ?about where { 
//         ?coin a :Coin .
//         ?coin :name ?name .
//         ?coin :about ?about .
//     } limit 100`);
//   res.json(result);
// };

Coins.listCoins = async function () {
  try {
    const result = await db.query(`
    select ?name ?symbol ?slug ?id where { 
              ?coin a :Coin .
              ?coin :name ?name .
              ?coin :symbol ?symbol .
              ?coin :slug ?slug .
              ?coin :id ?id .
          }
        `);
    return result;
  
  } catch (e) {
      throw e;
  }
};

Coins.listCoin2 = async function (id) {
  try {
    const result = await db.query(`select ?name ?about where { 
          ?coin a :Coin .
          ?coin :name ?name .
          ?coin :about ?about .
          ?coin :id ?id .
          filter( ?id = ${id})
      } limit 100`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};

Coins.getCoin = async function (slug) {
  try {
    const result = await db.query(`
select  ?id ?rank (group_concat(distinct ?explorers; separator = ';') as ?explorers) (group_concat(distinct ?community; separator = ';') as ?community) ?mineable ?max_supply ?about ?name ?original_url (group_concat(distinct ?other_links; separator = ';') as ?other_links) ?slug ?source_code ?symbol ?website ?whitepaper (group_concat(distinct ?nomeal; separator = ';') as ?nomeal) (group_concat(distinct ?nomecat; separator = ';') as ?nomecat) (group_concat(distinct ?nomeind; separator = ';') as ?nomeind) (group_concat(distinct ?nomeplat; separator = ';') as ?nomeplat) where{
    ?coin a :Coin.
    ?coin :id ?id.
    optional{
        ?coin :explorers ?explorers.
    }
    optional{
        ?coin :community ?community.
    }
    optional{
        ?coin :rank ?rank.
    }
    optional{
        ?coin :mineable ?mineable.
    }
    optional{
        ?coin :max_supply ?max_supply.
    }
    optional{
        ?coin :name ?name.
    }
    optional{
        ?coin :original_url ?original_url.
    }
    optional{
        ?coin :other_links ?other_links.
    }
    optional{
        ?coin :slug ?slug.
    }
    optional{
        ?coin :source_code ?source_code.
    }
    optional{
        ?coin :symbol ?symbol.
    }
    optional{
        ?coin :website ?website.
    }
    optional{
        ?coin :whitepaper ?whitepaper.
    }
    optional{
        ?coin :temAlgorithm ?temAlgorithm.
        ?temAlgorithm :name ?nomeal.
    }
    optional{
        ?coin :temCategory ?temCategory.
        ?temCategory :name ?nomecat.
    }
    optional{
        ?coin :temIndustry ?temIndustry.
        ?temIndustry :name ?nomeind.
    }
    optional{
        ?coin :temPlataform ?temPlataform.
        ?temPlataform :name ?nomeplat.
    }
    optional{
        ?coin :about ?about.
    }
    filter(?slug='${slug}')
} group by ?id ?rank ?mineable ?max_supply ?name ?about ?original_url ?slug ?source_code ?symbol ?website ?whitepaper

    `);
    //console.log(result)
    return result;
  } 
  catch (e) {
      throw e;
  }
};

// PREFIX : <http://www.semanticweb.org/ricardoleal24/ontologies/cryptomoedas#>
// select  ?max_supply ?id ?mineable ?name ?original_url  ?rank ?slug ?source_code ?symbol  where{
//     ?coin a :Coin.
//     ?coin :id ?id.
//     optional{
//         ?coin :name ?name.
//     }
//     optional{    	
//         ?coin :max_supply ?max_supply.
//     }
//     optional{
//         ?coin :mineable ?mineable.
//     }
//     optional{
//         ?coin :original_url ?original_url.
//     }
//     optional{
//         ?coin :rank ?rank.
//     }
//     optional{
//         ?coin :slug ?slug.
//     }
//     optional{
//         ?coin :source_code ?source_code.
//     }
//     optional{
//         ?coin :symbol ?symbol.
//     }
    
// }