-- create a function that divides two integer numbers
-- and retuns result or 0 if second number = 0

DELIMITER //

CREATE FUNCTION SafeDiv(a INTEGER, b INTEGER)
RETURNS INTEGER
BEGIN
	IF b = 0
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END;
//
DELIMITER ;
