-- Write your query below
SELECT C.customer_id, C.customer_name
FROM customers AS C
WHERE C.customer_id IN (SELECT customer_id FROM orders WHERE product_name = 'A')
    AND C.customer_id IN (SELECT customer_id FROM orders WHERE product_name = 'B')
    AND C.customer_id NOT IN (SELECT customer_id FROM orders WHERE product_name = 'C')
ORDER BY C.customer_name;