-- demonstrate basic SQL commands showing the following
--Queries using Create database, Show databases, Use, Create table, Show Tables, Describe, 
--Rename, Alter, Select, From, Where, Insert, Update commands 

create database SchoolDB;


show databases;

use SchoolDB;

create table Students (
    Roll int primary key,
    Name varchar(50),
    Age int,
    Class varchar(10)
);

show tables;

describe Students;

rename table Students to Pupils;

alter table Pupils add column Address varchar(100);

select * from Pupils where Age > 10;

insert into Pupils (Roll, Name, Age, Class, Address) values (1, 'Hira', 17, '12th', 'RZ-243');

update Pupils set Address = 'P-128' where Roll = 1;

