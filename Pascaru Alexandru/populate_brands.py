import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Leonida$27",
	database="bonk"
	)

mycursor = mydb.cursor()

lsbrands = [
("Nvidia",1,"nvidia.com"),
("Intel",2,"intel.com"),
("AMD",	3,"amd.com"),
("Corsair",4,"corsair.com"),
("MSI",5,"msi.com"),
("ASUS",6,"asus.com"),
]


cod = "INSERT INTO brands(brand, brand_id, site) VALUES(%s, %s, %s)"

mycursor.executemany(cod, lsbrands)

mydb.commit()

print(mycursor.rowcount, "inserted!")