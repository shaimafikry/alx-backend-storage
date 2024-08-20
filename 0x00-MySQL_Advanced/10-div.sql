-- Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.


DELIMITER $$
CREATE FUNCTION SafeDiv (IN a INT, IN b INT)
RETURN FLOAT
BEGIN
	DECLARE res FLOAT;
	IF b = 0 THEN
		RETURN 0;
	END IF;
	SET res = a /b;
	RETURN res;
END $$
DELIMITER ;;
