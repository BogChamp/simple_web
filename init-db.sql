CREATE TABLE IF NOT EXISTS
users(
    id    	      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    login      	      TEXT NOT NULL,
    money_amount      TEXT NOT NULL,
    card_number       TEXT NOT NULL,
    status            TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS
passwd(
    id          	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    password            TEXT NOT NULL
);

INSERT INTO users ( login, money_amount, card_number, status ) VALUES
	( 'admin', '1000000', '4916866040325754', 'active' ),
	( 'Roma', '10', '5568094018238705', 'active' ),
	( 'Vlad', '10', '6011632972308153', 'active' ),
	( 'Alexey', '10', '349294990763442', 'inactive' ),
	( 'Ruslan', '10', '4916229809560998', 'inactive' ),
	( 'Natalia', '10', '377078336805586', 'inactive' )
;	

INSERT INTO passwd ( password ) VALUES
	('admin'),
	('easy'),
	('easy'),
	('easy'),
	('easy'),
	('easy')
;
