const coins = require('../models/coins');

module.exports.list = (req, res) => {
  coins.list(req, res);
};
