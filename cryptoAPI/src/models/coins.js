const db = require('../config/db');

module.exports.list = async (req, res) => {
  const result = await db.query(`select ?name ?about where { 
        ?coin a :Coin .
        ?coin :name ?name .
        ?coin :about ?about .
    } limit 100`);
  res.json(result);
};
