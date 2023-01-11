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
	SELECT * FROM stock WHERE sup_id=1;
    """)


results = mycursor.fetchall()

print(tabulate(results, headers=['gpu_id','price','deadstock','size','sup_id','unique_id'], tablefmt='psql'))