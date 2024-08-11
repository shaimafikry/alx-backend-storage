-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

-- Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

DELIMITER // -- DELIMTER CHANGE
CREATE TRIGGER email_reset
AFTER UPDATE ON users  -- event time trigger table
FOR EACH ROW -- EXCUTE ON EVERY ROW
BEGIN -- trigger body
  IF NEW.email != OLD.email THEN
    UPDATE users
    SET valid_email = 0
    WHERE id = NEW.id;
  END IF;
END //
DELIMITER ; -- DELEIMTER RETRIVE
