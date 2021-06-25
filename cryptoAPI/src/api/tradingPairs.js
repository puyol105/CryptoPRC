const express = require('express');
const router = express.Router();

const TradingPairs = require('../controllers/tradingPairs');

// Checkar os controllers e models

router.get('/', function(req, res){
  TradingPairs.listTradingPairs()
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Trading Pairs ${e}`))
});

router.get('/:id', function(req, res){
  TradingPairs.listTradingPair(req.params.id)
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Trading Pair ${req.params.id} ${e}`))
});


module.exports = router;
