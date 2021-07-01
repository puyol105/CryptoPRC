const mongoose = require('mongoose');

const Schema = new mongoose.Schema({
  name: String,
  email: String,
  username: String,
  password: String,
  level: String,
  dateRegister: { type: Date, default: Date.now },
  dateLast: { type: Date, default: Date.now },
  favCoins: [String],
});

module.exports = mongoose.model('User', Schema, 'users');
