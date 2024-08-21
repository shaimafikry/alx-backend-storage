-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

-- Requirements:

-- Procedure ComputeAverageWeightedScoreForUsers is not taking any input.
-- Tips:

-- Calculate-Weighted-Average

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users
  SET average_score = (
      SELECT SUM(score * weight) / SUM(weight)
      FROM corrections
      JOIN projects
      ON corrections.project_id = projects.id
      WHERE corrections.user_id = users.id
  );

END //
DELIMITER ;
