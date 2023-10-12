-- script that creates trigger that decreases quantity
-- of an item after adding new record
-- use of TRIGGER

CREATE TRIGGER decrease_item
AFTER INSERT ON orders
FOR EACH ROW
	UPDATE items
	SET quantity = quantity - 1
	WHERE name = NEW.item_name;
END;
