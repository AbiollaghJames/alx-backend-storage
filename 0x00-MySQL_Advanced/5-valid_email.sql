-- script that creates trigger that resets attribute
-- valid_email only when email is changed.
-- use TRIGGER

DELIMETER$$

CREATE TRIGGER reset_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END$$

DELIMETER;
