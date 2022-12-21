import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Leonida$27",
	database="bonk"
	)

mycursor = mydb.cursor()

lsstk=[
(1001,450,True,12,3),
(1002,525,True,8,1),
(1003,800,True,10,2),
(1003,850,True,10,6),
(1004,300,True,12,3),
(1005,600,True,12,5),
(1006,1200,True,10,5),
(1007,1800,True,24,4),
(1008,340,True,8,1),
(1009,250,True,8,3),
(3001,300,False,12,2),
(3002,800,True,16,5),
(3002,810,True,16,4),
(3002,830,True,16,4),
(3003,340,True,12,1),
(3004,1050,True,20,5),
(3007,250,True,16,1),
(3005,1075,True,16,6),
(3005,370,True,16,6),
(3006,120,True,8,2),
(4001,1300,True,16,4),
(4002,470,True,12,3),
(4003,280,False,8,5),
(5002,625,True,12,5),
(5003,760,True,8,3),
(5001,490,True,12,4),
(6001,675,False,12,6),
(6002,770,True,16,2),
(6003,1500,True,16,2),

]

cod = "INSERT INTO stock(gpu_id, price, deadstock, size, sup_id) VALUES(%s, %s, %s, %s, %s)"

mycursor.executemany(cod, lsstk)

mydb.commit()

print(mycursor.rowcount, "inserted!")