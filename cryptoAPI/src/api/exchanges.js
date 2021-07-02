const express = require('express');
const router = express.Router();

const Exchanges = require('../controllers/exchanges');

// Checkar os controllers e models

router.get('/:slug', function(req, res){
  Exchanges.listExchange(req.params.slug)
    .then( dados => {
      res.json(dados)
    })
    .catch( e => res.status(500).send(`Error listing Exchange ${e}`))
});

router.get('/type/:type', function(req, res){
  if(req.query.size && req.query.page){
    Exchanges.listExchanges(req.params.type)
      .then( dados => {
        console.log('dados', dados.sort((a1,a2) => parseInt(a1.id) - parseInt(a2.id)))

        res.json({totalItems: dados.length , numberOfPages: Math.floor(dados.length/req.query.size), dados : dados.sort((a1,a2) => parseInt(a1.id) > parseInt(a2.id)).splice(req.query.page * req.query.size, req.query.size)})
        
      })
      .catch( e => res.status(500).send(`Error listing Exchange ${e}`))
    }
});

module.exports = router;
