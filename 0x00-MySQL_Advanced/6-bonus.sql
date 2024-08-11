-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
-- Requirements:
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction
-- Context: Write code in SQL is a nice level up!
-- Syntax:
-- CREATE [DEFINER = { user | CURRENT_USER }]          
-- PROCEDURE sp_name ([proc_parameter[,...]])          
-- [characteristic ...] routine_body    
-- proc_parameter: [ IN | OUT | INOUT ] param_name type    
-- type:          
-- Any valid MySQL data type    
-- characteristic:          
-- COMMENT 'string'     
-- | LANGUAGE SQL      
-- | [NOT] DETERMINISTIC      
-- | { CONTAINS SQL | NO SQL | READS SQL DATA 
-- | MODIFIES SQL DATA }      
-- | SQL SECURITY { DEFINER | INVOKER }    
-- routine_body:      
-- Valid SQL routine statement
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER \\
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(225), IN score INT)
BEGIN
  -- define a var to hold project user_id
  DECLARE project_id INT;
  -- Initialize project_id to NULL
  SET project_id = NULL;
  -- add id value to project_id
  SELECT id INTO project_id
  FROM projects
  WHERE name = project_name;

  IF project_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    -- Retrieve the ID of the newly inserted project
    -- BUILT-IN PROCEDURE
    SET project_id = LAST_INSERT_ID();
  END IF;
  INSERT INTO corrections(user_id, project_id, score)
  VALUES (user_id, project_id, score);
END \\
DELIMITER ;
