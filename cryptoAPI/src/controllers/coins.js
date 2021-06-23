const coins = require('../models/coins');


module.exports.list = (req, res, next) => {
  coins.list(req,res);
};