Connect to psql DB from command line -> psql -h hostname -p Port -U username db_name;  

Commands within psql   
Default post -> 5432   
semicolon at the end of each command  
List all the table -> \l   
list all the users -> \du    
connect to DB -> \c db_name;  
CREATE DB -> CREATE DATABASE db_name (name should be lowercase)  
DELETE B ->DROP DATABASE db_name  

CREATE TABLE -> CREATE TABLE person ( id BIGSERIAL NOT NULL PRIMARY KEY, fist_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, gender VARCHAR(5) NOT NULL, date_of_birth DATE NOT NULL);  
//here BIGSERIAL Datatype is auto increment type .   

View a table - \d table_name  

Add a new column to the tale ->  ALTER TABLE table_name ADD COLUMN column_name data_type [constraints];  
Example -> ALTER TABLE person ADD COLUMN email VARCHAR(150) NOT NULL;  

Change the name of a column -> ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;  
ex -> ALTER TABLE person RENAME fist_name TO first_name;  

Change the dtype of a column -> ALTER TABLE table_name ALTER COLUMN column_name TYPE new_data_type;  
ex -> ALTER TABLE person ALTER COLUMN gender TYPE VARCHAR(15);  

Inter values into the table -> INSERT INTO person (first_name, last_name, gender, date_of_birth, email) VALUES ('abc', 'abc', 'FEMALE', DATE '2003-05-21', 'abc@gmail.com');  

to create 1000 rows -> use Mockaroo  

to execute commands from a file -> \i path of the file   

ORDER BY ->  SELECT * FROM person ORDER BY country_of_birth; (by Default ASC)
-> SELECT * FROM person ORDER BY country_of_birth DESC;  

DISTINCT ->  SELECT DISTINCT country_of_birth FROM person ORDER BY country_of_birth;
WHERE -> SELECT * FROM person WHERE country_of_birth= 'Zimbabwe';  
WHERE & AND -> SELECT * FROM person WHERE country_of_birth= 'Zimbabwe' and gender='FEMALE';  
WHERE & AND & OR -> SELECT * FROM person WHERE (country_of_birth= 'Zimbabwe' OR country_of_birth='China') and gender='Female';  

Comparison operator -> <>(not equal) , <=, >=, =, <,>    
LIMIT -> SELECT * FROM person LIMIT 10;  (limits the no of records returned by the query )    
OFFSET -> SELECT * FROM person OFFSET 5; (returns the query res after the offset no of records)    

//limit is not a sql standard , FETCH command is preferred to be used for limiting 
FETCH ->  SELECT * FROM person FETCH FIRST 10 ROW ONLY;    

IN -> SELEct * FROM person WHERE country_of_birth IN('Brazil', 'China', 'France');
//better than using multiple OR's     

IN & ORDER BY -> SELEct * FROM person WHERE country_of_birth IN('Brazil', 'China', 'France') ORDER BY country_of_birth;    

BETWEEN -> SELECT * FROM person WHERE date_of_birth BETWEEN DATE '2000-01-01' AND '2025-02-22';    

LIKE -> SELECT * FROM person WHERE email LIKE '%@bloomberg.com';    
SELECT * FROM person WHERE email LIKE '________@%';    
// % -> wild card i.e anything     
//_ -> no of characters (any)    

//ILIKE keyword igonres the case unlike LIKE Keyword     
ILIKE -> SELECT * FROM person WHERE country_of_birth ILIKE 'j%';   

GROUP BY -> SELECT country_of_birth , COUNT(*) FROM person GROUP BY country_of_birth;    

