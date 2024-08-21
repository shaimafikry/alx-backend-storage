-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

-- how to get weight value:
-- multiple every grade * its weight value / sum of weights
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	DECLARE weight_score FLOAT;

	SELECT SUM(score * weight) / SUM(weight)
	INTO weight_score
	FROM projects
	JOIN corrections ON correction.project_id = project.id
	WHERE corrections.user_id = user_id;
	
		-- updated the table
	UPDATE users
	SET average_score = weight_score
	WHERE id = user_id;
END //
DELIMITER ;
