from PyQt5.QtWidgets import QApplication,QLabel,QHBoxLayout,QVBoxLayout,QWidget,QLineEdit,QPushButton,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

client1=MongoClient("mongodb://localhost:27017/")
db1=client1["Info"]
person1=db1["Person1"]
target_id="693eeb9406e3cb57ae437e23"

query1={"_id": ObjectId(target_id)}
person1_data=person1.find_one(query1)

class Login(QWidget):
    def __init__(self):
        super().__init__()    
        self.setWindowTitle("Login Page")
        self.setFixedSize(990,800)
        self.initUI()

    def initUI(self):
        self.text=QLabel("LÜTFEN ŞİFRENİZİ GİRİNİZ")
        self.text.setStyleSheet("font-size:50px; color:red; font-family:Arial")
        
        self.login_bar=QLineEdit()
        self.login_bar.setEchoMode(QLineEdit.Password)
        
        
        self.login_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_bar.setFixedWidth(120)
        self.login_bar.setStyleSheet("QLineEdit{background:white;border: 10px solid white; border-radius:16px;font-size:40px}")
        
        self.okay=QPushButton("Onayla")
        self.okay.setFixedWidth(100)
        self.okay.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red;font-size: 20px; font-weight:bold}")
        
        self.master_layout=QVBoxLayout()
        
        self.text_row=QHBoxLayout()
        self.bar_row=QHBoxLayout()
        self.button_row=QHBoxLayout()
        
        
        
        self.text_row.addWidget(self.text,alignment=Qt.AlignmentFlag.AlignCenter)
        
        
        self.bar_row.addWidget(self.login_bar)
        self.button_row.addWidget(self.okay)
        
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.text_row)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.bar_row)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.button_row)
        self.master_layout.addStretch()
        self.setLayout(self.master_layout)
        
        self.setStyleSheet("QWidget {background:darkblue}")
        self.show()
        self.okay.clicked.connect(self.loginning)

    def loginning(self):
        self.password=self.login_bar.text()
        if self.password == person1_data["password"]:
            from main5 import MotherPage
            self.loging=MotherPage()
            self.loging.show()
            self.close()
        else:
            self.warning_message= QMessageBox()
            self.warning_message.setWindowTitle("Hata!")
            self.warning_message.setText("Şifre Yanlış!")
            self.warning_message.setIcon(QMessageBox.Warning)
            self.warning_message.setStyleSheet("""
                QMessageBox{
                    background:darkblue;
                }
                QLabel{
                    color:white;
                    font-size: 16px;
                    font-family:Arial;

                }                                               
                QPushButton{
                    background:white; 
                    border: 10px solid white; 
                    border-radius:16px;
                    alignment: center;
                }
                                                                              """)
            self.login_bar.clear()
            self.warning_message.show()
            self.warning_message.exec_()
            

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=Login()
    sys.exit(app.exec_())
