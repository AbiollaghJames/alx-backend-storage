-- create a function that divides two integer numbers
-- and retuns result or 0 if second number = 0

DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
	IF b = 0
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END //

DELIMITER ;
