-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

-- Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

DELIMITER // -- DELIMTER CHANGE
CREATE TRIGGER email_reset
BEFORE UPDATE ON users  -- event time trigger table
FOR EACH ROW -- EXCUTE ON EVERY ROW
BEGIN -- trigger body
  IF NEW.email != OLD.email THEN
    SET NEW.valid_email = 1
  ELSE
    SET NEW.valid_email = 0
  END IF;
END //
DELIMITER ; -- DELEIMTER RETRIVE
