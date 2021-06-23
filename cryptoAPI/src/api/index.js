const express = require('express');

const coins = require('./coins');

const router = express.Router();

router.get('/', (req, res) => {
  res.json({
    message: 'Bem vindo ao nosso sistema de esquemas em pirame das cryptos. One love. To da fucking mooooooon!'
  });
});

router.use('/coins', coins);

module.exports = router;
