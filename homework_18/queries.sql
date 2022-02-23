EXPLAIN
SELECT customerNumber, contactFirstName, contactLastName
FROM customers
WHERE contactFirstName = 'Jean' AND contactLastName = 'King';

CREATE INDEX ix_fullname ON customers (contactLastName,contactFirstName);

START TRANSACTION;
DELETE FROM shows;
ROLLBACK;
SELECT  * FROM shows;