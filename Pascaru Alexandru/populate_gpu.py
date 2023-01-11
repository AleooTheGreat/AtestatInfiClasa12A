import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Leonida$27",
	database="bonk"
	)

mycursor = mydb.cursor()

lssnk =[
(1001,"Nvidia","RTX 3060","12 GB"),
(1002,"Nvidia","RTX 3070","8 GB"),
(1003,"Nvidia","RTX 3080","10 GB"),
(1004,"Nvidia","RTX 2060","12 GB"),
(1005,"Nvidia","RTX 3060 Ti","12 GB"),
(1006,"Nvidia","RTX 3080 Ti","10 GB"),
(1007,"Nvidia","RTX 4090","24 GB"),
(1008,"Nvidia","RTX 2070 SUPER","8 GB"),
(1009,"Nvidia","RTX 3050 ","8 GB"),
(2001,"Intel","Arc A750","8 GB"),
(3001,"AMD","Radeon RX 6750","12 GB"),
(3002,"AMD","Radeon RX 6900","16 GB"),
(3003,"AMD","Radeon RX 6700","12 GB"),
(3004,"AMD","Radeon RX 7900","20 GB"),
(3005,"AMD","Radeon RX 6800","16 GB"),
(3006,"AMD","Radeon RX 6600","8 GB"),
(3007,"AMD","Radeon RX 6950","16 GB"),
(4001,"Corsair","RTX 4080","16 GB"),
(4002,"Corsair","RTX 3060","12 GB"),
(4003,"Corsair","ARC A770","8 GB"),
(5001,"ASUS","ROG Strix Radeon RX 6700","12 GB"),
(5002,"ASUS","RTX 3060 Ti Rog Strix","12 GB"),
(5003,"ASUS","RTX 3070 Noctua","8 GB"),
(6001,"MSI","RX 6750 XT","12 GB"),
(6002,"MSI","Radeon RX 6800","16 GB"),
(6003,"MSI","RTX 4080","16 GB"),

]

cod = "INSERT INTO gpu(gpu_id, brand, name, memory) VALUES(%s, %s, %s, %s)"

mycursor.executemany(cod, lssnk)

mydb.commit()

print(mycursor.rowcount, "inserted!")