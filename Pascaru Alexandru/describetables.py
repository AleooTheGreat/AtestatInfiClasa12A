import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Leonida$27",
	database="bonk"
	)

mycursor = mydb.cursor()

mycursor.execute("""
	DESCRIBE gpu;
    """)

print('\nGPU\n')

results = mycursor.fetchall()

print(tabulate(results, headers=['Field','Type','Null','KEY','Default','Extra'], tablefmt='psql'))

print('\nSTOCK\n')

mycursor.execute("""
	DESCRIBE stock;
    """)

results = mycursor.fetchall()

print(tabulate(results, headers=['Field','Type','Null','KEY','Default','Extra'], tablefmt='psql'))
	
print('\nSUPPLIERS\n')

mycursor.execute("""
	DESCRIBE suppliers;
    """)

results = mycursor.fetchall()

print(tabulate(results, headers=['Field','Type','Null','KEY','Default','Extra'], tablefmt='psql'))
	
print('\nBRANDS\n')

mycursor.execute("""
	DESCRIBE brands;
    """)

results = mycursor.fetchall()

print(tabulate(results, headers=['Field','Type','Null','KEY','Default','Extra'], tablefmt='psql'))