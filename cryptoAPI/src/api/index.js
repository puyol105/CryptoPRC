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
router.get('/repos', function(_req, res) {
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

router.get('/teste', function(req, res){
  axios.get("http://localhost:9000/coinPrice?id=10,20,30,40")
    .then( dados => {

      //var keys = Object.keys(dados.data);
      //var values = Object.values(dados.data);

      let ids = Object.values(dados.data).map( item => {
        return({ symbol: item.symbol})
        //return item.symbol
      })

      console.log('ids', ids)
      // let data = {};
      // for (var j = 0; j < keys.length; j++) {
      //   let g = 1;
      //   data[j] = { name: keys[j], group: g++ };
      // }

      //console.log(data);
      //console.log('dados', dados.data)
      res.json(ids)
    })
    .catch( e => res.status(500).send(`Error in /teste route ${e}`))
});


//router.use('/coins', coins);

module.exports = router;
