WITH table_1 AS
	(SELECT Group as group,
	 		MAX(Price) as cost
	 FROM MainMenu
	 GROUP BY Group)
SELECT name, MainMenu.Group, MainMenu.Price
FROM MainMenu JOIN table_1 on MainMenu.Price = table_1.cost
AND MainMenu.Group = table_1.group;
