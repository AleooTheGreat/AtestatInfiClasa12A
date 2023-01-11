import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Leonida$27",
	database="bonk"
	)

mycursor = mydb.cursor(buffered=True)

brand=str(input("Brand: "))

mycursor.execute("SELECT brand_id FROM brands WHERE brand = " + '\'' + brand + '\';')

curs = mycursor.fetchall()

for x in curs:
	for i in x:
		brand_id = i

print(brand_id)
mycursor = mydb.cursor(buffered=True)

mycursor.execute("SELECT sup_id FROM stock WHERE gpu_id > " + str(1000*brand_id) + " AND gpu_id < " + str(1000*(brand_id+1)))

result = mycursor.fetchall()

print(result)
mylist=[]

for x in result:
	for i in x:
		if not i in mylist:
			mylist.append(int(i))

print(mylist)

mycursor = mydb.cursor(buffered=True)

mytuple = tuple(mylist)

print(mytuple)
if len(mytuple) == 0:
	pass
elif len(mytuple) == 1:
	mycursor.execute("SELECT sup_name FROM suppliers WHERE sup_id = " + str(mytuple[0]))
else:
	mycursor.execute("SELECT sup_name FROM suppliers WHERE sup_id IN " + str(mytuple))

result = mycursor.fetchall()

for x in result:
	for i in x:
		print('\n',i)