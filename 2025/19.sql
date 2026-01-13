/*Queries using DISTINCT, BETWEEN, IN, LIKE, IS NULL, ORDER BY, GROUP BY, HAVING 
*/
use SchoolDB;
alter table Pupils drop column Phone;


select DISTINCT Name from Pupils;

select * from Pupils where Age BETWEEN 15 AND 18;

select * from Pupils where Class IN ('11th', '12th');

select * from Pupils where Name LIKE 'A%';

alter table Pupils add column Phone varchar(15) NULL;

select * from Pupils where Phone IS NULL;  

select * from Pupils ORDER BY Name ASC;

select Class, COUNT(*) from Pupils GROUP BY Class;

select Class, Age from Pupils GROUP BY Class HAVING Age > 15;

