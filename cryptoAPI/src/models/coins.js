//MODELS SÓ SÃO NECESSÁRIOS PARA o user que tem Schema Mongodb
const coins = require('../models/coins');

module.exports.list = (req, res) => {
  coins.list(req, res);
};