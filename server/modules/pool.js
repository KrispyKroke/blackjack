const pg = require('pg');

let config = {
    host: 'localhost',
    port: 5432,
    database: 'blackjack', 
};


const pool = new pg.Pool(config);


pool.on('connect', () => {
  console.log('Postgesql connected');
});


pool.on('error', (err) => {
  console.log('Unexpected error on idle client', err);
  process.exit(-1);
});

module.exports = pool;