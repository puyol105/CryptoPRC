var Exchange = module.exports;

const db = require('../config/db');

Exchange.listExchanges = async function () {
  try {
    const result = await db.query(
      `select ?exchange ?id ?name ?slug where { 
        ?exchange a :Exchange ; 
                    :id ?id ;
                    :name ?name ;
                    :slug ?slug .
      } limit 100`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};

Exchange.listExchange = async function (id) {
  try {
    const result = await db.query(
      `select ?exchange ?id ?name ?slug where { 
        ?exchange a :Exchange ; 
                    :id ?id ;
                    :name ?name ;
                    :slug ?slug .
        filter( ?id = ${id})
      } limit 100`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};