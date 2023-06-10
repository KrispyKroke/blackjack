const express = require('express');
const pool = require('../modules/pool');
const router = express.Router();

// This route is used to select the current player of the game.
router.get('/:id', (req, res) => {
    const person = req.params.id;
    const queryText = `SELECT * FROM players WHERE "name" = $1;`;
    pool.query(queryText, [person]).then(response => {
        res.send(response.rows);
    }).catch(error => {
        console.log(error);
        res.sendStatus(500);
    }); 
});

// This route is used to add a new player to the game.
router.post('/add', (req, res) => {
    const person = req.body;
    const queryText = `INSERT INTO players ("name") 
    VALUES ($1);`;
    pool.query(queryText, [person.name]).then(response => {
        res.sendStatus(201);
    }).catch(error => {
        console.log(error);
        res.sendStatus(500);
    });
});

// Route for score initialization to 0 when a new player is added to the game.
router.post('/score', (req, res) => {
    const newScore = req.body;
    const queryText = `INSERT INTO scores ("wins", "player_id")
    VALUES ('0', $1);`;
    pool.query(queryText, [newScore.player_id]).then(response => {
        res.sendStatus(201);
    }).catch(error => {
        console.log(error);
        res.sendStatus(500);
    });
});

module.exports = router;