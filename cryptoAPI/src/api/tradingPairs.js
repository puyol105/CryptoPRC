const express = require('express');
const router = express.Router();

const TradingPairs = require('../controllers/tradingPairs');

// Checkar os controllers e models

// router.get('/', function(req, res){
//   TradingPairs.listTradingPairs()
//     .then( dados => res.json(dados))
//     .catch( e => res.status(500).send(`Error listing Trading Pairs ${e}`))
// });

// router.get('/:id', function(req, res){
//   TradingPairs.listTradingPair(req.params.id)
//     .then( dados => res.json(dados))
//     .catch( e => res.status(500).send(`Error listing Trading Pair ${req.params.id} ${e}`))
// });

router.get('/:slug/type/:typePair', function(req, res){
  TradingPairs.getTradingPairCoin(req.params.slug,req.params.typePair)
    .then( dados => {
      res.json({totalItems: dados.length , numberOfPages: Math.floor(dados.length/req.query.size), dados : dados.sort((a1,a2) => parseInt(a1.id) > parseInt(a2.id)).splice(req.query.page * req.query.size, req.query.size)})    
    })
    .catch( e => res.status(500).send(`Error listing Trading Pair ${req.params.id} ${e}`))
});

router.get('/exchange/:slug/type/:typePair', function(req, res){
  TradingPairs.getTradingPairExchange(req.params.slug,req.params.typePair)
    .then( dados => {
      res.json({totalItems: dados.length , numberOfPages: Math.floor(dados.length/req.query.size), dados : dados.sort((a1,a2) => parseInt(a1.id) > parseInt(a2.id)).splice(req.query.page * req.query.size, req.query.size)})    
    })
    .catch( e => res.status(500).send(`Error listing Trading Pair ${req.params.id} ${e}`))
});
module.exports = router;
