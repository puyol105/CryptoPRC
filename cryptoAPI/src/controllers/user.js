const User = require('../models/user');

// Devolve a lista de alunos
module.exports.listar = () => User
  .find()
  .exec();

module.exports.consultar = (id) => User
  .findOne({
    _id: id
  })
  .exec();

module.exports.lookUpUsername = (uname) => User
  .findOne({
    username: uname
  })
  .exec();

module.exports.inserir = (u) => {
  const novo = new User(u);
  return novo.save();
};

module.exports.eliminar = (id) => User
  .deleteOne({
    _id: id
  });

module.exports.atualizar = (id, user) => User
  .updateOne({
    _id: id
  }, user);
