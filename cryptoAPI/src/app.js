const express = require('express');
const morgan = require('morgan');
const helmet = require('helmet');
const path = require('path');
const cors = require('cors');
const cookieParser = require('cookie-parser');
const multer = require('multer')


require('dotenv').config();

const mongoose = require('mongoose');

const { v4: uuidv4 } = require('uuid');
const session = require('express-session');
const FileStore = require('session-file-store')(session);
const passport = require('passport');
const passportSetup = require('./config/passport-setup.js');



// Set up default mongoose connection
const mongoDB = 'mongodb://127.0.0.1/BD_Crypto_Cenas';
mongoose.connect(mongoDB, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Get the default connection
const db = mongoose.connection;

// Bind connection to error event (to get notification of connection errors)
db.on('error', console.error.bind(console, 'MongoDB connection error...'));
db.once('open', () => {
  console.log('MongoDB connected successfully...');
});

const middlewares = require('./middlewares');

const api = require('./api');
const usersRouter = require('./api/users');
const coinsRouter = require('./api/coins');
const exchangesRouter = require('./api/exchanges');
const tradingPairsRouter = require('./api/tradingPairs');
const tagsRouter = require('./api/tags');

const app = express();


//CORS
const corsOpts = {
    origin: '*',
    credentials: true,
    methods: ['GET', 'PUT', 'POST', 'DELETE', 'OPTIONS'],
    allowedHeaders: ['Accept', 'Authorization', 'Cache-Control', 'Content-Type', 'DNT', 'If-Modified-Since', 'Keep-Alive', 'Origin', 'User-Agent', 'X-Requested-With', 'Content-Length']
}
app.use(cors(corsOpts))
app.options('*', cors(corsOpts))

app.use(multer().array()); 



app.use(session({
  genid: (req) => uuidv4(),
  store: new FileStore(),
  secret: 'O meu segredo',
  resave: false,
  saveUninitialized: false,
  name: 'cookie'
}));

app.use(morgan('dev'));
app.use(helmet());
// app.use(cors({
//   origin: '*',
//   methods: ['POST']
// }));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use(passport.initialize());
app.use(passport.session());

app.get('/', (req, res) => {
  res.json({
    message: '🦄🌈✨👋🌎🌍🌏✨🌈🦄'
  });
});

app.use('/api/v1', api);
app.use('/users', usersRouter);
app.use('/coins', coinsRouter);
app.use('/exchanges', exchangesRouter);
app.use('/tradingPairs', tradingPairsRouter);
app.use('/tags', tagsRouter);

app.use(middlewares.notFound);
app.use(middlewares.errorHandler);

module.exports = app;
