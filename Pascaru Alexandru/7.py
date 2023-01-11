import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Leonida$27",
	database="bonk"
	)

mycursor = mydb.cursor(buffered=True)

size=str(input("size: "))
brand=str(input("brand: "))



mycursor.execute("SELECT stock.price FROM stock JOIN gpu ON stock.gpu_id=gpu.gpu_id WHERE gpu.brand=" + '\'' + brand + '\'' + "AND stock.deadstock=1 AND stock.size=" + str(size))

minim = 1000000000

for x in mycursor:
	for i in x:
		minim = min(minim, int(i))

if(minim != 1000000000):
	print('Minim =', minim)

else:
	print("GPU not found!")