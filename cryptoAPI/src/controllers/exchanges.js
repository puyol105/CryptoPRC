var Exchange = module.exports;

const db = require('../config/db');

Exchange.listExchange = async function (slug) {
  try {
    const result = await db.query(
      `select * where { 
        ?s a :Exchange ;
             :slug ?slug .
          filter(?slug = '${slug}')
             
          optional {
          ?s :name ?name ;
             :id ?id ;
             :about ?about ;
             :fees ?fees ;
             :chat ?chat ;
             :other_links ?links .
             }
      }`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};

Exchange.listExchanges = async function (type) {
  try {
    const result = await db.query(
      `select * where { 
        ?s a :Exchange ;
             :type ?type ;
             :name ?name ;
             :id ?id ;
             :slug ?slug .
          filter(?type = '${type}')
      }`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};