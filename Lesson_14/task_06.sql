SELECT *
FROM product INNER JOIN vendor ON product.vendor_id = vendor.id;

SELECT *
FROM product LEFT OUTER JOIN vendor ON product.vendor_id = vendor.id;

SELECT *
FROM product RIGHT OUTER JOIN vendor ON product.vendor_id = vendor.id;

SELECT *
FROM product FULL OUTER JOIN vendor ON product.vendor_id = vendor.id;


SELECT vendor.name, COUNT(*)
FROM vendor
LEFT JOIN product ON vendor.id = product.vendor_id
GROUP BY vendor.name;

SELECT vendor.name, AVG(product.price)
FROM vendor
LEFT JOIN product ON vendor.id = product.vendor_id
GROUP BY vendor.name;


SELECT vendor.name
FROM vendor
LEFT JOIN product ON vendor.id = product.vendor_id
GROUP BY vendor.name
HAVING COUNT(product.id) = 0;

SELECT *
FROM vendor