var Tags = module.exports;

const db = require('../config/db');

// DEPOIS VER PORMENOR ID CATEGORY 

String.prototype.capitalize = function() {
  return this.charAt(0).toUpperCase() + this.slice(1);
}



Tags.listTags = async function (tag) {
  try {
    const result = await db.query(
    `select * where { 
      ?s a :${tag} ;
          :name ?name .
    }`);
    console.log('result', result)

    let r = result.map((e) => {
      return({
        link: e.s.split(`${tag.toLowerCase()}_`)[1],
        name: e.name
      })
    })
    return r;
  
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
        ?coin :tem${f_tag} :${tag}_${id}.
        :${tag}_${id} :name ?nametag.
        optional {
          ?coin :name ?name .
        }
        optional {
          ?coin :symbol ?symbol .
        }
        optional {
            ?coin :slug ?slug .
        }
        optional {
            ?coin :id ?id .
        }
          
      } `);
    
    console.log('result category', result)
    return result;
  
  } catch (e) {
      throw e;
  }
};