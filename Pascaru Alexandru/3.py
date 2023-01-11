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


mycursor.execute("SELECT name, memory FROM gpu JOIN stock ON stock.gpu_id=gpu.gpu_id WHERE gpu.brand=" + '\'' + brand + '\'' + "AND stock.size=" + str(size))

results = mycursor.fetchall()

print(tabulate(results, headers=['name', 'memory'], tablefmt='psql'))
