// #!/usr/bin/node

// const request = require('request');

// const arg = process.argv[2];
// const url = 'https://swapi-api.alx-tools.com/api/films/' + arg;
// const getCharacters = async () => {
//     request(url, (err, res, body) => {
//   if (!err && res.statusCode === 200) {
//     const data = JSON.parse(body);
//     const charactersLink = data.characters;
//     for (const link of charactersLink) {
//       await request(element, (error, response, body_) => {
//         if (!error && response.statusCode === 200) {
//           const data_ = JSON.parse(body_);
//           console.log(data_.name);
//         }
//       });
//     };
//   } else {
//     console.log('An Error Occurred!');
//   }
// })};

let request = require('request');
request = require('request-promise');

const arg = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg;

const getCharacters = async (url) => {
  const response = await request(url);
  if (response) {
    const charactersLink = JSON.parse(response).characters;
    for (const link of charactersLink) {
      const name = await request(link);
      if (name) {
        console.log(JSON.parse(name).name);
      } else {
        console.log('An Error Occured!');
      }
    }
  } else {
    console.log('An Error Occured!');
  }
};

getCharacters(url);
