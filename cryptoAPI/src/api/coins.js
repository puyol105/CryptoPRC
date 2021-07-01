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

function normalize_data(data){
  let categories = ['nomeal', 'nomecat', 'nomeind', 'nomeplat']
  //console.log('here', data[0])

  categories.forEach( elem => {
    //console.log('tem elem', elem)
    if(data[0].hasOwnProperty(elem) && data[0][elem] != ''){
      console.log('here')
      var d = data[0][elem].split(';')
      let result = d.map(e => {
        let fix = gen_tag_id(e)
        console.log('fix',fix)
        return {tag: e, tag_link: gen_tag_id(e)}
      }) 
      console.log('result', result)
      console.log('d',d)
      data[0][elem] = result
    }
  })
  return data
}
function gen_tag_id(tag){
  subs = ['\\', '/', '&', '[', ']', '(', ')']
  subs.forEach( (elem) => {
    console.log('elem', elem)
    tag = tag.replace(elem, '')
    console.log('substitui os ',elem, 'tag', tag)
  
  })
  return tag.replaceAll(' ','_').toLowerCase()
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

router.get('/:slug', function(req, res){
  Coins.getCoin(req.params.slug)
    .then( dados => {
      console.log('here')
      
      console.log('dados antes', dados)

      result_data = normalize_data(dados)
      
      console.log('dados depois', result_data)

      res.json(result_data)
      
    })
    .catch( e => res.status(500).send(`Error listing Coins ${req.params.slug} ${e}`))
});


module.exports = router;
