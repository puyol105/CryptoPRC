const express = require('express');
const router = express.Router();

const Coins = require('../controllers/coins');

// Checkar os controllers e models

function aux(ids_string){
  axios.get("http://localhost:9000/coinPrice?id=1")
      .then((response) => doSomething(response.data))
      .catch((err) => {
        console.error("ops! ocorreu um erro" + err);
     });
} 

router.get('/', function(req, res){
  if(req.query.size && req.query.page){
    Coins.listCoins()
      .then( dados => {
        console.log('dados', dados.sort((a1,a2) => parseInt(a1.id) - parseInt(a2.id)))
        res.json({totalItems: dados.length , numberOfPages: Math.floor(dados.length/req.query.size), dados : dados.sort((a1,a2) => parseInt(a1.id) > parseInt(a2.id)).splice(req.query.page * req.query.size, req.query.size)})
        
      })
      .catch( e => res.status(500).send(`Error listing Coins ${e}`))
  }
})

// router.get('/', async function (req, res) {
//   Coins.listCoins()
//     .then( dados => {
//       let exists = await axios.get('http://localhost:3000/user/test1');
//     });

// router.get('/', async function(req, res){
//   Coins.listCoins()
//     .then( dados => {
//       ids = dados.map( c => {
//         return c.id
//       }).toString()
//       ids_string = ids
//       console.log('ids_string', ids)

//       let res = await axios.get('http://localhost:3000/user/test1');

//       res.json(dados)

//     })
//     .catch( e => res.status(500).send(`Error listing Coins ${e}`))
// });

router.get('/:id', function(req, res){
  Coins.listCoin(req.params.id)
    .then( dados => res.json(dados))
    .catch( e => res.status(500).send(`Error listing Coins ${req.params.id} ${e}`))
});


module.exports = router;
