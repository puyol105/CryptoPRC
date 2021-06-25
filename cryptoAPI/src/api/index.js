const express = require('express');
const axios = require('axios');

//const coins = require('./coins');

const router = express.Router();

router.get('/', (req, res) => {
  res.json({
    message: 'Bem vindo ao nosso sistema de esquemas em pirame das cryptos. One love. To da fucking mooooooon!'
  });
});

//Lista Repositórios
router.get('/repos', function(req, res) {
  axios.get("http://localhost:7200/rest/repositories")
    .then(dados =>{
        console.dir(dados.data)
        repos = dados.data.map(r => {
          return({
            id: r.id,
            tit: r.title,
            uri: r.uri
          })
        })
        res.json(repos)
    })
    .catch(erro => res.render('error', {error: erro}));
});

//router.use('/coins', coins);

module.exports = router;
