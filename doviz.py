from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QApplication
from PyQt5.QtCore import Qt
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import requests
import sys

client=MongoClient("mongodb://localhost:27017/")
db=client["Info"]
person=db["Person1"]
rate_col=db["doviz_kurlari"]

target_id="693eeb9406e3cb57ae437e23"
query={"_id":ObjectId(target_id)}
person_data=person.find_one(query)

API_KEY ="11805879221b0ad1b71b9c24"

class Foreign(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Döviz İşlemleri")
        self.setFixedSize(990,800)
        self.initUI()
    def initUI(self):
        self.text=QLabel("LÜTFEN İŞLEM YAPMAK İSTEDİĞİNİZ KURU SEÇİN")
        self.text.setStyleSheet("font-size:40px; color:red; font-family:Arial")
        
        self.dollar=QPushButton("Dolar")
        self.dollar.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.euro=QPushButton("Euro")
        self.euro.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.sterlin=QPushButton("Sterlin")
        self.sterlin.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.manat=QPushButton("Manat")
        self.manat.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.frank=QPushButton("Frank")
        self.frank.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.geri_don=QPushButton("Geri Dön")
        self.geri_don.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.master_layout=QVBoxLayout()
        
        self.row1=QHBoxLayout()
        self.row2=QHBoxLayout()
        self.row3=QHBoxLayout()
        self.row4=QHBoxLayout()

        self.row1.addWidget(self.text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.row2.addWidget(self.dollar)
        self.row2.addWidget(self.euro)
        self.row3.addWidget(self.sterlin)
        self.row3.addWidget(self.manat)
        self.row4.addWidget(self.frank)
        self.row4.addWidget(self.geri_don)
        
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row3)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.row4)
        self.master_layout.addStretch()
        self.setLayout(self.master_layout)
        self.setStyleSheet("background:darkblue")

        #Buton fonksiyonları
        self.dollar.clicked.connect(self.go_to_dollar)
        self.euro.clicked.connect(self.go_to_euro)
        self.sterlin.clicked.connect(self.go_to_sterlin)
        self.manat.clicked.connect(self.go_to_manat)
        self.frank.clicked.connect(self.go_to_frank)
        self.geri_don.clicked.connect(self.get_back_from_foreign)

    def go_to_dollar(self):
        self.go_dollar=Dollar()
        self.go_dollar.show()
        self.close()
    
    def go_to_euro(self):
        self.go_euro=Euro()
        self.go_euro.show()
        self.close()

    def go_to_sterlin(self):
        self.go_sterlin=Sterlin()
        self.go_sterlin.show()
        self.close()

    def go_to_manat(self):
        self.go_manat=Manat()
        self.go_manat.show()
        self.close()

    def go_to_frank(self):
        self.go_frank=Frank()
        self.go_frank.show()
        self.close()
    
    def get_back_from_foreign(self):
        from main5 import MotherPage
        self.get_back_to_menu= MotherPage()
        self.get_back_to_menu.show()
        self.close()

class Dollar(QWidget):
    BASE_CURRENCY = "USD"
    API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dolar")
        self.setFixedSize(990,800)
        self.dolarUI()
    
    def dolarUI(self):
        self.master_layout=QVBoxLayout()
        
        self.dollar_text=QLabel(f"YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN (Dolar: {self.get_usd_rate():.2f})")
        self.dollar_text.setStyleSheet("font-size:40px; color:red; font-family:Arial")
        
        self.dollar_amount=QLineEdit()
        self.dollar_amount.setStyleSheet("QLineEdit{background:white;border: 10px solid white; border-radius:16px;font-family:Arial;font-size:40px}")
        self.dollar_amount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dollar_amount.setFixedWidth(200)
        
        self.dollar_withdraw=QPushButton("Para Çek")
        self.dollar_withdraw.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.dollar_deposit=QPushButton("Para Yatır")
        self.dollar_deposit.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")     
        
        self.get_back_to_foreign_from_dollar=QPushButton("Geri Dön")
        self.get_back_to_foreign_from_dollar.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.get_back_to_foreign_from_dollar.setFixedWidth(600)
        
        self.dollar_row1=QHBoxLayout()
        self.dollar_row2=QHBoxLayout()
        self.dollar_row3=QHBoxLayout()
        self.dollar_row4=QHBoxLayout()

        self.dollar_row1.addWidget(self.dollar_text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.dollar_row2.addWidget(self.dollar_amount)
        self.dollar_row3.addWidget(self.dollar_withdraw)
        self.dollar_row3.addWidget(self.dollar_deposit)
        self.dollar_row4.addWidget(self.get_back_to_foreign_from_dollar)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.dollar_row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.dollar_row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.dollar_row3)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.dollar_row4)
        self.master_layout.addStretch()
        self.setLayout(self.master_layout)

        self.dollar_withdraw.clicked.connect(self.withdraw_dollar)
        self.dollar_deposit.clicked.connect(self.deposit_dollar)
        self.get_back_to_foreign_from_dollar.clicked.connect(self.from_dollar_to_foreign)

        self.setStyleSheet("background:darkblue")

    def get_usd_rate(self):
        self.cached = rate_col.find_one({"base_code": "USD"})
        
        #Veri var mı ve 12 saat dolmadan önce veri tabanına kaydedilmiş mi
        if self.cached:
            self.last_fetched = self.cached.get("last_fetched")
            if self.last_fetched and(datetime.now() - self.last_fetched) < timedelta(hours=12):
                return self.cached["conversion_rates"]["TRY"]
        
        #Veri yoksa veya 12 saat dolmuşsa API'dan çek
        try:
            
            self.response = requests.get(self.API_URL)
            self.data = self.response.json()

            if self.data["result"] == "success":
                self.rates = self.data["conversion_rates"]

                #MongoDB'yi güncelle
                rate_col.update_one({"base_code": "USD"},{"$set":{"base_code": "USD","conversion_rates": self.rates,"last_fetched": datetime.now()}},upsert=True)
                return self.rates["TRY"]
            else:
                return None
        except:
            return None

    def withdraw_dollar(self):
        try:
            self.miktar = float(self.dollar_amount.text())
            self.kur = self.get_usd_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": -self.tutar_tl}})

            self.dollar_text.setText(f"İşlem Başarılı!\nÇekilen: {self.miktar}")

            self.dollar_amount.clear()
        except ValueError:
            self.dollar_text.setText("Lütfen Geçerli Bir Sayı Girin!")

    def deposit_dollar(self):
        try:
            self.miktar = float(self.dollar_amount.text())
            self.kur = self.get_usd_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": self.tutar_tl}})

            self.dollar_text.setText(f"İşlem Başarılı!\nYatırılan: {self.tutar_tl:.2f}")

            self.dollar_amount.clear()
        except ValueError:
            self.dollar_text.setText("Lütfen Geçerli Bir Sayı Girin!")

    def from_dollar_to_foreign(self):
        self.foreign_from_dollar=Foreign()
        self.foreign_from_dollar.show()
        self.close()

class Euro(QWidget):
    BASE_CURRENCY = "EUR"
    API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Euro")
        self.setFixedSize(990,800)
        self.euroUI()
    
    def euroUI(self):
        self.master_layout=QVBoxLayout()
        
        self.euro_text=QLabel(f"YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN (Euro: {self.get_euro_rate():.2f})")
        self.euro_text.setStyleSheet("font-size:40px; color:red; font-family:Arial")

        self.euro_amount=QLineEdit()
        self.euro_amount.setStyleSheet("QLineEdit{background:white;border: 10px solid white; border-radius:16px;font-family:Arial;font-size:40px}")
        self.euro_amount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.euro_amount.setFixedWidth(200)

        self.euro_withdraw=QPushButton("Para Çek")
        self.euro_withdraw.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.euro_deposit=QPushButton("Para Yatır")
        self.euro_deposit.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")      
        
        self.get_back_to_foreign_from_euro=QPushButton("Geri Dön")
        self.get_back_to_foreign_from_euro.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.get_back_to_foreign_from_euro.setFixedWidth(600)

        self.euro_row1=QHBoxLayout()
        self.euro_row2=QHBoxLayout()
        self.euro_row3=QHBoxLayout()
        self.euro_row4=QHBoxLayout()

        self.euro_row1.addWidget(self.euro_text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.euro_row2.addWidget(self.euro_amount)
        self.euro_row3.addWidget(self.euro_withdraw)
        self.euro_row3.addWidget(self.euro_deposit)
        self.euro_row4.addWidget(self.get_back_to_foreign_from_euro)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.euro_row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.euro_row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.euro_row3)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.euro_row4)
        self.master_layout.addStretch()
        self.setLayout(self.master_layout)

        self.setStyleSheet("background:darkblue")

        self.euro_withdraw.clicked.connect(self.withdraw_euro)
        self.euro_deposit.clicked.connect(self.deposit_euro)
        self.get_back_to_foreign_from_euro.clicked.connect(self.from_euro_to_foreign)

    def get_euro_rate(self):
        
        self.cached = rate_col.find_one({"base_code": "EUR"})
        
        #Veri var mı ve 12 saat dolmadan önce veri tabanına kaydedilmiş mi
        if self.cached:
            self.last_fetched = self.cached.get("last_fetched")
            if self.last_fetched and(datetime.now() - self.last_fetched) < timedelta(hours=12):
                return self.cached["conversion_rates"]["TRY"]
        
        #Veri yoksa veya 12 saat dolmuşsa API'dan çek
        try:
            self.response = requests.get(self.API_URL)
            self.data = self.response.json()

            if self.data["result"] == "success":
                self.rates = self.data["conversion_rates"]

                #MongoDB'yi güncelle
                rate_col.update_one({"base_code": "EUR"},{"$set":{"base_code": "EUR","conversion_rates": self.rates,"last_fetched": datetime.now()}},upsert=True)
                return self.rates["TRY"]
            else:
                return None
        except:
            return None
    def withdraw_euro(self):
        try:
            self.miktar = float(self.euro_amount.text())
            self.kur = self.get_euro_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": -self.tutar_tl}})

            self.euro_text.setText(f"İşlem Başarılı!\nÇekilen: {self.miktar}")

            self.euro_amount.clear()

        except ValueError:
            self.euro_text.setText("Lütfen Geçerli Bir Sayı Girin!")

    def deposit_euro(self):
        try:
            self.miktar = float(self.euro_amount.text())
            self.kur = self.get_euro_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": self.tutar_tl}})

            self.euro_text.setText(f"İşlem Başarılı!\nYatırılan: {self.tutar_tl:.2f}")
            
            self.euro_amount.clear()

        except ValueError:
            self.euro_text.setText("Lütfen Geçerli Bir Sayı Girin!")

    def from_euro_to_foreign(self):
        self.foreign_from_euro=Foreign()
        self.foreign_from_euro.show()
        self.close()

class Sterlin(QWidget):
    BASE_CURRENCY = "GBP"
    API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sterlin")
        self.setFixedSize(990,800)
        self.sterlinUI()
    def sterlinUI(self):
        self.master_layout=QVBoxLayout()
        
        self.sterlin_text=QLabel(f"YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN (Sterlin: {self.get_sterlin_rate():.2f})")
        self.sterlin_text.setStyleSheet("font-size:40px; color:red; font-family:Arial")

        self.sterlin_amount=QLineEdit()
        self.sterlin_amount.setStyleSheet("QLineEdit{background:white;border: 10px solid white; border-radius:16px;font-family:Arial;font-size:40px}")
        self.sterlin_amount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sterlin_amount.setFixedWidth(200)

        self.sterlin_withdraw=QPushButton("Para Çek")
        self.sterlin_withdraw.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.sterlin_deposit=QPushButton("Para Yatır")
        self.sterlin_deposit.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")        
        
        self.get_back_to_foreign_from_sterlin=QPushButton("Geri Dön")
        self.get_back_to_foreign_from_sterlin.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.get_back_to_foreign_from_sterlin.setFixedWidth(600)

        self.sterlin_row1=QHBoxLayout()
        self.sterlin_row2=QHBoxLayout()
        self.sterlin_row3=QHBoxLayout()
        self.sterlin_row4=QHBoxLayout()

        self.sterlin_row1.addWidget(self.sterlin_text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.sterlin_row2.addWidget(self.sterlin_amount)
        self.sterlin_row3.addWidget(self.sterlin_withdraw)
        self.sterlin_row3.addWidget(self.sterlin_deposit)
        self.sterlin_row4.addWidget(self.get_back_to_foreign_from_sterlin)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.sterlin_row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.sterlin_row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.sterlin_row3)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.sterlin_row4)
        self.master_layout.addStretch()
        self.setLayout(self.master_layout)

        self.setStyleSheet("background:darkblue")
        
        self.sterlin_withdraw.clicked.connect(self.withdraw_sterlin)
        self.sterlin_deposit.clicked.connect(self.deposit_sterlin)
        self.get_back_to_foreign_from_sterlin.clicked.connect(self.from_sterlin_to_foreign)

    def get_sterlin_rate(self):
        
        self.cached = rate_col.find_one({"base_code": "GBP"})
        
        #Veri var mı ve 12 saat dolmadan önce veri tabanına kaydedilmiş mi
        if self.cached:
            self.last_fetched = self.cached.get("last_fetched")
            if self.last_fetched and(datetime.now() - self.last_fetched) < timedelta(hours=12):
                return self.cached["conversion_rates"]["TRY"]
        
        #Veri yoksa veya 12 saat dolmuşsa API'dan çek
        try:
            self.response = requests.get(self.API_URL)
            self.data = self.response.json()

            if self.data["result"] == "success":
                self.rates = self.data["conversion_rates"]

                #MongoDB'yi güncelle
                rate_col.update_one({"base_code": "GBP"},{"$set":{"base_code": "GBP","conversion_rates": self.rates,"last_fetched": datetime.now()}},upsert=True)
                return self.rates["TRY"]
            else:
                return None
        except:
            return None
    def withdraw_sterlin(self):
        try:
            self.miktar = float(self.sterlin_amount.text())
            self.kur = self.get_sterlin_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": -self.tutar_tl}})

            self.sterlin_text.setText(f"İşlem Başarılı!\nÇekilen: {self.miktar}")

            self.sterlin_amount.clear()

        except ValueError:
            self.sterlin_text.setText("Lütfen Geçerli Bir Sayı Girin!")

    def deposit_sterlin(self):
        try:
            self.miktar = float(self.sterlin_amount.text())
            self.kur = self.get_sterlin_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": self.tutar_tl}})

            self.sterlin_text.setText(f"İşlem Başarılı!\nYatırılan: {self.tutar_tl:.2f}")
            
            self.sterlin_amount.clear()

        except ValueError:
            self.sterlin_text.setText("Lütfen Geçerli Bir Sayı Girin!")
        
    def from_sterlin_to_foreign(self):
        self.foreign_from_sterlin=Foreign()
        self.foreign_from_sterlin.show()
        self.close()

class Manat(QWidget):
    BASE_CURRENCY = "AZN"
    API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manat")
        self.setFixedSize(990,800)
        self.manatUI()
    def manatUI(self):
        self.master_layout=QVBoxLayout()
        
        self.manat_text=QLabel(f"YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN (Manat: {self.get_manat_rate():.2f})")
        self.manat_text.setStyleSheet("font-size:40px; color:red; font-family:Arial")

        self.manat_amount=QLineEdit()
        self.manat_amount.setStyleSheet("QLineEdit{background:white;border: 10px solid white; border-radius:16px;font-family:Arial;font-size:40px}")
        self.manat_amount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.manat_amount.setFixedWidth(200)

        self.manat_withdraw=QPushButton("Para Çek")
        self.manat_withdraw.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.manat_deposit=QPushButton("Para Yatır")
        self.manat_deposit.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.get_back_to_foreign_from_manat=QPushButton("Geri Dön")
        self.get_back_to_foreign_from_manat.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.get_back_to_foreign_from_manat.setFixedWidth(600)
        
        self.manat_row1=QHBoxLayout()
        self.manat_row2=QHBoxLayout()
        self.manat_row3=QHBoxLayout()
        self.manat_row4=QHBoxLayout()

        self.manat_row1.addWidget(self.manat_text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.manat_row2.addWidget(self.manat_amount)
        self.manat_row3.addWidget(self.manat_withdraw)
        self.manat_row3.addWidget(self.manat_deposit)
        self.manat_row4.addWidget(self.get_back_to_foreign_from_manat)
        
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.manat_row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.manat_row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.manat_row3)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.manat_row4)
        self.master_layout.addStretch()

        self.setLayout(self.master_layout)

        self.setStyleSheet("background:darkblue")
        
        self.manat_withdraw.clicked.connect(self.withdraw_manat)
        self.manat_deposit.clicked.connect(self.deposit_manat)
        self.get_back_to_foreign_from_manat.clicked.connect(self.from_manat_to_foreign)
        
    def get_manat_rate(self):
        
        self.cached = rate_col.find_one({"base_code": "AZN"})
        
        #Veri var mı ve 12 saat dolmadan önce veri tabanına kaydedilmiş mi
        if self.cached:
            self.last_fetched = self.cached.get("last_fetched")
            if self.last_fetched and(datetime.now() - self.last_fetched) < timedelta(hours=12):
                return self.cached["conversion_rates"]["TRY"]
        
        #Veri yoksa veya 12 saat dolmuşsa API'dan çek
        try:
            self.response = requests.get(self.API_URL)
            self.data = self.response.json()

            if self.data["result"] == "success":
                self.rates = self.data["conversion_rates"]

                #MongoDB'yi güncelle
                rate_col.update_one({"base_code": "AZN"},{"$set":{"base_code": "AZN","conversion_rates": self.rates,"last_fetched": datetime.now()}},upsert=True)
                return self.rates["TRY"]
            else:
                return None
        except:
            return None
    def withdraw_manat(self):
        try:
            self.miktar = float(self.manat_amount.text())
            self.kur = self.get_manat_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": -self.tutar_tl}})

            self.manat_text.setText(f"İşlem Başarılı!\nÇekilen: {self.miktar}")

            self.manat_amount.clear()

        except ValueError:
            self.manat_text.setText("Lütfen Geçerli Bir Sayı Girin!")

    def deposit_manat(self):
        try:
            self.miktar = float(self.manat_amount.text())
            self.kur = self.get_manat_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": self.tutar_tl}})

            self.manat_text.setText(f"İşlem Başarılı!\nYatırılan: {self.tutar_tl:.2f}")
            self.manat_amount.clear()
        except ValueError:
            self.manat_text.setText("Lütfen Geçerli Bir Sayı Girin!")
        
    def from_manat_to_foreign(self):
        self.foreign_from_manat=Foreign()
        self.foreign_from_manat.show()
        self.close()

class Frank(QWidget):
    BASE_CURRENCY = "CHF"
    API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Frank")
        self.setFixedSize(990,800)
        self.frankUI()

    def frankUI(self):
        self.master_layout=QVBoxLayout()        
        
        self.frank_text=QLabel(f"YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN (Frank: {self.get_frank_rate():.2f})")
        self.frank_text.setStyleSheet("font-size:40px; color:red; font-family:Arial")

        self.frank_amount=QLineEdit()
        self.frank_amount.setStyleSheet("QLineEdit{background:white;border: 10px solid white; border-radius:16px;font-family:Arial;font-size:40px}")
        self.frank_amount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frank_amount.setFixedWidth(200)

        self.frank_withdraw=QPushButton("Para Çek")
        self.frank_withdraw.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        
        self.frank_deposit=QPushButton("Para Yatır")
        self.frank_deposit.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")

        self.get_back_to_foreign_from_frank=QPushButton("Geri Dön")
        self.get_back_to_foreign_from_frank.setStyleSheet("QPushButton {background:white; border: 10px solid white; border-radius:16px; font-size: 20px; font-weight:bold} QPushButton:hover{background:red; border: 10px solid red; font-size: 20px; font-weight:bold}")
        self.get_back_to_foreign_from_frank.setFixedWidth(600)

        self.frank_row1=QHBoxLayout()
        self.frank_row2=QHBoxLayout()
        self.frank_row3=QHBoxLayout()
        self.frank_row4=QHBoxLayout()

        self.frank_row1.addWidget(self.frank_text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.frank_row2.addWidget(self.frank_amount)
        self.frank_row3.addWidget(self.frank_withdraw)
        self.frank_row3.addWidget(self.frank_deposit)
        self.frank_row4.addWidget(self.get_back_to_foreign_from_frank)
        
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.frank_row1)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.frank_row2)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.frank_row3)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.frank_row4)
        self.master_layout.addStretch()

        self.setLayout(self.master_layout)
        
        self.setStyleSheet("background:darkblue")
        
        self.frank_withdraw.clicked.connect(self.withdraw_frank)
        self.frank_deposit.clicked.connect(self.deposit_frank)
        self.get_back_to_foreign_from_frank.clicked.connect(self.from_frank_to_foreign)

    def get_frank_rate(self):
        
        self.cached = rate_col.find_one({"base_code": "CHF"})
        
        #Veri var mı ve 12 saat dolmadan önce veri tabanına kaydedilmiş mi
        if self.cached:
            self.last_fetched = self.cached.get("last_fetched")
            if self.last_fetched and(datetime.now() - self.last_fetched) < timedelta(hours=12):
                return self.cached["conversion_rates"]["TRY"]
        
        #Veri yoksa veya 12 saat dolmuşsa API'dan çek
        try:
            self.response = requests.get(self.API_URL)
            self.data = self.response.json()

            if self.data["result"] == "success":
                self.rates = self.data["conversion_rates"]

                #MongoDB'yi güncelle
                rate_col.update_one({"base_code": "CHF"},{"$set":{"base_code": "CHF","conversion_rates": self.rates,"last_fetched": datetime.now()}},upsert=True)
                return self.rates["TRY"]
            else:
                return None
        except:
            return None
    def withdraw_frank(self):
        try:
            self.miktar = float(self.frank_amount.text())
            self.kur = self.get_frank_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": -self.tutar_tl}})

            self.frank_text.setText(f"İşlem Başarılı!\nÇekilen: {self.miktar}")
            self.frank_amount.clear()
        except ValueError:
            self.frank_text.setText("Lütfen Geçerli Bir Sayı Girin!")

    def deposit_frank(self):
        try:
            self.miktar = float(self.frank_amount.text())
            self.kur = self.get_frank_rate()

            self.tutar_tl=self.miktar * self.kur

            

            person.update_one(query,{"$inc":{"current_value": self.tutar_tl}})

            self.frank_text.setText(f"İşlem Başarılı!\nYatırılan: {self.tutar_tl:.2f}")
            self.frank_amount.clear()
        except ValueError:
            self.frank_text.setText("Lütfen Geçerli Bir Sayı Girin!")
        
    
        
    def from_frank_to_foreign(self):
        self.foreign_from_frank=Foreign()
        self.foreign_from_frank.show()
        self.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=Foreign()
    window.show()
    sys.exit(app.exec_())