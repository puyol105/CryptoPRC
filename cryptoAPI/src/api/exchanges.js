const express = require('express');
const router = express.Router();

const Exchanges = require('../controllers/exchanges');

// Checkar os controllers e models

router.get('/', function(req, res){
  Exchanges.listExchanges()
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Exchange ${e}`))
});

router.get('/:id', function(req, res){
  Exchanges.listExchange(req.params.id)
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Exchange ${req.params.id} ${e}`))
});


module.exports = router;
