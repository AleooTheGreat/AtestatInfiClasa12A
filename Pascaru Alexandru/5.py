import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Leonida$27",
	database="bonk"
	)

mycursor = mydb.cursor(buffered=True)


brand=str(input("brand: "))
brand_id=int(input("brand_id: "))
site=str(input("site: "))


ins=(brand, brand_id, site)

cod = "INSERT INTO brands(brand, brand_id, site) VALUES(%s, %s, %s)"

mycursor.execute(cod, ins)

mycursor.execute("SELECT * FROM gpu WHERE brand=\"" + brand + "\"")

gpu_id = int(1000*brand_id) + int(mycursor.rowcount) + 1
print (gpu_id)
name=str(input("name: "))
memory=str(input("memory: "))

ins=(gpu_id, brand, name, memory)

cod = "INSERT INTO gpu(gpu_id, brand, name, memory) VALUES(%s, %s, %s, %s)"

mycursor.execute(cod, ins)

mycursor = mydb.cursor()

price=int(input("price: "))
deadstock=bool(input("(1 = DA, 0 = NU) deadstock: "))
size=float(input("Size: "))
sup_id=int(input("sup_id: "))
ins=(gpu_id, price, deadstock, size, sup_id)

cod = "INSERT INTO stock(gpu_id, price, deadstock, size,  sup_id) VALUES(%s, %s, %s, %s, %s)"

mycursor.execute(cod, ins)

mydb.commit()

print('Done inserting!')