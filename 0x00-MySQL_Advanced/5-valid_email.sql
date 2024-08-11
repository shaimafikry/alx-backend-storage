-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

-- Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

DELIMITER // -- DELIMTER CHANGE
CREATE TRIGGER email_reset
AFTER --time
UPDATE --event
ON users -- trigger table
-- trigger body
FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email
    UPDATE users
    SET valid_email = 1 WHERE user_id = NEW.user_id;
  END IF;
END //
DELIMITER ; -- DELEIMTER RETRIVE
