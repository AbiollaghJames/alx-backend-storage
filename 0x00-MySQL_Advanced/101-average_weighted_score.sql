-- create stored procedure that compute and store
-- the average weighted score for all students.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users AS u
	JOIN (
		SELECT u.id, COALESCE(SUM(score * weight) / NULLIF(SUM(weight), 0), NULL) AS avg
		FROM users AS u
		JOIN corrections AS c ON u.id = c.user_id
		JOIN projects AS p ON c.project_id = p.id
		GROUP BY u.id
	)
	AS weight ON u.id = weight.id
	SET u.average_score = weight.avg;
END //

DELIMITER ;
