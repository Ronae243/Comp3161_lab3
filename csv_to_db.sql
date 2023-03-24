-- Load data from CSV file into the table
LOAD DATA INFILE 'C:\\Users\\Ronae\\Documents\\y3\\Database\\lab 3\\Customers.csv' INTO TABLE Customers
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;