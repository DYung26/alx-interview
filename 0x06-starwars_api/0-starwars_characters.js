#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films/'

request(`${API_URL}${process.argv[2]}/`, (error, response, body) => {
  const characters = JSON.parse(body).characters;
  const charactersName = characters.map(character_url => new Promise((resolve, reject) => {
    request(character_url, (error, response, body) => {
      resolve(JSON.parse(body).name);
    });
  }));

  Promise.all(charactersName)
    .then(names => console.log(names.join('\n')))
    .catch(allErr => console.log(allErr));
});
