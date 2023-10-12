-- create a function that divides two integer numbers
-- and retuns result or 0 if second number = 0

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF b = 0
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END //

DELIMITER ;
