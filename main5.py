from PyQt5.QtWidgets import QPushButton,QWidget,QVBoxLayout,QHBoxLayout,QApplication,QLabel
from PyQt5.QtCore import Qt
import sys

class MotherPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Sayfa")
        self.setFixedSize(990,800)
        self.initUI()

    def initUI(self):
        self.buttons=["Para Çekme","Para Yatırma","Ödeme İşlemleri","Döviz İşlemleri","Çıkış"]

        self.text=QLabel("LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ")
        self.text.setStyleSheet("font-size:40px; color:red; font-family:Arial")
        
        self.master_layout=QVBoxLayout()

        self.text_row=QHBoxLayout()
        self.text_row.addWidget(self.text,alignment=Qt.AlignmentFlag.AlignCenter)

        self.button_row1=QHBoxLayout()
        self.button_row2=QHBoxLayout()
        self.button_row3=QHBoxLayout()

        self.para_cekme = QPushButton(self.buttons[0])
        self.para_yatirma = QPushButton(self.buttons[1])
        self.odeme_islem = QPushButton(self.buttons[2])
        self.doviz = QPushButton(self.buttons[3])
        self.cikis = QPushButton(self.buttons[4])

        self.button_row1.addWidget(self.para_cekme)
        self.button_row1.addWidget(self.para_yatirma)
        self.para_cekme.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.para_yatirma.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        
        self.button_row2.addWidget(self.odeme_islem)
        self.button_row2.addWidget(self.doviz)
        self.odeme_islem.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.doviz.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.button_row3.addWidget(self.cikis)
        self.cikis.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.cikis.setFixedWidth(479)
        self.button_row3.addStretch()

        self.master_layout.addStretch()
        self.master_layout.addLayout(self.text_row)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.button_row1)
        self.master_layout.addStretch()

        self.master_layout.addLayout(self.button_row2)

        self.master_layout.addStretch()


        self.master_layout.addLayout(self.button_row3)
        self.master_layout.addStretch()
        self.setLayout(self.master_layout)

        self.setStyleSheet("QWidget {background:darkblue}")
        

        #Butonlara tıklandığında olacaklar
        self.para_cekme.clicked.connect(self.show_withdraw)
        self.para_yatirma.clicked.connect(self.show_deposit)
        self.odeme_islem.clicked.connect(self.payment)
        self.doviz.clicked.connect(self.foreign_currency)
        self.cikis.clicked.connect(self.exitting)
        

    def show_withdraw(self):
        from para_cekme import Withdraw
        self.withdraw_window = Withdraw()
        self.withdraw_window.show()
        self.close()
    
    def show_deposit(self):
        from para_yatirma import Deposit
        self.deposit_window = Deposit()
        self.deposit_window.show()
        self.close() 

    
    def payment(self):
        from odeme_islemleri import Paying
        self.pay=Paying()
        self.pay.show()
        self.close()
    
    def foreign_currency(self):
        from doviz import Foreign
        self.doviz_islem = Foreign()
        self.doviz_islem.show()
        self.close()
    
    def exitting(self):
        from login import Login
        self.getting_back = Login()
        self.getting_back.show()
        self.close()

