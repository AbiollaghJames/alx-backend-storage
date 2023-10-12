-- script that creates trigger that resets attribute
-- valid_email only when email is changed.
-- use TRIGGER

CREATE TRIGGER reset_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;
