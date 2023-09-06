#!/usr/bin/node

const request = require('request');

const arg = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg;
request(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const charactersLink = data.characters;
    charactersLink.forEach(element => {
      request(element, (error, response, body_) => {
        if (!error && response.statusCode === 200) {
          const data_ = JSON.parse(body_);
          console.log(data_.name);
        }
      });
    });
  } else {
    console.log('An Error Occurred!');
  }
});
