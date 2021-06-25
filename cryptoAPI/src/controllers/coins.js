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
    const result = await db.query(`select ?name ?symbol ?slug where { 
          ?coin a :Coin .
          ?coin :name ?name .
          ?coin :symbol ?symbol .
          ?coin :slug ?slug .
          
      } limit 100`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};

Coins.listCoin = async function (id) {
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