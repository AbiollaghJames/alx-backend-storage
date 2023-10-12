-- create stored procedure that calculates and store the
-- average weighted score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightScoreForUser(IN user_id INT)
BEGIN
	UPDATE users
	SET average_score = (
	  SELECT SUM(corrections.score * projects.weight) / NULLIF(SUM(projects.weight), 0)
	  FROM scores
	  WHERE corrections.user_id = user_id
	)
	WHERE users.id = user_id;
END //

DELIMITER ;
