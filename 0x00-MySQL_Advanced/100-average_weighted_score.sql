-- create stored procedure that calculates and store the
-- average weighted score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightScoreForUser(IN user_id INT)
BEGIN
	UPDATE users
	SET average_score = (
	SELECT COALESCE(SUM(corrections.score * projects.weight) / NULLIF(SUM(projects.weight), 0), NULL)
	FROM corrections
	INNER JOIN projects
	ON projects.id = corrections.project_id
	WHERE corrections.user_id = user_id)
	WHERE users.id = user_id;
END //

DELIMITER ;
