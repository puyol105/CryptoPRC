var Tags = module.exports;

const db = require('../config/db');

// DEPOIS VER PORMENOR ID CATEGORY 

String.prototype.capitalize = function() {
  return this.charAt(0).toUpperCase() + this.slice(1);
}



Tags.listTags = async function () {
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


Tags.listTag = async function (tag, id) {
  console.log('tag', tag, 'id', id)
  let f_tag = tag.capitalize()
  console.log('f_tag', f_tag)
  try {
    const result = await db.query(
      `select * where {
        ?s :tem${f_tag} :${tag}_${id}.
          optional {
                  ?coin :name ?name .
                  ?coin :symbol ?symbol .
                  ?coin :slug ?slug .
                  ?coin :id ?id .
              }
          
      } limit 100 `);
    
    console.log('result category', result)
    return result;
  
  } catch (e) {
      throw e;
  }
};