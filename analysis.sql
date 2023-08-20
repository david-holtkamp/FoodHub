SELECT DISTINCT res.name, res.address, res.phone_number 
FROM restaurants AS res 
JOIN menu_items AS menu on res.id = menu.restaurant_id
WHERE res.cuisines LIKE '%"Mediterranean"%'
AND menu.price < 15.0;

