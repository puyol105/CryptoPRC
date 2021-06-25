const express = require('express');
const router = express.Router();

const Categories = require('../controllers/categories');

// Checkar os controllers e models

router.get('/', function(req, res){
  Categories.listCategories()
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Categories ${e}`))
});

router.get('/:id', function(req, res){
  Categories.listCategory(req.params.id)
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Trading Category ${req.params.id} ${e}`))
});


module.exports = router;
