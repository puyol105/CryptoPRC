const express = require('express');
const router = express.Router();

const Tags = require('../controllers/tags');

// Checkar os controllers e models

router.get('/:tag', function(req, res){
  console.log('entrou', req.params.tag)
  Tags.listTags(req.params.tag)
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Categories ${e}`))
});

router.get('/:tag/:id', function(req, res){
  if(req.query.size && req.query.page){
    Tags.listTag(req.params.tag, req.params.id)
      .then( dados => {
        console.log('dados', dados.sort((a1,a2) => parseInt(a1.id) - parseInt(a2.id)))

        res.json({totalItems: dados.length , numberOfPages: Math.floor(dados.length/req.query.size), dados : dados.sort((a1,a2) => parseInt(a1.id) > parseInt(a2.id)).splice(req.query.page * req.query.size, req.query.size)})
        
      })
      .catch( e => res.status(500).send(`Error listing Tags ${e}`))
  }
});


module.exports = router;
