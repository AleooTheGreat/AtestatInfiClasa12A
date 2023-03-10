import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont
import mysql.connector
from tabulate import tabulate


        
class Window(QWidget):

    s = 'bruh'
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("bonk")
        self.setGeometry(620,100,500,400)
 
        self.setIcon()
 
        self.createGridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
 
        self.show()
 
 
 
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
 
    
    def createGridLayout(self):
        self.groupBox = QGroupBox("FILL IN THE BLANKS")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()
        
        labelId = QLabel()
        labelId.setText("gpu id")
        gridLayout.addWidget(labelId, 1,0)
        
        labelBrand = QLabel()
        labelBrand.setText("brand")
        gridLayout.addWidget(labelBrand, 2,0)
        
        labelName = QLabel()
        labelName.setText("name")
        gridLayout.addWidget(labelName, 3,0)
        
        labelmemory = QLabel()
        labelmemory.setText("memory")
        gridLayout.addWidget(labelmemory, 4,0)

        idbox = QLineEdit("",self)
        brandbox = QLineEdit("",self)
        namebox = QLineEdit("",self)
        memorybox = QLineEdit("",self)

        gridLayout.addWidget(idbox, 1,1)
        gridLayout.addWidget(brandbox, 2,1)
        gridLayout.addWidget(namebox, 3,1)
        gridLayout.addWidget(memorybox, 4,1)
        
        buttonST2 = QPushButton("SELECT", self)
        buttonST2.clicked.connect(lambda: do_thing_select())
        gridLayout.addWidget(buttonST2, 6,0)
        
        self.groupBox.setLayout(gridLayout)
        
        def do_thing_select():
            id1 = idbox.text()
            brand1 = brandbox.text()
            name1 = namebox.text()
            memory = memorybox.text()
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Leonida$27",
            database="bonk"
            )
            
            cond = " "
            movetoand = False
            
            
            if id1.strip():
                cond += (" WHERE gpu_id = " + id1)
                movetoand = True
            
            if brand1.strip():
                if not movetoand:
                    cond += (" WHERE brand = \'" + brand1 + "\'")
                    movetoand = True
                else:
                    cond += (" AND brand = \'" + brand1 + "\'")
            
            if name1.strip():
                if not movetoand:
                    cond += (" WHERE name =  \'" + name1 + "\'")
                    movetoand = True
                else:
                    cond += (" AND name = \'" + name1 + "\'")
                
            if memory.strip():
                if not movetoand:
                    cond += (" WHERE memory = \'" + memory + "\'")
                    movetoand = True
                else:
                    cond += (" AND memory = \'" + memory + "\'")
                
            mycursor = mydb.cursor(buffered=True)

            mycursor.execute("SELECT * FROM gpu " + cond + " ORDER BY name ASC")
            #print("SELECT * FROM gpu " + cond + " ORDER BY name ASC")

            head = ['gpu_id', 'brand', 'name', 'memory']
            
            results = mycursor.fetchall()

            print(tabulate(results, headers=head, tablefmt='psql'))
 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()

app = QApplication(sys.argv)                                                                        

app.exec_()