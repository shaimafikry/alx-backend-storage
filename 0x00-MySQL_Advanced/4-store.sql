-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

-- Quantity in the table items can be negative.

-- Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

DELIMITER //  -- i change the end delimeter so that i can do more than one statment without ending the block
CREATE TRIGGER sum_quantity -- creation and name
AFTER  -- trigger time
INSERT -- trigger event 
ON orders  -- table that activate trigger
FOR EACH ROW 
BEGIN
  UPDATE items
  set quantity = quantity - NEW.number -- NEW represent the new value
  WHERE name = NEW.item_name;
END //
DELIMITER ; -- i retrieve the normal delimiter
