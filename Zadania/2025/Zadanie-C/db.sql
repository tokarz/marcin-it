UPDATE Accounts
SET AccountNumber = '007'
WHERE Id = 4;

UPDATE Accounts
SET AccountNumber = '008'
WHERE PersonId = 66;

UPDATE Accounts
SET AccountNumber = ''
WHERE PersonId = NULL;

DELETE FROM Person
WHERE Id = 3;

DELETE p FROM Person p
LEFT JOIN Accounts a ON p.Id = a.PersonId
WHERE a.PersonId = NULL;

SELECT AccountNumber FROM Accounts
JOIN Person ON Person.Id = Accounts.PersonId
WHERE Person.Name = 'John';

SELECT DateOfBirth FROM Person
WHERE Person.LastName = 'LastName_10';

SELECT Name , LastName , DateOfBirth FROM Person
WHERE Name LIKE '%Name_%'
ORDER BY DateOfBirth ASC;
