SELECT distinct(p1.email)
FROM Person as p1, Person as p2
WHERE p1.id != p2.id AND p1.email = p2.email
