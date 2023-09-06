#!/usr/bin/node

const request = require('request');

const arg = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg;

const getCharacters = (index, charactersLink) => {
  if (index >= charactersLink.length) {
    return;
  }
  request(charactersLink[index], (err, res, body) => {
    if (err) {
      console.log('An Error Occured!');
    } else {
      console.log(JSON.parse(body).name);
      getCharacters(index + 1, charactersLink);
    }
  });
};

request(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    getCharacters(0, data.characters);
  } else {
    console.log('An Error Occurred!');
    return [];
  }
});
