SELECT id, name
FROM drinks
UNION
SELECT contactFirstName, contactLastName
FROM customers;

SELECT CONCAT(firstName,' ', lastName) AS fullname, 'employee' as category
FROM employees
UNION
SELECT CONCAT(contactFirstName,' ', contactLastName), 'customer' as category
FROM customers
ORDER BY fullname;

WITH cte AS (
    SELECT 	of.officecode,
	        of.city,
	        emp.firstName,
	        emp.lastName,
	        of.phone
	FROM offices AS of
	JOIN employees AS emp
	USING (officecode))
SELECT * FROM cte;