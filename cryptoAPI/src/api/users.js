const express = require('express');

const router = express.Router();
const passport = require('passport');
const { verificaAutenticacao } = require('../config/common');

const User = require('../controllers/user');

// GET users listing.
router.get('/', verificaAutenticacao, (req, res) => {
  User.listar()
    .then((dados) => res.render('users', {
      title: 'Lista de Users',
      users: dados
    }))
    .catch((e) => res.render('error', {
      error: e
    }));
});

// GET '/users/logout' to clean cookie
router.get('/logout', (req, res) => {
  User.atualizar(req.user._id, { dateLast: Date.now() })
    .then(() => {
      req.logout();
      req.session.destroy((err) => {
        if (!err) {
          res.clearCookie('cookie');
          res.redirect('/');
        } else {
          // eslint-disable-next-line no-console
          console.log('Destroy session error: ', err);
        }
      });
    })
    .catch((e) => res.render('error', {
      error: e
    }));
});

// POST '/users/login'  login
router.post('/login', passport.authenticate('local'), (req, res) => {
  console.log("ENOTRU!!!!!!", req)
  res.json(req.user)
  
});

// POST regista novo user
router.post('/signup', (req, res) => {
  console.log(req.body)
  const user = {
    name: req.body.name,
    username: req.body.username,
    email: req.body.email,
    password: req.body.password
  };

  const unames = [];
  const emails = [];

  User.listar()
    .then((dados) => {
      dados.forEach((u) => {
        unames.push(u.username);
        emails.push(u.email);
      });
      let errormsg = ' ';
      if (unames.includes(user.username)) {
        errormsg = 'Username indisponível';
      } else if (emails.includes(user.email)) {
        errormsg = 'Email indisponível';
      }

      if (errormsg === ' ') {
        User.inserir(user)
          .then((dados2) => {res.json(dados2)})
          .catch((e) => res.render('error', {
            error: e
          }));
      }
    })
    .catch((e) => res.render('error', {
      error: e
    }));
});

// POST delete user
router.post('/delete/:idUser', verificaAutenticacao, (req, res) => {
  if (req.user.level === 'admin' || req.user._id === req.params.idUser) {
    User.eliminar(req.params.idUser)
      .then(() => {
        res.render('users/deleted');
      })
      .catch((e) => res.render('error', {
        error: e
      }));
  } else {
    res.redirect('/');
  }
});

// POST update user
router.post('/update/:idUser', verificaAutenticacao, (req, res) => {
  const { idUser } = req.params;
  const user = req.body;

  const unames = [];
  const emails = [];

  User.listar()
    .then((dados) => {
      dados.forEach((u) => {
        unames.push(u.username);
        emails.push(u.email);
      });
      let errormsg = ' ';
      if (unames.includes(user.username)) {
        errormsg = 'Username indisponível';
      } else if (emails.includes(user.email)) {
        errormsg = 'Email indisponível';
      } if (errormsg !== ' ') {
        console.log(errormsg);
        res.render('users/user', {
          title: 'Página de Perfil',
          checksame: true,
          infouser: req.user,
          errormsg
        });
      } else {
        User.atualizar(idUser, user)
          .then(() => {
            res.render('users/userUpdate');
          })
          .catch((e) => res.render('error', {
            error: e
          }));
      }
    })
    .catch((e) => res.render('error', {
      error: e
    }));
});

// GET user page
router.get('/:uname', verificaAutenticacao, (req, res) => {
  const { uname } = req.params;
  let checksame = false;

  if (uname === req.user.username || req.user.level === 'admin') {
    checksame = true;
  }

  User.lookUpUsername(uname)
    .then((dados) => res.render('users/user', {
      infouser: dados,
      checksame,
      title: 'Página de Perfil'
    }))
    .catch((e) => res.render('error', {
      error: e
    }));
});

//GET user favs
router.get('/:uname/favs', verificaAutenticacao, (req, res) => {
  var user = req.user;
  console.log("USR", user)
  User.consultar(user)
    .then(dados => res.render('/favs', {
      dados: dados
    }))
    .catch(e => res.render('error', {
      error: e
    }))
})

// POST add fave 
// router.post('/update/:idUser', verificaAutenticacao, (req, res) => {
  
// }

module.exports = router;

