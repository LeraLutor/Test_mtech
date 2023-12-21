SELECT *
FROM VegMenu
WHERE ID_Dish NOT in (SELECT ID_Dish
					  FROM MainMenu);
