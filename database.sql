CREATE TABLE players (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE scores (
	"id" SERIAL PRIMARY KEY,
	"wins" INT NOT NULL,
	"player_id" INT REFERENCES "players" ON DELETE CASCADE
);

INSERT INTO players ("name") 
VALUES ('Jared'), ('Jake'), ('Denise');

INSERT INTO scores ("wins", "player_id") 
VALUES ('8', '1'), ('5', '2'), ('12', '3');

-- Query for incrementing number of wins for a player.
UPDATE scores 
SET "wins" = "wins" + 1 
WHERE "player_id" = '1';

SELECT * FROM players WHERE "name" = 'Jared';

SELECT "wins" FROM scores WHERE "player_id" = '1';

-- Query which grabs the top 5 scores for all recorded players of the game.
SELECT players."name", scores."wins" FROM scores
JOIN players ON players."id" = scores."player_id" 
ORDER BY scores."wins" DESC LIMIT 5;


DROP TABLE players CASCADE;

DROP TABLE scores CASCADE;