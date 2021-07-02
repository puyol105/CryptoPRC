const app = require('./app');

const port = process.env.PORT || 5102;
app.listen(port, () => {
  console.log(`Listening: http://localhost:${port}`);
});
