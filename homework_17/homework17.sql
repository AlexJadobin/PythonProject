SELECT
		firstName,
		lastName,
		email,
		jobTitle,
		RANK() OVER (ORDER BY lastname)
		FROM employees;

SELECT customers.customerNumber,
		 customers.customerName,
		 customers.phone,
		 orders.orderNumber,
		 orders.orderDate,
		 LAG (orders.orderDate, 1)
		 OVER (PARTITION BY customers.customerNumber, ORDER BY orders.orderDate) AS prev_order_day
		 FROM customers
		 JOIN orders USING (customerNumber)