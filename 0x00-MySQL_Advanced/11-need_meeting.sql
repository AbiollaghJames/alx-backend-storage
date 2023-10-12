-- create a view that lists all students with score under 80
-- and no last meetiing or more than 1 month

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND
(students.last_meeting IS NULL OR students.last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
