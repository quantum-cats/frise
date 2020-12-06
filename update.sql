-- UPDATE events
-- SET labels = "date of birth",
-- 	details = "I was born in Schoelcher"
-- WHERE
-- 	id = 1;

DELETE FROM events
WHERE labels IS NULL OR trim(labels) = "";