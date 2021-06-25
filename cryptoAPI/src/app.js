const express = require('express');
const morgan = require('morgan');
const helmet = require('helmet');
const cors = require('cors');

require('dotenv').config();

const middlewares = require('./middlewares');

const api = require('./api');
const coinsRouter = require('./api/coins')
const exchangesRouter = require('./api/exchanges')
const tradingPairsRouter = require('./api/tradingPairs')
const categoriesRouter = require('./api/categories')

const app = express();

app.use(morgan('dev'));
app.use(helmet());
app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.json({
    message: '🦄🌈✨👋🌎🌍🌏✨🌈🦄'
  });
});

app.use('/api/v1', api);
app.use('/coins', coinsRouter)
app.use('/exchanges', exchangesRouter)
app.use('/tradingPairs', tradingPairsRouter)
app.use('/categories', categoriesRouter)

app.use(middlewares.notFound);
app.use(middlewares.errorHandler);

module.exports = app;
