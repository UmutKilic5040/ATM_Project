from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
from PyQt5.QtCore import Qt
from pymongo import MongoClient
from bson.objectid import ObjectId

client1=MongoClient("mongodb://localhost:27017/")
db1=client1["Info"]
person1=db1["Person1"]

target_id="693eeb9406e3cb57ae437e23"
query1={"_id":ObjectId(target_id)}
person1_data=person1.find_one(query1)

class Deposit(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Para Yatırma")
        self.setFixedSize(990,800)
        self.initUI()
    def initUI(self):
        self.text=QLabel("YATIRMAK İSTEDİĞİNİZ TUTARI GİRİNİZ")
        
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text.setStyleSheet("font-size:40px; color:red; font-family:Arial")
        
        self.amount_bar=QLineEdit()
        self.amount_bar.setStyleSheet("QLineEdit{background:white;border: 10px solid white; border-radius:16px;font-family:Arial;font-size:40px}")
        self.amount_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.amount_bar.setFixedWidth(200)

        self.accept=QPushButton("Onayla")
        self.exit=QPushButton("Geri dön")

        self.accept.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.exit.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.master_layout=QVBoxLayout()
        self.row1=QHBoxLayout()
        self.row2=QHBoxLayout()
        
        self.row1.addWidget(self.amount_bar)
        self.row2.addWidget(self.accept)
        self.row2.addWidget(self.exit)
    
        self.master_layout.addStretch()   
        self.master_layout.addWidget(self.text)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row2)
        self.master_layout.addStretch()
        
        self.setStyleSheet("QWidget {background:darkblue}")
        self.setLayout(self.master_layout)
        
        self.accept.clicked.connect(self.depositing)
        self.exit.clicked.connect(self.get_back_from_deposit)
    
    def depositing(self):
        
        self.deposit_amount=float(self.amount_bar.text())
        
        person1.update_one(query1,{"$inc":{"current_value": self.deposit_amount}})

        self.text.setText(f"İşlem Başarılı!\nYatırılan: {self.deposit_amount}")

        self.amount_bar.clear()
    
    def get_back_from_deposit(self):
        from main5 import MotherPage
        self.get_back_to_menu=MotherPage()
        self.get_back_to_menu.show()
        self.close()
    
    