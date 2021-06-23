const express = require('express');
const coins = require('../controllers/coins');

const router = express.Router();

router.get('/', coins.list);

module.exports = router;
