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

class Withdraw(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Para Çekme")
        self.setFixedSize(990,800)
        self.initUI()
    
    def initUI(self):
        self.master_layout=QVBoxLayout()
        
        self.message=QLabel("ÇEKMEK İSTEDİĞİNİZ TUTARI GİRİNİZ")
        self.message.setStyleSheet("font-size:40px; color:red; font-family:Arial")
        self.amount=QLineEdit()
        
        
        self.accept=QPushButton("Onayla")
        self.exit=QPushButton("Geri Dön")

        self.amount.setStyleSheet("QLineEdit{background:white;border: 10px solid white; border-radius:16px;font-family:Arial;font-size:40px}")
        self.amount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.amount.setFixedWidth(200)
        self.accept.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.exit.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.row1=QHBoxLayout()
        self.row2=QHBoxLayout()
        self.row3=QHBoxLayout()

        self.row1.addWidget(self.message,alignment=Qt.AlignmentFlag.AlignCenter)
        self.row2.addWidget(self.amount)
        self.row3.addWidget(self.accept)
        self.row3.addWidget(self.exit)
        
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row3)


        self.accept.clicked.connect(self.withdrawing)
        self.exit.clicked.connect(self.get_back_from_withdraw)

        self.setStyleSheet("QWidget {background:darkblue}")

        self.setLayout(self.master_layout)
        self.master_layout.addStretch()
        
    def get_back_from_withdraw(self):
        from main5 import MotherPage
        self.getting_back_menu=MotherPage()
        self.getting_back_menu.show()
        self.close()
        
    def withdrawing(self):
        self.withdraw_amount=float(self.amount.text())
        
        person1.update_one(query1,{"$inc":{"current_value": -self.withdraw_amount}})

        self.message.setText(f"İşlem Başarılı!\nÇekilen: {self.withdraw_amount}")

        self.amount.clear()

        
        

