import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Leonida$27",
	database="bonk"
	)

mycursor = mydb.cursor()

mycursor.execute("""

	CREATE TABLE brands(
	brand VARCHAR(40) PRIMARY KEY,
	brand_id INT UNIQUE,
	site VARCHAR(120)
	);

	CREATE TABLE gpu(
	gpu_id INT PRIMARY KEY,
	brand VARCHAR(40) NOT NULL,
	name VARCHAR(200) NOT NULL,
	memory VARCHAR(40),
	FOREIGN KEY (brand) REFERENCES brands(brand)
	);

	CREATE TABLE suppliers(
	sup_id INT PRIMARY KEY,
	sup_name VARCHAR(80),
	cut2 INT,
	cut3 INT,
	cut4 INT,
	sup_sup INT DEFAULT NULL
	);

	CREATE TABLE stock(
	gpu_id INT,
	price INT,
	deadstock BOOL,
	size DECIMAL(3,1),
	sup_id INT,
    unique_id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (unique_id),
	FOREIGN KEY (gpu_id) REFERENCES gpu(gpu_id),
	FOREIGN KEY (sup_id) REFERENCES suppliers(sup_id)
	)

    """)

print("Tables created!")