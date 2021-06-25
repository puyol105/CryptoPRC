var Categories = module.exports;

const db = require('../config/db');

// DEPOIS VER PORMENOR ID CATEGORY 

Categories.listCategories = async function () {
  try {
    const result = await db.query(
      `select ?category ?nome where { 
        ?category a :Category ;
                      :name ?nome .
      } limit 100`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};

Categories.listCategory = async function (id) {
  try {
    const result = await db.query(
      `select ?category ?nome where { 
        ?category a :Category ;
                      :name ?nome .
      filter(?nome = "Avalanche Ecosystem")
    } limit 100`);
    
    return result;
  
  } catch (e) {
      throw e;
  }
};