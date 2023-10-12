-- create a function that divides two integer numbers
-- and retuns result or 0 if second number = 0

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
	RETURN (IF (b = 0, 0, a / b));
END //

DELIMITER ;
