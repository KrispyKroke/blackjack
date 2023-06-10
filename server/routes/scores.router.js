const express = require('express');
const pool = require('../modules/pool');
const router = express.Router();

// This route will grab the number of wins for a specific player.
router.get('/single/:id', (req, res) => {
    const person = req.params.id;
    const queryText = `SELECT "wins" FROM scores WHERE "player_id" = $1;`;
    pool.query(queryText, [person]).then(response => {
        res.send(response.rows);
    }).catch(error => {
        console.log(error);
        res.sendStatus(500);
    });
});

// This route handles the incrementation of the current player's score by one.
router.put('/increase/:id', (req, res) => {
    const person = req.params.id;
    const queryText = `UPDATE scores 
    SET "wins" = "wins" + 1 
    WHERE "player_id" = $1;`;
    pool.query(queryText, [person]).then(response => {
        res.sendStatus(200);
    }).catch(error => {
        console.log(error);
        res.sendStatus(500);
    });
});

// GET route which retrieves and orders the 5 highest scores in the database.
router.get('/highest', (req, res) => {
    const queryText = `SELECT players."name", scores."wins" FROM scores
    JOIN players ON players."id" = scores."player_id" 
    ORDER BY scores."wins" DESC LIMIT 5;`;
    pool.query(queryText).then(response => {
        res.send(response.rows);
    }).catch(error => {
        console.log(error);
        res.sendStatus(500);
    });
});


module.exports = router;