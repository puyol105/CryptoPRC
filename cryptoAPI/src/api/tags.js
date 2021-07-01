const express = require('express');
const router = express.Router();

const Tags = require('../controllers/tags');

// Checkar os controllers e models

router.get('/', function(req, res){
  Tags.listTags()
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Categories ${e}`))
});

router.get('/:tag/:id', function(req, res){
  Tags.listTag(req.params.tag, req.params.id)
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Trading Category ${req.params.id} ${e}`))
});


module.exports = router;
