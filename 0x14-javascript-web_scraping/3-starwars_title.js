const request = require('request');

const movieId = process.argv[2];
const host = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(host, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
