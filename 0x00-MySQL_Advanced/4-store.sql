-- script that creates trigger that decreases quantity
-- of an item after adding new record
-- use of TRIGGER

CREATE TRIGGER decrease_item
AFTER INSERT ON orders
FOR EACH ROW
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;
