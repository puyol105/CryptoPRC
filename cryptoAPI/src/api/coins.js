const express = require('express');
const router = express.Router();

const Coins = require('../controllers/coins');

// Checkar os controllers e models

router.get('/', function(req, res){
  Coins.listCoins()
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Coins ${e}`))
});

router.get('/:id', function(req, res){
  Coins.listCoin(req.params.id)
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Coins ${req.params.id} ${e}`))
});


module.exports = router;
