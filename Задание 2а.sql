SELECT Menu.Group,
	   MIN(Price) as min_price
FROM (SELECT *
	  FROM MainMenu
	  UNION
	  SELECT *
	  FROM VegMenu) as Menu
WHERE Menu.Group in ('Салаты','Основное блюдо','Напитки')
GROUP BY Menu.Group;